## CIFAR-10 Image Classification using TensorFlow and Keras

This project demonstrates the implementation of two deep learning models—an Artificial Neural Network (ANN) and a Convolutional Neural Network (CNN)—for image classification using the CIFAR-10 dataset. The CIFAR-10 dataset consists of 60,000 32x32 color images in 10 classes, with 6,000 images per class.

## Dataset

The CIFAR-10 dataset is automatically downloaded and loaded using TensorFlow. It is split into 50,000 training images and 10,000 test images. The 10 classes in the dataset are:

1. Airplane
2. Automobile
3. Bird
4. Cat
5. Deer
6. Dog
7. Frog
8. Horse
9. Ship
10. Truck

## Code Overview

1. Data Loading and Preprocessing
The CIFAR-10 dataset is loaded using tensorflow.keras.datasets.cifar10.load_data().
The images are normalized by dividing by 255 to scale the pixel values to the range [0, 1].
The labels are reshaped for compatibility with the models.
2. Visualization
A sample image from the dataset is visualized using Matplotlib, along with its corresponding label.

def plot_sample(X, y, index):
    plt.figure(figsize=(4, 4))
    plt.imshow(X[index])
    plt.xlabel(classes[y[index]])

3. Artificial Neural Network (ANN)
An ANN model is created using Keras with the following layers:

Flatten layer to convert the 2D image into a 1D array.
Two Dense layers with 3000 and 1000 neurons, respectively, using ReLU activation.
Output layer with 10 neurons and a softmax activation function for multi-class classification.
The model is compiled with:

Optimizer: SGD
Loss function: Sparse Categorical Crossentropy
Metric: Accuracy
The model is trained for 5 epochs and evaluated on the test dataset.

4. Convolutional Neural Network (CNN)
A CNN model is created using Keras with the following layers:

Two Conv2D layers with 32 and 64 filters, respectively, and ReLU activation.
Two MaxPooling2D layers to reduce the spatial dimensions.
Flatten layer to convert the 2D image into a 1D array.
Dense layer with 64 neurons using ReLU activation.
Output layer with 10 neurons and a softmax activation function for multi-class classification.
The model is compiled with:

Optimizer: SGD
Loss function: Sparse Categorical Crossentropy
Metric: Accuracy
The model is trained for 10 epochs and evaluated on the test dataset.

5. Prediction and Visualization
The CNN model is used to predict the class of images from the test dataset.
A sample of the predictions is compared with the actual labels, and the corresponding images are visualized.

## Results

The ANN model is a basic approach and may not perform as well as the CNN model, which is specifically designed for image data.
The CNN model should show better performance in terms of accuracy on the test dataset.