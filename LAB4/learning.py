#os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

import os
import re
import glob
import numpy as np
import os.path as path
from scipy import ndimage, misc

from keras.models import Sequential
from keras.layers import Activation, Dropout, Flatten, Dense, Conv2D, MaxPooling2D, BatchNormalization
from keras.callbacks import EarlyStopping, TensorBoard
from keras.utils import print_summary, to_categorical
from keras import regularizers, optimizers
from keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import accuracy_score, f1_score
from datetime import datetime

import pickle

PATH = 'D:\Jhonatan\Documentos\AI\Vision\LAB4\cifar-10-batches-py'

def load_cfar10_batch(PATH, batch_id):
    with open(PATH + '\data_batch_' + str(batch_id), mode='rb') as file:
        batch = pickle.load(file, encoding='latin1')

    features = batch['data'].reshape((len(batch['data']), 3, 32, 32)).transpose(0, 2, 3, 1)
    labels = batch['labels']

    return features, labels

batch_data, batch_labels = [], []

for i in range(5):
    data, label = load_cfar10_batch(PATH, i + 1)
    batch_data.append(data)
    batch_labels.append(label)

images = np.concatenate((batch_data[0], batch_data[1], batch_data[2], batch_data[3], batch_data[4]), axis=0)
labels = np.concatenate((batch_labels[0], batch_labels[1], batch_labels[2], batch_labels[3], batch_labels[4]), axis=0)

image_size = np.asarray([images.shape[1], images.shape[2], images.shape[3]])
print(image_size)
labels = np.asarray(labels)

images = images / 255
n_images = 50000
k_split = 0.9

split_index = int(k_split * n_images)
shuffled_indices = np.random.permutation(n_images)
train_indices = shuffled_indices[0:split_index]
test_indices = shuffled_indices[split_index:]

x_train = images[train_indices, :, :]
y_train = labels[train_indices]
x_test = images[test_indices, :, :]
y_test = labels[test_indices]

y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)


def cnn(size, n_layers):
    KERNEL = (3, 3)
    neurons = [32, 32, 64, 64, 128, 128]
    drop = [0.2, 0.3, 0.4]
    weight_decay = 1e-4
    k = 0
    model = Sequential()

    for i in range(0, n_layers):
        if i == 0:
            shape = (size[0], size[1], size[2])
            model.add(Conv2D(neurons[i], KERNEL, padding='same', kernel_regularizer=regularizers.l2(weight_decay), input_shape=shape))
        else:
            model.add(Conv2D(neurons[i], KERNEL, padding='same', kernel_regularizer=regularizers.l2(weight_decay)))

        #model.add(MaxPooling2D(pool_size=(2, 2)))
        #model.add(Dropout(0.3))
        model.add(Activation('relu'))
        model.add(BatchNormalization())
        if (i + 1) % 2 == 0:
            model.add(MaxPooling2D(pool_size=(2, 2)))
            model.add(Dropout(drop[k]))
            k += 1

    #model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    #model.add(Dense(MAX_NEURONS))
    #model.add(Activation('relu'))
    #model.add(Dropout(0.3))

    model.add(Dense(10))
    model.add(Activation('softmax'))

    opt_rms = optimizers.rmsprop(lr=0.001, decay=1e-6)

    model.compile(loss='categorical_crossentropy',
                  optimizer=opt_rms,
                  metrics=['accuracy'])
    model.summary()

    return model

datagen = ImageDataGenerator(
    featurewise_center=False,
    samplewise_center=False,
    featurewise_std_normalization=False,
    samplewise_std_normalization=False,
    zca_whitening=False,
    rotation_range=15,
    width_shift_range=0.1,
    height_shift_range=0.1,
    horizontal_flip=True,
    vertical_flip=False
    )
datagen.fit(x_train)

model = cnn(image_size, 6)
epochs = 150
batch_size = 64

PATIENCE = 10
early_stopping = EarlyStopping(monitor='loss', min_delta=0, patience=PATIENCE, verbose=0, mode='auto')

LOG_DIRECTORY_ROOT = 'D:\Jhonatan\Documentos\DL\LAB3\Log'
now = datetime.utcnow().strftime("%Y%m%d%H%M%S")
log_dir = "{}/run-{}/".format(LOG_DIRECTORY_ROOT, now)
tensorboard = TensorBoard(log_dir=log_dir, write_graph=True, write_images=True)

callbacks = [early_stopping, tensorboard]

model.fit(x_train, y_train, epochs=epochs, batch_size=batch_size, callbacks=callbacks, verbose=1)

score = model.evaluate(x_test, y_test, verbose=1)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

model.fit_generator(datagen.flow(x_train, y_train, batch_size=batch_size), steps_per_epoch=x_train.shape[0] // batch_size, epochs=epochs, verbose=1, validation_data=(x_test, y_test), callbacks=callbacks)

test_predictions = model.predict(x_test)
test_predictions = np.round(test_predictions)

# Report the accuracy
accuracy = accuracy_score(y_test, test_predictions)
print("Accuracy: " + str(accuracy))

model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)

model.save('model.h5')

score = model.evaluate(x_test, y_test, verbose=1)
print('Test loss:', score[0])
print('Test accuracy:', score[1])