#!/usr/bin/env python3

import json
from os.path import join, dirname
from watson_developer_cloud import VisualRecognitionV3

visual_recognition = VisualRecognitionV3('2016-05-20', api_key='5b6484bea44dd2318e19fd9a8763c42716a122d4')

face_path = join(dirname(__file__), 'testPhotoParv.jpg')
with open(face_path, 'rb') as image_file:
    face_result = visual_recognition.detect_faces(images_file=image_file)
    print(json.dumps(face_result, indent=2))