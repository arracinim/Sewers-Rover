# EPM CCTV Sewers Faillure Detection

**About the Project**

App for detection of failuresin sewer systems of the city of Medellin - Colombia. 
Model implemented with YOLO v3. App created with Dash

**IMPORTANT**

- You must download the data from this link: https://drive.google.com/u/1/uc?export=download&confirm=RvgA&id=10777tL9PnvYKCxK78tSM_xSB_gsUXN-1
- Then copy both folders in the project folder (This folder contains all the data requiered for YOLO V3 model)


Thanks for being intersted in this project. Special greetings to EPM, Correlation One and Mintic for this oportunity.

## Notebook in **COLAB**
To use the `YOLOv3_YOLOv4_colab_training_TL.ipynb` notebook, the user must change the runtime to GPU in *COLAB* and upload the following repository https://drive.google.com/drive/folders/1ege1-3IYXj_xiVQ3IBQEBsbxsYj66ERi?usp=sharing in your personal DRIVER. If you want to increase the number of images in the Transfer Learning process, you must proceed to label them in PASCAL VOC format in the label application that the user sees fit. In addition, if it is required to increase the training periods or the learning rate; As well as, to activate the Transfer Learning and Data Augmentation process, one must resort to the `./yolov3/configs.py` file in the repository in DRIVE and change these parameters.<br>

-- **Note:** In the repository you can see two (2) videos in Spanish of the step by step to follow in *COLAB*.

## TensorFlow-2.x-YOLOv3 and YOLOv4 tutorials
YOLOv3 and YOLOv4 implementation in TensorFlow 2.x, with support for training, transfer training, object tracking mAP and so on... Code was tested with following specs:

* i7-7700k CPU and Nvidia 1080TI GPU
* OS Ubuntu 18.04
* CUDA 10.1
* cuDNN v7.6.5
* TensorRT-6.0.1.5
* Tensorflow-GPU 2.3.1
* Code was tested on Ubuntu and Windows 10 (TensorRT not supported officially)

### Installation
First, download this https://drive.google.com/drive/folders/1ege1-3IYXj_xiVQ3IBQEBsbxsYj66ERi?usp=sharing repository. Install requirements and download pretrained weights:
```
pip install -r ./requirements.txt

# yolov3
wget -P model_data https://pjreddie.com/media/files/yolov3.weights

# yolov4
wget -P model_data https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights

```

### Quick start
Start with using pretrained weights to test predictions on both image and video:
```
python detection_demo.py
```

### Quick training for custom dataset (Sewer's Anomalies) 
`./custom_dataset/` folder contains anomalies images, create training and test data.<br>

**Note:** In the original exercise the data had approximately 8000 tagged images.

### Transfer Learning
* Convert pascal voc format images to YOLO
```
python tools/XML_to_YOLOv3.py
```
*For this case, three (3) labels were used: HOLES, ROOTS and DEPOSITS. The above, due to the fact that according to the descriptive results they are the most frequent and have a high impact on sanitation problems.*

* Training
Before starting the training process, change the Transfer Learning and Data Augmetation parameters to True in the `./yolov3/configs.py` file.

https://github.com/arracinim/Sewers-Rover/Train_Options.png



Now, you can train it and then evaluate your model

python train.py
tensorboard --logdir=log
Track training progress in Tensorboard and go to http://localhost:6006/:



Test detection with detect_mnist.py script:

python detect_mnist.py
