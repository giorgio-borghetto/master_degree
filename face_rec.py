import face_recognition
import os
import numpy as np
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

#Provide the face images of the known subjects, i.e. the swap subjects and the RADVESS' actor.
known_giorgio_image = face_recognition.load_image_file("giorgio.png")
known_giulia_image = face_recognition.load_image_file("giulia.png")
known_actor_image = face_recognition.load_image_file("actor.png")

giorgio_face_encoding = face_recognition.face_encodings(known_giorgio_image)[0]
giulia_face_encoding = face_recognition.face_encodings(known_giulia_image)[0]
actor_face_encoding = face_recognition.face_encodings(known_actor_image)[0]

known_encodings = [
    giorgio_face_encoding,
    giulia_face_encoding,
    actor_face_encoding,
]
#Cumulative distances for the swap subjects and the RADVESS' actor.
face_dst_actor=np.array([])
face_dst_giorgio=np.array([])
face_dst_giulia=np.array([])

#Directory with the frames extractd by extract_frames.py.
path = '/Tests'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        files.append(os.path.join(r, file))

for i, f in enumerate(files):
    print(f)
    image_to_test = face_recognition.load_image_file(f)
    image_to_test_encoding = face_recognition.face_encodings(image_to_test)[0]

    print '\n\nFACE DISTANCE SWAP #', i + 1
    # See how far apart the test image is from the known faces using the Euclidean distance. Threshold set at 0.6 between recognized/not recognized face.
    face_distances = face_recognition.face_distance(known_encodings, image_to_test_encoding)

    for j, face_distance in enumerate(face_distances):
        print("The test image has a distance of {:.2} from known image #{}".format(face_distance, j))
        if j == 0:
            face_dst_giorgio = np.append(face_dst_giorgio, face_distance)
        else:
            if j==1:
                face_dst_giulia = np.append(face_dst_giulia, face_distance)
            else:
                face_dst_actor = np.append(face_dst_actor, face_distance)

print '\nDst from giorgio: ', np.mean(face_dst_giorgio), 'StdDev: ', np.std(face_dst_giorgio)
print 'Dst from giulia: ', np.mean(face_dst_giulia), 'StdDev: ', np.std(face_dst_giulia)
print 'Dst from actor: ', np.mean(face_dst_actor), 'StdDev: ', np.std(face_dst_actor)


