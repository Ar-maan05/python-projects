import face_recognition
import os, shutil
import time

# Load the jpg files into numpy arrays
a_image = face_recognition.load_image_file("C:/Users/MAEHR/Dropbox/My PC (LAPTOP-R4NV25O8)/Desktop/python projects/face recognition/a.png")
b_image = face_recognition.load_image_file("C:/Users/MAEHR/Dropbox/My PC (LAPTOP-R4NV25O8)/Desktop/python projects/face recognition/b.png")
c_image = face_recognition.load_image_file("C:/Users/MAEHR/Dropbox/My PC (LAPTOP-R4NV25O8)/Desktop/python projects/face recognition/c.png")
d_image = face_recognition.load_image_file("C:/Users/MAEHR/Dropbox/My PC (LAPTOP-R4NV25O8)/Desktop/python projects/face recognition/d.png")
#check_image = face_recognition.load_image_file("C:/Users/MAEHR/Dropbox/My PC (LAPTOP-R4NV25O8)/Desktop/python projects/face recognition/d.png")

directory = input('Enter the file dir: ')

file = os.listdir(directory)
#print(file)

a = int(len(file))

for i in range(0, a):
    n = file[i]
    check_image = face_recognition.load_image_file(f'{directory}/{n}')

# Get the face encodings for each face in each image file
# Since there could be more than one face in each image, it returns a list of encodings.
# But since I know each image only has one face, I only care about the first encoding in each image, so I grab index 0.
    try:
        a_face_encoding = face_recognition.face_encodings(a_image)[0]
        b_face_encoding = face_recognition.face_encodings(b_image)[0]
        c_face_encoding = face_recognition.face_encodings(c_image)[0]
        d_face_encoding = face_recognition.face_encodings(d_image)[0]
        check_image_encoding = face_recognition.face_encodings(check_image)[0]
    except IndexError:
        print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
        quit()

    known_faces = [
        a_face_encoding,
        b_face_encoding,
        c_face_encoding,
        d_face_encoding
    ]

    # results is an array of True/False telling if the unknown face matched anyone in the known_faces array
    results = face_recognition.compare_faces(known_faces, check_image_encoding)

    if str(results[0]) == 'True':
        source = f'{directory}/{n}'
        destination = "C:/Users/MAEHR/Dropbox/My PC (LAPTOP-R4NV25O8)/Desktop/photos"
        shutil.move(source, destination)
        print(f'{n} Image moved to {destination} succesfully')

    else:
        print('Image not recognised')

time.sleep(60)
exit()
    #print(f"is the image recognised? {results[0]}")
    #print("Is the unknown face a picture of Obama? {}".format(results[1]))
    #print("Is the unknown face a new person that we've never seen before? {}".format(not True in results))