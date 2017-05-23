# -*- coding:utf-8 -*-
__author__ = 'Microcosm'

import cv2
from feature_matching import FeatureMatching
img_train = cv2.imread('train.png')

matching = FeatureMatching(query_image='query.png')
flag = matching.match(img_train)