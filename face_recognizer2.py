import face_recognition
import cv2
import numpy as np
import os
import imutils
from tkinter import *
from PIL import Image
from PIL import ImageTk
from imutils.video import VideoStream
import time
cont=0
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#cap=VideoStream(src=0, resolution=(1920, 1280), framerate=30).start()
time.sleep(2.0)
path = "imagenes"
image = os.listdir(path)
known_face_encodings = []
known_face_names = []
process_this_frame=True
# Initialize some variables
face_locations = []
face_encodings = []
face_names = []

for a in image:
    if a != ".DS_Store":
        name_image = face_recognition.load_image_file(str(path) + "/" + str(a))
        name_face_encoding = face_recognition.face_encodings(name_image)
        if len(name_face_encoding) > 0:
            known_face_names.append(a.strip('.jpg'))
            name_face_encoding = name_face_encoding[0]
            known_face_encodings.append(name_face_encoding)
        else:
            print("¡No se detectó un área de cara válida!")
def bounding_box(frame,face_locations, face_names):
  
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left+15, top-70), (right, bottom), (55, 55, 255), 1)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 45), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = 4
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    #cv2.imshow('Video', frame)

def deteccion_facial(frame):

    global process_this_frame
    # Only process every other frame of video to save time
    if process_this_frame:
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Find all the faces and face encodings in the current frame of video
        global face_locations
        global face_names
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame
    # Display the results
    bounding_box(frame,face_locations, face_names)

    return frame
        
def visualizar():
    global cap
    
    #btnFinalizar.configure(state="active")
   
    ret, frame = cap.read()
    if ret == True:
            frame = imutils.resize(frame, width=740)
            frame = deteccion_facial(frame)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)
            lblVideo.configure(image=img)
            lblVideo.image = img
            lblVideo.after(1, visualizar)          
            # Display the resulting image
            #cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!

def finalizar():
    global cap
    cap.release()
    cv2.destroyAllWindows()

def iniciar():
    global cap
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    visualizar()

cap = None
root = Tk()
lblVideo = Label(root)
lblVideo.grid(column=0, row=2, columnspan=2)
btnIniciar = Button(root, text="Iniciar", width=45, command=iniciar)
btnIniciar.grid(column=0, row=0, padx=5, pady=5)
btnFinalizar = Button(root, text="Finalizar", width=45, command=finalizar)
btnFinalizar.grid(column=1, row=0, padx=5, pady=5)

root.mainloop()
# Release handle to the webcam
cap.release()
cv2.destroyAllWindows()