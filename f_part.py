import warnings
from PIL import Image
import coco
from cache import cache
import cv2 as cv
from gtts import gTTS
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import FaceToolKit as ftk
import DetectionToolKit as dtk
warnings.filterwarnings("ignore")
from pymongo import MongoClient


MONGODB_URI = "mongodb://admin:digivision1@ds247690.mlab.com:47690/digivision"
client = MongoClient(MONGODB_URI)
db = client.get_database("digivision")
digi_db = db.digi_vision


verification_threshhold = 0.65
image_size = 160
v = ftk.Verification()
# Pre-load model for Verification
v.load_model("./models/20180204-160909/")
v.initial_input_output_tensors()

d = dtk.Detection()

def img_to_encoding(img):
    image = plt.imread(img)
    aligned = d.align(image, False)[0]
    return v.img_to_encoding(aligned, image_size)

def distance(emb1, emb2):
    diff = np.subtract(emb1, emb2)
    return np.sum(np.square(diff))


def verify(image_path, identity, database):

    # Compute the encoding for the image. Use img_to_encoding()
    encoding = img_to_encoding(image_path)

    # Compute distance with identity's image
    dist = distance(encoding, database[identity])

    if dist < verification_threshhold:
        print("It's " + str(identity) + ", welcome!")
    else:
        print("It's not " + str(identity) + ", please go away")

    return dist


def who_is_it(image_path):

    # Step 1: Compute the target "encoding" for the image. Use img_to_encoding()
    encoding = img_to_encoding(image_path)

    # Step 2: Find the closest encoding ##

    # Initialize "min_dist" to a large value, say 100
    min_dist = 100
    # Loop over the database dictionary's names and encodings.
    data = digi_db.find()
    for i in data:
        if list(i.keys())[0] != '_id':
            name = list(i.keys())[0]
        else:
            name = list(i.keys())[1]
        db_enc = np.array(i[name])

        # Compute L2 distance between the target "encoding" and the current "emb" from the database. (≈ 1 line)
        dist = distance(encoding, db_enc)

        # If this distance is less than the min_dist, then set min_dist to dist, and identity to name. (≈ 3 lines)
        if min_dist > dist:
            min_dist = dist
            identity = name

    if min_dist > verification_threshhold:
        return min_dist, 'unknown'
    # else:
        # print ("it's " + str(identity) + ", the distance is " + str(min_dist))

    return min_dist, identity
