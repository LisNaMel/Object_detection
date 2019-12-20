from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
from matplotlib import pyplot
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='path to the input image')
ap.add_argument('-o', '--output', required=True, help='path to store augmentation examples')
ap.add_argument('-t', '--total', type=int, default=100, help='# of training samples to generate')
args = vars(ap.parse_args())

#load the input images, convert it to a NumPy array, and then reshape it to have an extra dimension
image = load_img(args['image'])
image = img_to_array(image)
image = np.expand_dims(image, axis=0)

# construct the image generator for data augmentation then
# initialize the total number of images generated thus far
aug = ImageDataGenerator(rotation_range=30,	zoom_range=0.15,width_shift_range=0.2,
                         height_shift_range=0.2, shear_range=0.15, horizontal_flip=True,
                         fill_mode="nearest")
total = 0

#prepare iterator
imageGen = aug.flow(image, batch_size=1, save_to_dir=args['output'], save_prefix='image', save_format='jpg')

#generate image data augmentation generator
for image in imageGen:
    total += 1
    if total == args['total']:
        break
