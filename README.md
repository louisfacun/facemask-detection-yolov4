# Wearing of face mask detection using YOLOv4
[![Python 3.6](https://img.shields.io/badge/Python-3.6-3776AB)](https://www.python.org/downloads/release/python-360/)

This repository only contains the specific file used in our undergraduate research. 
yolov4 codes are not included in this repository

include links of:
-yolov4
-darknet
-albumentation
-labelImg

## Data gathering

## Data preprocessing
### Data augmentation
- To try other augmentations, check https://albumentations-demo.herokuapp.com, modify `apply_image_augmentations.py` based on your options and run `python data_preprocessing_tools/apply_image_augmentations.py --input "sample_images/train/" --option 1`
- To try our augmentations, run default `python data_preprocessing_tools/apply_image_augmentations.py --input "sample_images/train/" --option 1`
```
Option 1: 100% Horizontal Flip
Option 2: 50% Random Rotate, 50% Random Blur, 50% Random Noise
Option 3: 100% Horizontal Flip, 50% Random Rotate, 50% Random Blur, 50% Random Noise
```
## Model training

## Model evaluation

# Running model inference
### Prepare the following files:
`.weights` `.cfg` `obj.data` `obj.names`

### To use our files, download the following:
1. Trained model: [yolov4.weights](https://github.com/lpfacun/FaceMaskDetection_YOLOv4/releases/download/model/yolov4.weights) (244 MB)
2. Config file: [yolov4.cfg](https://github.com/lpfacun/FaceMaskDetection_YOLOv4/releases/download/model/yolov4.cfg)
3. Data file: 
```
classes = 3
train = data/train.txt
valid = data/test.txt
names = obj.names #important
backup = backup/
```
4. obj.names
```
NWM
WM
IWM
```
or your own label similar to `classes.txt`

## How to run inference from a single image
