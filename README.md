# under-water-challenge

##Line tracking underwater.py Algorithm

what the task want ? 

"Companies must fly a transect line over the coral reef, displaying the video image of the transect on a
display screen for the station judge. Successfully flying a transect over the coral reef is defined as
starting at one end of the transect and moving to the other end of the transect. Starting at one end of
the transect is defined as the ROV directly above the black length of PVC pipe on either end of the coral
reef."

ok. what our code do ?



Line tracking underwater , used a python library named "Open CV" to detect lines using filter “gaussianblur” and  "mask" function ,then “threshold” function and finally used “HoughLines” function 

ok why we using filter ""guassianblur" ?

to make a filter 2d and reduce noise , then after using "guassianblur" we need to normalize our photo and change the light 

good , what now ?

now we using "mask" function to detect blue color "color of track" 

then use "threshold" function to use "HoughLines" function to draw our lines

and finally we can see the track detected and make our control





-------------------------------------------------------------------


##detect Yolo v3.py Algorithm

i'm using a python library named "ImageAI" and it use "Keras" and "Tensorflow" and use Darknet layers.

YOLOv3 Keras R-CNN
(Region-Based Convolution Neural Network) trained
model to detect objects within the taken screenshot.

100 Epoch.

accuracy 97%.

dataset for training : 2037 photo ,
test : 99 photo ,
valid : 197 photo .

