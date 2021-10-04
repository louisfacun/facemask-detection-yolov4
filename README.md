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

**To use our files, you can download them in the following:**
1. **facemask.weights**: [Download](https://github.com/lpfacun/FaceMaskDetection_YOLOv4/releases/download/model/yolov4.weights) (244 MB)
2. **facemask.cfg**: [Download](https://github.com/lpfacun/FaceMaskDetection_YOLOv4/releases/download/model/yolov4.cfg) (12 KB)
You can modify this size: higher size=lower inference but more accurate, lower size=faster inference but less accurate
```ini
.
.
width=640
height=640
.
.
```
3. **obj.data** [Download](https://github.com/lpfacun/FaceMaskDetection_YOLOv4/releases/download/model/yolov4.cfg) (12 KB)
```ini
classes = 3 # important
train = data/train.txt # not important
valid = data/test.txt # not important
names = obj.names # important
backup = backup/ # not important
```
4. **obj.names** [Download](https://github.com/lpfacun/FaceMaskDetection_YOLOv4/releases/download/model/yolov4.cfg) (12 KB)
```
NWM
WM
IWM
```

## Running the inference from different sources

- **Single image:** `pythonfacemask_image.py --input "sample_images_folder/image1.jpg"` 

- **PC webcam:** `python facemask_webcam.py`

- **Video file:** `python facemask_video_file.py --input "sample_video_folder/video.mp4"` 

- **IP camera:** `python facemask_ip_camera.py --input "rstp://192.168.9.1/"`
 
 ## Labels
| Label id | Label | Description |
| --- | --- | --- |
| 0 | NWM | Not Wearing a Mask |
| 1 | WM  | Wearing a Mask |
| 2 | IWM | Improperly Waring a Mask |

## Tools/libraries used
- **LabelImg:** `gui annotation` https://github.com/tzutalin/labelImg (labelling and drawing bounding boxes on images)
- **Albumentations:** `augmentation package` https://albumentations.ai/docs/getting_started/installation/ (for running our script)
