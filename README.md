# Wearing of Face Mask Detection Using YOLOv4
**Requirements**

See YOLOv4's install guide https://github.com/AlexeyAB/darknet#requirements-for-windows-linux-and-macos

If darknet (YOLOv4) is successfully installed, start running model inference using our files:
`facemask.weights` `facemask.cfg` `facemask.data` `facemask.names`

## Running face mask detection
**Download the the following files for face mask detection:**
1. **[facemask.weights](https://github.com/lpfacun/facemask-detection-yolov4/releases/download/model/facemask.weights)** (244 MB)
2. **facemask.cfg** (check repository)
```ini
.
.
# facemask.weights trained on 640x640
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

## Files / directory structure
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

## Running an inference from different source

- **Single image:** `python facemask_image.py --input "sample_images_folder/image1.jpg"` 

- **PC webcam:** `python facemask_webcam.py`

- **Video file:** `python facemask_video_file.py --input "sample_video_folder/video.mp4"` 

- **IP camera:** `python facemask_ip_camera.py --input "rstp://192.168.9.1/"`
 

## Tools and libraries used
- **LabelImg:** https://github.com/tzutalin/labelImg (labelling and drawing bounding boxes on images)
- **Albumentations:** https://albumentations.ai/docs/getting_started/installation/ (applying augmentations)

 # Model info
 ## Labels
| Label id | Label | Description | Box Color |
| --- | --- | --- | --- |
| 0 | NWM | Not Wearing a Mask | Red |
| 1 | WM  | Wearing a Mask | Green |
| 2 | IWM | Improperly Wearing a Mask | Yellow |

## Dataset
| Label | Instances | Min Dimension | Max Dimension |
| --- | --- | --- | --- |
| NWM | 1,006 | 14x17 | 235x265 |
| WM  | 1,012 | 14x15 | 614x605 |
| IWM | 1,007 | 22x53 | 559x577 |

## Results

| Average inference time | mean Average Precision |
| --- | --- |
| 73ms | 94% |
Using GTX 1650 Super (CUDA Enabled Inference Time)

**Confusion matrix:**

![image](https://user-images.githubusercontent.com/58874676/136065222-68d93f5c-cb35-4e51-b2cb-e9ea9e53bc8e.png)
*None* row in the predictions means, for example, that there is 3 ground-truth of IWM that is not predicted.

**Sample detections:**

![image](https://user-images.githubusercontent.com/58874676/136065117-9915b76b-826f-4ade-8def-1853ef84bd24.png)

![image](https://user-images.githubusercontent.com/58874676/136065261-19a2b070-9023-47ab-9aec-9c82a55c51f4.png)

