#encoding:utf-8
import numpy as np
from net_model import *
import tensorflow as tf


class Detector:
    def __init__(self):
        self.gender_model = net_model('Alexnet-simple-gender')
        self.age_model = net_model('Alexnet-simple-age')
        self.gender_model.load_weights("models/gender_model.h5")
        self.age_model.load_weights("models/age_model.h5")
        self.graph=tf.get_default_graph()

    def predict(self,image):
        image=np.asarray([np.asarray(image,dtype='float64')/256])
        with self.graph.as_default():
            gender_result = self.gender_model.predict(image)
            age_result = self.age_model.predict(image)
            return gender_result.argmax()+1,age_result.argmax()+1
