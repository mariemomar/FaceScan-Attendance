import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

classNames = [] # to append the names of the images in it
images = []

path = 'Faces'
my_list = os.listdir(path)
# print(my_list)

for i in my_list :
    current_img = cv2.imread(f'{path}/{i}')
    images.append(current_img)
    classNames.append(os.path.splitext(i)[0]) # to take the name of the photo without the extension (.png)

# make a function that encodes the images
def findEncodings(images):
    encodingList = []
    for img in images :
        img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodingList.append(encode)
    return encodingList

encodeKnownImages = findEncodings(images)
print(len(encodeKnownImages))

marked_names = set()

def markAttendence(name):
    with open('Attendence.csv' , 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList :
            entry = line.split(',')
            nameList.append(entry[0])

        if name not in nameList :
            now = datetime.now()
            dateString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name} , {dateString}')

# find the matches


cap = cv2.VideoCapture(0) # access the default camera


while True :
    ret , frame = cap.read()
    # frame = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
    locationFaceinFrame = face_recognition.face_locations(frame)
    encodeFaceinFrame = face_recognition.face_encodings(frame)
    print(locationFaceinFrame)

    for encode , (top, right, bottom, left) in zip(encodeFaceinFrame , locationFaceinFrame) : # check the faces in the frame one by one and we are using zip because we want them in the same loop
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        matches = face_recognition.compare_faces(encodeKnownImages , encode)
        faceDistance = face_recognition.face_distance(encodeKnownImages , encode)
        print(faceDistance)

        matchIndex = np.argmin(faceDistance)
        if matches[matchIndex] :
            name = classNames[matchIndex]
            cv2.putText(
                frame , name , (left , top -10) , cv2.FONT_HERSHEY_SIMPLEX , 0.9 , (0 , 255 , 0) , 2
            )
            if not name in marked_names :
                marked_names.add(name)
                markAttendence(name)




    if not ret :
        break

    if cv2.waitKey(30) & 0xFF  == ord('q'):
        break

    cv2.imshow("frame" , frame)

cap.release()
cv2.destroyAllWindows()