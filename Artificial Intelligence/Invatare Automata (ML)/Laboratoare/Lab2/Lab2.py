import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import MultinomialNB

train_images = np.loadtxt('train_images.txt') 
train_labels = np.loadtxt('train_labels.txt').astype(int)
test_images = np.loadtxt('test_images.txt')
test_labels = np.loadtxt('test_labels.txt').astype(int)

#2
def values_to_bins(X, num_bins):
    bins = np.linspace(start=0, stop=255, num=num_bins)
    x_to_bins = np.digitize(X, bins) - 1 
    return x_to_bins

# 3 + 4
bin_options = [3, 5, 7, 9, 11]
best_accuracy = 0
best_bins = 0

for num_bins in bin_options:
    train_binned = values_to_bins(train_images, num_bins)
    test_binned = values_to_bins(test_images, num_bins)
    
    naive_bayes_model = MultinomialNB()
    naive_bayes_model.fit(train_binned, train_labels)
    
    accuracy = naive_bayes_model.score(test_binned, test_labels)
    print(f"Acuratete pentru {num_bins} sub-intervale: {accuracy * 100:.2f}%")
    
    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_bins = num_bins


#5
print(f"\nCel mai bun model a avut {best_bins} bins.")
train_binned_best = values_to_bins(train_images, best_bins)
test_binned_best = values_to_bins(test_images, best_bins)

best_model = MultinomialNB()
best_model.fit(train_binned_best, train_labels)
predictions = best_model.predict(test_binned_best)



misclassified_indices = np.where(predictions != test_labels)[0]

for i in range(min(10, len(misclassified_indices))):
    idx = misclassified_indices[i]
    image = test_images[idx]
    image = np.reshape(image, (28, 28))
    
    plt.imshow(image.astype(np.uint8), cmap='gray')
    plt.title(f"Clasificata ca {predictions[idx]}, dar este {test_labels[idx]}")
    plt.axis('off')
    plt.show()

#6

def confusion_matrix(y_true, y_pred):
    num_classes = len(np.unique(y_true))
    matrix = np.zeros((num_classes, num_classes), dtype=int)
    for t, p in zip(y_true, y_pred):
        matrix[t, p] += 1
    return matrix

conf_matrix = confusion_matrix(test_labels, predictions)
print("\nMatricea de confuzie:")
print(conf_matrix)