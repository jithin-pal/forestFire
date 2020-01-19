from keras.layers import Dense, Flatten , Convolution2D, MaxPooling2D
from keras import Sequential
from keras_preprocessing.image import ImageDataGenerator
import  tensorflow as tf

classifier = Sequential()
classifier.add(Convolution2D(32,3,3, input_shape=(32,32,3),activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2,2)))
classifier.add(Flatten())
classifier.add(Dense(64,activation='relu'))
classifier.add(Dense(1,activation='sigmoid'))
classifier.compile(optimizer='adam',metrics=['accuracy'],loss='binary_crossentropy')
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

train_set = train_datagen.flow_from_directory(
        'E:/project1/biomass_detection/train',
        target_size=(32,32),
        batch_size=25,
        class_mode='binary')

test_set = test_datagen.flow_from_directory(
        'E:/project1/biomass_detection/test',
        target_size=(32, 32),
        batch_size=25,
        class_mode='binary')

classifier.fit_generator(
        train_set,
        steps_per_epoch=100,
        epochs=3,
        validation_data=test_set,
        validation_steps=100)

classifier.save('biomass.hdf5')
classifier.save_weights('biomassweights.h5')
converter = tf.lite.TFLiteConverter.from_keras_model(classifier)
tflite_model = converter.convert()
print(train_set.class_indices)