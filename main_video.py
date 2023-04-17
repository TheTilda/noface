import cv2
from simple_facerec import SimpleFacerec
import seial as serial



# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

# Load Camera
cap = cv2.VideoCapture(0)

face = []
last_face = []
while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    if face_names is None : #or len(face_names) == 0
        pass
    else:
        
        if len(face_names) != 0 and 'Unknown' not in face_names:
            print('0' + str(face_names))
            serial.open()
        elif 'Unknown' in face_names and last_face != face_names:
            print('1' + str(face_names))
            serial.close()
        elif len(face_names) == 0 and last_face != face_names:
            print('2' + str(face_names))
            serial.close()
        last_face = face_names
        print(face_names)
        # if face_names in face:
        #     pass
        # else:
        #     serial.open()
        #     face.append(face_names)
        
    #print(face_names)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 'q':
        break

cap.release()
cv2.destroyAllWindows()
