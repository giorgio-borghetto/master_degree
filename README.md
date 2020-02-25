This project refers to de-identification methods for visual privacy protection and focuses on provide a qualitative
and quantitative measurement of the degree of privacy applied by a face swap tool, considering how well the tool conceals
the identity of the original subject and retains useful facial information.
In this README we refer to the subject of the
target video as Original subject and the subject intended to be replaced over him/her as Swap subject.

_ extract_frames:
This script extracts a given number of frames from a given video. It accepts command line interface parameters, as the input
video path, the desired number of extracted frames from it and the path where to save them.

_ face_rec.py:
This script will compare each unknown faces (i.e. the swapped ones from the swapped video) against each known faces, employing
the Euiclidian distance measure. The threshold is set to 0.6, wich discriminates between matching/non matching subjects.
The script takes in input a directory composed by the face images of the known subjects (i.e. the Original subject and the
Swap subject) and a directory composed by the frames extracted with the previous script from the swapped video.

_ att_preservation.py:
This script will compare each .csv file with the registered Action Units intensities from the swapped videos, against the .csv
obtained by the Original vido. It takes in input the .csv files and outputs the respective comparison employing the Pearson
Correlation Coefficient and Root Mean Square Error.
