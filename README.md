# DigiVision

DigiVision is a deep learning based application which is entitled to help the visually impaired people. This application acts as a virtual eye for the visually-impaired people.The application automatically generates the textual description of what's happening in front of the camera and conveys it to a person through proper audio. 

It is also capable of recognizing faces and it tells user whether a known person is present in front of him or not. If it is not a known face for the user then it gives the user a choice to set it as a known person for all future identification.

![logo](images/Digivision.JPG)

# Requirements
* Tensorflow (>1.9)
* Keras
* OpenCV
* Python 3.5+
* gTTS
* pygame
* pymongo

# Datasets
MS COCO 2017 for Image Processing and Captioning.

Dataset for face Recognition is manually collected.

# Features/Functions

![logo](images/Digivision2.JPG)
![logo](images/Digivision3.JPG)

# Setup and Instructions

1. Install all the required frameworks, libraries and dependecies as mentioned in Requirements above.

2. Download the COCO dataset if not available, in order to train the model
  - [Train images](http://images.cocodataset.org/zips/train2017.zip)
  - [Test images](http://images.cocodataset.org/zips/test2017.zip)
  - [Annotations](http://images.cocodataset.org/annotations/annotations_trainval2017.zip)
 
  Or run:
 ```
 python download.py
 ```

3. Create your own MongoDB Cluster and replace MONGO_URI in line 16 of f_part.py with your own Mongo AccessID.

4. Get the source code on your pc via git and navigate inside the folder through your terminal.

```
  git clone https://github.com/altruistcoder/Digivision
```
5. Run the project using:
  - run.py (for gTTS audio and adding names through Canvas/ python gtk)
  - digivision.py (for Single face detection along with new face addition through python gtk)
  - digivision_mul.py (for Multiface detection along with all Input/Outputs through Audio)

 ```
 python <desired_file_name>.py
 ```
 > It will take around 90 minutes to process all images and approx 5 minutes to process Validation images.
 > Takes around 22 minutes for a single epoch during training on batch size of 256 on NVIDIA GTX 960M.
 > Don't need to re-train data on every single run. Once trained, weights gets loaded automatically.

 # Demo
 [Click here](demo.mp4) for demo of run.py

