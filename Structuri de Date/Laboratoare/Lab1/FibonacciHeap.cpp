#include <iostream>
#include <cmath>
#include <unordered_map>
#include <vector>
#include <limits>

using namespace std;

struct FibonacciNode {
    int key;
    int degree;
    bool marked;
    FibonacciNode* parent;
    FibonacciNode* child;
    FibonacciNode* left;
    FibonacciNode* right;

    FibonacciNode(int val) : key(val), degree(0), marked(false),
                           parent(nullptr), child(nullptr),
                           left(this), right(this) {}
};

class FibonacciHeap {
private:
    FibonacciNode* minNode;
    int size;
    unordered_map<int, FibonacciNode*> nodeMap;

    void consolidate() {
        int maxDegree = static_cast<int>(log2(size)) + 1;
        vector<FibonacciNode*> degreeTable(maxDegree, nullptr);
        
        FibonacciNode* current = minNode;
        vector<FibonacciNode*> nodesToProcess;
        
        do {
            nodesToProcess.push_back(current);
            current = current->right;
        } while (current != minNode);
        
        for (auto x : nodesToProcess) {
            int d = x->degree;
            while (degreeTable[d] != nullptr) {
                FibonacciNode* y = degreeTable[d];
                if (x->key > y->key) {
                    swap(x, y);
                }
                link(y, x);
                degreeTable[d] = nullptr;
                d++;
            }
            degreeTable[d] = x;
        }
        
        minNode = nullptr;
        for (auto node : degreeTable) {
            if (node) {
                if (!minNode) {
                    minNode = node;
                    minNode->left = minNode->right = minNode;
                } else {
                    node->right = minNode;
                    node->left = minNode->left;
                    minNode->left->right = node;
                    minNode->left = node;
                    
                    if (node->key < minNode->key) {
                        minNode = node;
                    }
                }
            }
        }
    }

    void link(FibonacciNode* y, FibonacciNode* x) {
        y->left->right = y->right;
        y->right->left = y->left;
        
        y->parent = x;
        if (!x->child) {
            x->child = y;
            y->left = y->right = y;
        } else {
            y->right = x->child;
            y->left = x->child->left;
            x->child->left->right = y;
            x->child->left = y;
        }
        
        x->degree++;
        y->marked = false;
    }

    void cut(FibonacciNode* x, FibonacciNode* y) {
        if (x->right == x) {
            y->child = nullptr;
        } else {
            y->child = x->right;
            x->left->right = x->right;
            x->right->left = x->left;
        }
        
        y->degree--;
        
        x->left = minNode->left;
        x->right = minNode;
        minNode->left->right = x;
        minNode->left = x;
        
        x->parent = nullptr;
        x->marked = false;
    }

    void cascadingCut(FibonacciNode* y) {
        FibonacciNode* z = y->parent;
        if (z) {
            if (!y->marked) {
                y->marked = true;
            } else {
                cut(y, z);
                cascadingCut(z);
            }
        }
    }

public:
    FibonacciHeap() : minNode(nullptr), size(0) {}
    
    ~FibonacciHeap() {
        if (!minNode) return;
        FibonacciNode* current = minNode;
        do {
            FibonacciNode* next = current->right;
            delete current;
            current = next;
        } while (current != minNode);
    }

    void insert(int key) {
        FibonacciNode* newNode = new FibonacciNode(key);
        nodeMap[key] = newNode;
        
        if (!minNode) {
            minNode = newNode;
        } else {
            newNode->right = minNode;
            newNode->left = minNode->left;
            minNode->left->right = newNode;
            minNode->left = newNode;
            
            if (newNode->key < minNode->key) {
                minNode = newNode;
            }
        }
        size++;
    }

    int extractMin() {
        if (!minNode) {
            throw runtime_error("Heap is empty");
        }
        
        FibonacciNode* z = minNode;
        int minKey = z->key;
        nodeMap.erase(minKey);
        
        if (z->child) {
            FibonacciNode* child = z->child;
            do {
                FibonacciNode* nextChild = child->right;
                child->left = minNode->left;
                child->right = minNode;
                minNode->left->right = child;
                minNode->left = child;
                child->parent = nullptr;
                child = nextChild;
            } while (child != z->child);
        }
        
        z->left->right = z->right;
        z->right->left = z->left;
        
        if (z == z->right) {
            minNode = nullptr;
        } else {
            minNode = z->right;
            consolidate();
        }
        
        delete z;
        size--;
        return minKey;
    }

    void decreaseKey(int oldKey, int newKey) {
        if (newKey > oldKey) {
            throw runtime_error("New key is greater than current key");
        }
        
        FibonacciNode* x = nodeMap[oldKey];
        if (!x) {
            throw runtime_error("Key not found");
        }
        
        x->key = newKey;
        nodeMap.erase(oldKey);
        nodeMap[newKey] = x;
        
        FibonacciNode* y = x->parent;
        
        if (y && x->key < y->key) {
            cut(x, y);
            cascadingCut(y);
        }
        
        if (x->key < minNode->key) {
            minNode = x;
        }
    }

    void deleteNode(int key) {
        decreaseKey(key, numeric_limits<int>::min());
        extractMin();
    }

    bool isEmpty() const { return minNode == nullptr; }
    int getSize() const { return size; }
    int getMin() const { return minNode ? minNode->key : numeric_limits<int>::max(); }
};

int main() {
    //asta e generata
    FibonacciHeap fibHeap;
    
    fibHeap.insert(5);
    fibHeap.insert(3);
    fibHeap.insert(7);
    fibHeap.insert(2);
    fibHeap.insert(8);
    fibHeap.insert(1);
    
    cout << "Extracted min: " << fibHeap.extractMin() << endl;
    
    fibHeap.decreaseKey(7, 4);
    fibHeap.deleteNode(5);
    
    while (!fibHeap.isEmpty()) {
        cout << fibHeap.extractMin() << " ";
    }
    
    return 0;
}