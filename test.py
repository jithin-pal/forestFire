from keras.models import load_model
from keras_preprocessing import image
import numpy as np

model = load_model('biomass.hdf5')
test_image = image.load_img('E:/project1/1.jpg', target_size=(32,32))
test_image= image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis=0)
prediction = model.predict(test_image)
print(prediction)
print(prediction.shape)
if(prediction[0] == 1):
    print("not bio")
else:
    print("bio")