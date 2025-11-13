#include <iostream>
#include <vector>

using namespace std;

struct Node
{
    int val;
    Node *left, *right;
    Node(int val)
    {
        this->val = val;
        left = right = NULL;
    }
};

Node *insert(Node *node, int val)
{
    if (!node)
        return new Node(val);
    if (node->val > val)
    {
        node->left = insert(node->left, val);
    }
    else if (node->val < val)
    {
        node->right = insert(node->right, val);
    }
    return node;
}

void inorder(Node *node)
{
    if (!node)
        return;
    inorder(node->left);
    cout << node->val << ' ';
    inorder(node->right);
}

void preorder(Node *node)
{
    if (!node)
        return;
    cout << node->val << ' ';
    preorder(node->left);
    preorder(node->right);
}

void postorder(Node *node)
{
    if (!node)
        return;
    postorder(node->left);
    postorder(node->right);
    cout << node->val << ' ';
}

Node *succ(Node *node)
{
    node = node->right;
    while (node && node->left)
        node = node->left;
    return node;
}

Node *remove(Node *node, int val)
{
    if (!node)
        return NULL;
    if (node->val > val)
    {
        node->left = remove(node->left, val);
        return node;
    }
    else if (node->val < val)
    {
        node->right = remove(node->right, val);
        return node;
    }
    // Node->val = val
    if (!node->left && !node->right)
    {
        delete node;
        return NULL;
    }
    else if (!node->left || !node->right)
    {
        Node *fiu;
        if (node->left)
            fiu = node->left;
        else
            fiu = node->right;
        delete node;
        return fiu;
    }
    Node *s = succ(node);
    node->val = s->val;
    node->right = remove(node->right, s->val);
    return node;
}

Node *search(Node *node, int val)
{
    if (!node)
        return NULL;
    if (node->val > val)
        return search(node->left, val);
    else if (node->val < val)
        return search(node->right, val);
    return node;
}

int main()
{
    Node *BST = NULL;
    BST = insert(BST, 5);
    BST = insert(BST, 2);
    BST = insert(BST, 3);
    BST = insert(BST, 1);
    BST = insert(BST, 7);
    BST = insert(BST, 6);
    BST = insert(BST, 8);
    cout << "inorder: ";
    inorder(BST);
    cout << "\npreorder: ";
    preorder(BST);
    cout << "\npostorder: ";
    postorder(BST);
    BST = remove(BST, 5);
    cout << "\n\nDupa Stergere: \n";
    cout << "inorder: ";
    inorder(BST);
    cout << "\npreorder: ";
    preorder(BST);
    cout << "\npostorder: ";
    postorder(BST);

    cout << '\n';
    cout << search(BST, 7);
}// TIP See CLion help at <a
// href="https://www.jetbrains.com/help/clion/">jetbrains.com/help/clion/</a>.
//  Also, you can try interactive lessons for CLion by selecting
//  'Help | Learn IDE Features' from the main menu.