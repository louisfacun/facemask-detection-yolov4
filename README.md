# Wearing of face mask detection using YOLOv4
[![Python 3.6](https://img.shields.io/badge/Python-3.6-3776AB)](https://www.python.org/downloads/release/python-360/)

`Please note that this repository only contains the specific files used in this research.`
## Requirements for  training and inference (either Windows or Linux):
Read https://github.com/AlexeyAB/darknet#requirements-for-windows-linux-and-macos or:
- **Python 3:** https://www.python.org/downloads/
- **YOLOv4 (darknet):** https://github.com/AlexeyAB/darknet (can be installed with `GPU support` for faster calculations, not required but **recommended**).
- **OpenCV** https://opencv.org/releases/ (can be installed with `GPU support` for faster calculations, not required but **recommended**).
- **CUDA** https://developer.nvidia.com/cuda-zone (if installing the requirements above with `GPU support`).
- **CUDA supported GPUs**:  https://developer.nvidia.com/cuda-gpus (CUDA is only for `NVIDIA GPUs`).
If you have successfully installed the requirements above you can now try [Running model inference](#running-model-inference).


# Running model inference
### Prepare the following files:
`.weights` `.cfg` `obj.data` `obj.names`

### To use our files, download the following:
1. Trained model: [yolov4.weights](https://github.com/lpfacun/FaceMaskDetection_YOLOv4/releases/download/model/yolov4.weights) (244 MB)
2. Config file: [yolov4.cfg](https://github.com/lpfacun/FaceMaskDetection_YOLOv4/releases/download/model/yolov4.cfg)
You can modify this size: higher size=lower inference but more accurate, lower size=faster inference but less accurate
```ini
.
.
width=640
height=640
.
.
```
3. Data file: 
```ini
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

### Inference from different source

- **Inference from a single image:** `python yolov4_image.py --input "sample_images_folder/image1.jpg"` 

- **Inference from a pc webcam:** `python yolov4_webcam.py`

- **Inference  from a video file:** `python yolov4_video_file.py --input "sample_video_folder/video.mp4"` 

- **Inference from an ip camera:** `python yolov4_ip_camera.py --input "rstp://192.168.9.1/"` 


## Tools/libraries
Data preparation:
- **LabelImg:**" `gui annotation` https://github.com/tzutalin/labelImg (labelling and drawing bounding boxes on images)
Data preprocessing:
- **Albumentations:** `augmentation package` https://albumentations.ai/docs/getting_started/installation/ (for running our script)

# Gather and repare your dataset, train and evaluate your own face mask detection model (guide)
## 1. Decide on your classes/labels**
| Label id | Label | Description |
| --- | --- | --- |
| 0 | NWM | Not wearing a mask |
| 1 | WM  | Wearing a mask |
| 2 | IWM | Improperly wearing a mask |

## 2. Data Gathering
**Sources:**
- Gather dataset (images/videos)
- Download images from search engine (Google, Bing etc.).
- Model your own images from friends.
- Gather and capture images (or from videos) from public places.

**Gather atleast 500-1000 instances (not images) per class**
Gather some images -> annotate -> count instances -> Gather some images...

## 3. Data Preprocessing/Preparation
### Image preprocessing
1. Resizing
2. 

### Data augmentation
- To try other augmentations, check https://albumentations-demo.herokuapp.com, modify `apply_image_augmentations.py` based on your options and run `python data_preprocessing_tools/apply_image_augmentations.py --input "sample_images/train/" --option 1`
- To try our augmentations, run default `python data_preprocessing_tools/apply_image_augmentations.py --input "sample_images/train/" --option 1`
```
Option 1: 100% Horizontal Flip
Option 2: 50% Random Rotate, 50% Random Blur, 50% Random Noise
Option 3: 100% Horizontal Flip, 50% Random Rotate, 50% Random Blur, 50% Random Noise
```
## 4. Training a model
s

## 5. Evaluate a model
s
