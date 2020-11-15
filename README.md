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

