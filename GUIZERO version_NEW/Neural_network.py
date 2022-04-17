import tensorflow as tf
from tensorflow.keras import datasets, layers, models

import matplotlib.pyplot as plt
import pathlib

data_dir = "C:\Users/tomrg\OneDrive\Desktop\Year-14-Comp-Project\GUIZERO version_NEW/train"
val_dir = "C:\Users/tomrg\OneDrive\Desktop\Year-14-Comp-Project\GUIZERO version_NEW/val"
batch_size = 32

train_ds = tf.keras.utils.image_dataset_from_directory(
    data_dir,
    seed=123,
    batch_size=batch_size
)
val_ds = tf.keras.utils.image_dataset_from_directory(
    val_dir,
    seed=123,
    batch_size=batch_size
)

t_class_names = train_ds.class_names
print(t_class_names)
v_class_names = val_ds.class_names
print(v_class_names)

# following code plots the images into a grid for easy viewing
# plt.figure(figsize=(10, 10))
# for images, labels in train_ds.take(1):
#   for i in range (9):
#      ax = plt.subplot(3, 3, i+1)
#     plt.imshow(images[i].numpy().astype("uint8"))
#    plt.title(t_class_names[labels[i]])
#   plt.axis("off")


#plt.show()
# shrinks the rgb colour range to between 0 and 1 (this is easier for the neural network to process)
# normilisation_layer= tf.keras.layers.Rescaling(1./255)
# norm_t_ds = train_ds.map(lambda x, y:(normilisation_layer, y))
# image_batch, labels_batch = next(iter(norm_t_ds))
# first_image = image_batch[0]
# Pixel values now between 1 and 0
# print(np.min(first_image), np.max(first_image))

model = models.Sequential(tf.keras.layers.Rescaling(1. / 255))
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))  # 32 3x3 filters applied over image
model.add(layers.MaxPooling2D((2, 2)))  # max pooling layer using 2x2 samples and a stride of 2
model.add(layers.Conv2D(64, (3, 3),
                        activation='relu'))  # increases the amount of filters as sample gets smaller to increase (computational) depth
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(2))
#model.summary()

# now compile the model with the recommended hyperparamaters bt tensorflow
model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])
model.fit(train_ds, validation_data=val_ds, epochs=10)

# Evaluate the model to see accuracy
test_loss, test_acc = model.evaluate(train_ds, verbose=2)
print(test_acc)