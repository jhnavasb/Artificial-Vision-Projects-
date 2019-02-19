import numpy as np
import pickle
from keras.models import model_from_json
import matplotlib.pyplot as plt

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

# Load trained CNN model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)
model.load_weights('model.h5')

labels = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

count = 0
figure = plt.figure()
maximum_square = np.ceil(np.sqrt(x_test[:16].shape[0]))

indices = np.argmax(model.predict(x_test[:16]), 1)

for i in range(x_test[:16].shape[0]):
    count += 1
    figure.add_subplot(maximum_square, maximum_square, count)
    plt.imshow(x_test[:16][i, :, :, :])
    plt.axis('off')
    plt.title("Predicted: " + labels[indices[i]], fontsize=10)

plt.show()

