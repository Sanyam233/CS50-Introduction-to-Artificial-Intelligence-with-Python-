import cv2
import numpy as np
import os
import sys
import tensorflow as tf

from sklearn.model_selection import train_test_split

EPOCHS = 10
IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43
TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) not in [2, 3]:
        sys.exit("Usage: python traffic.py data_directory [model.h5]")

    # Get image arrays and labels for all image files
    images, labels = load_data(sys.argv[1]) 

    # Split data into training and testing sets
    labels = tf.keras.utils.to_categorical(labels)
    x_train, x_test, y_train, y_test = train_test_split(
        np.array(images), np.array(labels), test_size=TEST_SIZE
    )

    # Get a compiled neural network
    model = get_model()

    # Fit model on training data
    model.fit(x_train, y_train, epochs=EPOCHS)

    # Evaluate neural network performance
    model.evaluate(x_test,  y_test, verbose=2)

    # Save model to file
    if len(sys.argv) == 3:
        filename = sys.argv[2]
        model.save(filename)
        print(f"Model saved to {filename}.")


def load_data(data_dir):
    """
    Load image data from directory `data_dir`.

    Assume `data_dir` has one directory named after each category, numbered
    0 through NUM_CATEGORIES - 1. Inside each category directory will be some
    number of image files.

    Return tuple `(images, labels)`. `images` should be a list of all
    of the images in the data directory, where each image is formatted as a
    numpy ndarray with dimensions IMG_WIDTH x IMG_HEIGHT x 3. `labels` should
    be a list of integer labels, representing the categories for each of the
    corresponding `images`.
    """

    images = []
    labels = []

    for dic in range(NUM_CATEGORIES):

        #path of image directories 
        path = os.path.join(data_dir, f"{dic}")

        #list all the files in that directory
        files = [f for f in os.listdir(path)]

        for img in files:

            #reads the image
            img = cv2.imread(os.path.join(path,img),cv2.IMREAD_COLOR)

            #resize the image
            img = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT))

            #adds images and labels to the list 
            images.append(img/255.0)
            labels.append(dic)

    return images, labels



    


def get_model():
    """
    Returns a compiled convolutional neural network model. Assume that the
    `input_shape` of the first layer is `(IMG_WIDTH, IMG_HEIGHT, 3)`.
    The output layer should have `NUM_CATEGORIES` units, one for each category.
    """
    #creating a convolutional neural net
    model = tf.keras.models.Sequential([

        #using convolution to identify important features of the image 
        tf.keras.layers.Conv2D(32, (3,3), activation="relu", input_shape = (30,30,3)),

        #reducing the dimensions of the image
        tf.keras.layers.MaxPooling2D(pool_size=(2,2)),

        #using convolution to identify important features of the image 
        tf.keras.layers.Conv2D(32, (3,3), activation="relu"),

        #reducing the dimensions of the image
        tf.keras.layers.MaxPooling2D(pool_size=(2,2)),
        
        #Flattening units
        tf.keras.layers.Flatten(),

        #adding hidden layers
        tf.keras.layers.Dense(132, activation="relu"),
        tf.keras.layers.Dense(64, activation="relu"),

        #randomly dropping nodes from hidden layers to avoid overfitting 
        tf.keras.layers.Dropout(0.5),

        #output layer
        tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax")
    ])

    #model complilation 
    model.compile(
        optimizer = "adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )

    #returning the model 
    return model


if __name__ == "__main__":
    main()
