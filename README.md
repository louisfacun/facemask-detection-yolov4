# Wearing of face mask detection using YOLOv4
[![Python 3.6](https://img.shields.io/badge/Python-3.6-3776AB)](https://www.python.org/downloads/release/python-360/)

`Please note that this repository only contains the specific files used in this research.`
## Requirements for  training and inference (either Windows or Linux):
See YOLOv4's install guide https://github.com/AlexeyAB/darknet#requirements-for-windows-linux-and-macos or:
- **Python 3:** https://www.python.org/downloads/
- **YOLOv4 (darknet):** https://github.com/AlexeyAB/darknet (can be installed with `GPU support` for faster calculations, not required but **recommended**).
- **OpenCV** https://opencv.org/releases/ (can be installed with `GPU support` for faster calculations, not required but **recommended**).
- **CUDA** https://developer.nvidia.com/cuda-zone (if installing the requirements above with `GPU support`).
- **CUDA supported GPUs**:  https://developer.nvidia.com/cuda-gpus (CUDA is only for `NVIDIA GPUs`).

Make sure that the requirements above are successfully installed. You can now try [running model inference](#running-model-inference).

## Model inference
To run YOLOv4 inference, you need these following files:
`facemask.weights` `facemask.cfg` `obj.data` `obj.names`

**Required files for inference:**
1. **[facemask.weights](https://github.com/lpfacun/facemask-detection-yolov4/releases/download/model/facemask.weights)** (244 MB)
2. **facemask.cfg** (check repository)
- higher size = slower inference but more accurate
- lower size = faster inference but less accurate
```ini
.
.
# modify based on your hardware
width=640
height=640 
.
.
```
3. **facemask.data** (check repository)
```ini
classes = 3 # important
train = data/train.txt # not important
valid = data/test.txt # not important
names = facemask.names # important
backup = backup/ # not important
```
4. **facemask.names** (check repository)
```
NWM
WM
IWM
```

## Directory
Put `facemask.weights` `facemask.cfg` `facemask.data` `facemask.names` in the same folder of YOLOv4. 
```
.
.
darknet (created after compiling darknet)
.
.
facemask.weights
facemas.cfg
facemask.data
facemask.names
facemask_image.py
facemask_webcam.py
facemask_video_file.py
facemask_ip_camera.py

```

## Running the inference from different sources

- **Single image:** `python facemask_image.py --input "sample_images_folder/image1.jpg"` 

- **PC webcam:** `python facemask_webcam.py`

- **Video file:** `python facemask_video_file.py --input "sample_video_folder/video.mp4"` 

- **IP camera:** `python facemask_ip_camera.py --input "rstp://192.168.9.1/"`
 
 ## Labels
| Label id | Label | Description |
| --- | --- | --- |
| 0 | NWM | Not Wearing a Mask |
| 1 | WM  | Wearing a Mask |
| 2 | IWM | Improperly Waring a Mask |

## Tools and libraries used
- **LabelImg:** https://github.com/tzutalin/labelImg (labelling and drawing bounding boxes on images)
- **Albumentations:** https://albumentations.ai/docs/getting_started/installation/ (applying augmentations)

## Deployment
Soon..
