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
To try other augmentations, check https://albumentations-demo.herokuapp.com/ and modify `apply_image_augmentations.py` and run `python data_preprocessing_tools/apply_image_augmentations.py --input "sample_images/train/" --option 1`

To try our augmentations, run default `python data_preprocessing_tools/apply_image_augmentations.py --input "sample_images/train/" --option 1`
```
Option 1: 100% Horizontal Flip
Option 2: 50% Random Rotate, 50% Random Blur, 50% Random Noise
Option 3: 100% Horizontal Flip, 50% Random Rotate, 50% Random Blur, 50% Random Noise
```
## Model training

## Model evaluation
