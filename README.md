# Wearing of Face Mask Detection Using YOLOv4
This repository contains the specific files and YOLOv4 implementation we used in our research paper.

## Prerequisites
- To keep this repository simple we won't include the source code of YOLOv4.
- Install YOLOv4's darknet. See YOLOv4's install guide https://github.com/AlexeyAB/darknet#requirements-for-windows-linux-and-macos
- If darknet (YOLOv4) is successfully installed, start running model inference using our files:
`facemask.weights` `facemask.cfg` `facemask.data` `facemask.names`

## How to use
**The following files are specific in this study:**
1. **[facemask.weights](https://github.com/lpfacun/facemask-detection-yolov4/releases/download/model/facemask.weights)** (244 MB)
2. **facemask.cfg**
https://github.com/LouisFacun/facemask-detection-yolov4/blob/86405f6adbf3f0cd78844b68f4cf215a71cc8258/facemask.cfg#L4-L5

3. **facemask.data**
https://github.com/LouisFacun/facemask-detection-yolov4/blob/a4cd233d80ee2b6c9b4051336f96b2f9157f2d69/facemask.data#L1-L2

4. **facemask.names**
https://github.com/LouisFacun/facemask-detection-yolov4/blob/d8098beae0e1935bfb1da0405eaf7624970d305c/facemask.names#L1-L3

## Files and directory structure
Put `facemask.weights` `facemask.cfg` `facemask.data` `facemask.names` in the same folder of compiled YOLOv4's darknet. 
```
.
.
darknet (created after compiling darknet)
.
.
facemask.weights
facemask.cfg
facemask.data
facemask.names
darknet_image.py
darknet_video.py
```

## Running an inference from different source

- **Single image:** `python darknet_image.py --input "<image location>"` 

- **PC webcam:** `python darknet_video.py`

- **Video file:** `python darknet_video.py --input "<video location>"` 

- **IP camera:** `python darknet_video.py --input "<rstp ip>"`
 

## Tools and libraries we used
- **LabelImg:** https://github.com/tzutalin/labelImg (labelling and drawing bounding boxes on images)
- **Albumentations:** https://albumentations.ai/docs/getting_started/installation/ (applying augmentations)

 ## Model info
 ### Labels
| Label id | Label | Description | Box Color |
| --- | --- | --- | --- |
| 0 | NWM | Not Wearing a Mask | Red |
| 1 | WM  | Wearing a Mask | Green |
| 2 | IWM | Improperly Wearing a Mask | Yellow |

### Dataset stats
| Label | Instances | Min Dimension | Max Dimension |
| --- | --- | --- | --- |
| NWM | 1,006 | 14x17 | 235x265 |
| WM  | 1,012 | 14x15 | 614x605 |
| IWM | 1,007 | 22x53 | 559x577 |

## Results

| Average inference time | mean Average Precision (PASCAL VOC 2012)|
| --- | --- |
| 73 ms | 94% |

*Using GTX 1650 Super (CUDA Enabled Inference Time)

### Confusion matrix

![image](https://user-images.githubusercontent.com/58874676/136065222-68d93f5c-cb35-4e51-b2cb-e9ea9e53bc8e.png)

**None** row in the predictions means, for example, that there is **3** ground-truth of **IWM** that is not predicted.

### Sample detections

![image](https://user-images.githubusercontent.com/58874676/136065117-9915b76b-826f-4ade-8def-1853ef84bd24.png)

![image](https://user-images.githubusercontent.com/58874676/136065261-19a2b070-9023-47ab-9aec-9c82a55c51f4.png)


## Citation
If you use our study as a reference in a scientific publication, we would appreciate citations to the following:

[Object Detection Frameworks fo Real-Time, Scale-Invariant Face Mask Detection](http://www.ijfcc.org/vol11/582-TD08.pdf), Facun *et al.,* IJFCC vol. 11, no. 1, pp. 12-17, 2022.

```
@article{facun_facemask_2022,
    title={Object Detection Frameworks for Real-Time, Scale-Invariant Face Mask Detection},
    author={Facun, Louis Philippe B. and Baculo, Maria Jeseca C. and Libao, Marlon F.
            and Eisma, Ceazar M. and Fredeluces, Christian B. and Garlejo, Rigzor A.
            and Idio, Raymart S.},
    journal={International Journal of Future Computer and Communication},
    volume={11},
    number={1},
    pages={12-17},
    year={2022}
}
```
