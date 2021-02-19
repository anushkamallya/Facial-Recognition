
import face_recognition
import cv2
import numpy as np
import os
import glob
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
from collections import defaultdict

#make array of sample pictures with encodings
known_face_encodings = []
known_face_names = []
dirname = os.path.dirname(__file__)
path = os.path.join(dirname, 'known_people/')

#make an array of all the saved jpg files' paths
list_of_files = [f for f in glob.glob(path+'*.jpg')]
#find number of known faces
number_files = len(list_of_files)

names = list_of_files.copy()

def getRDD(i):
    globals()['image_{}'.format(i)] = face_recognition.load_image_file(list_of_files[i])
    globals()['image_encoding_{}'.format(i)] = face_recognition.face_encodings(globals()['image_{}'.format(i)])[0]

    names[i] = names[i].replace("/home/rohit/bdsec/basicFR/known_people/", "")  
    
    return names[i], globals()['image_encoding_{}'.format(i)].tolist()

sc = SparkContext(master="local", appName="SparkDemo")
numberOfFile = (x for x in range(number_files))
print(numberOfFile)
inputrdd = sc.parallelize(numberOfFile)
npRDD = inputrdd.map(getRDD)
print(npRDD.collect())
npRDD.saveAsTextFile('/home/rohit/bdsec/test1/')


