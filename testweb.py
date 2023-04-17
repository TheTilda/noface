import cv2
from simple_facerec import SimpleFacerec




# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

# Load Camera
cap = cv2.VideoCapture('http://192.168.202.6:4747/video')


while True:
    try:
        ret, frame = cap.read()

        # Detect Faces
        face_locations, face_names = sfr.detect_known_faces(frame)
        if face_names is None:
            pass
        else:
            #requests.get(f'http://localhost:8000/set/1/1')
            pass
        print(face_names)
        for face_loc, name in zip(face_locations, face_names):
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

            cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 200), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1)
        if key == 'q':
            break
    except Exception as e:
        print(e)

cap.release()
cv2.destroyAllWindows()
