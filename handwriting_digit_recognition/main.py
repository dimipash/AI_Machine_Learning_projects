import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Input

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train, x_test = x_train / 255.0, x_test / 255.0

x_train_reshaped = x_train.reshape((-1, 28, 28, 1))
x_test_reshaped = x_test.reshape((-1, 28, 28, 1))

model = Sequential([
    Input(shape=(28, 28, 1)),
    Conv2D(32, kernel_size=(3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Conv2D(64, kernel_size=(3, 3), activation='relu'),
    MaxPooling2D(pool_size=(2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')

])

model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy']) 

model.fit(x_train_reshaped, y_train, epochs=5, validation_data=(x_test_reshaped, y_test))

test_loss, test_acc = model.evaluate(x_test_reshaped, y_test)
print(f'\nTest accuracy: {test_acc * 100:.2f}%')

index = 0
test_image = x_test[index].reshape(1, 28, 28, 1)

prediction = np.argmax(model.predict(test_image), axis=-1)
plt.imshow(x_test[index], cmap='gray')
plt.title(f'Predicted Digit: {prediction}')
plt.show()

# model.summary()

# plt.imshow(x_train[0], cmap='gray')
# plt.title(f'Label: {y_train[0]}')
# plt.show()

