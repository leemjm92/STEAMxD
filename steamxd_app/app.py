import streamlit as st
import streamlit.components.v1 as components
import cv2
from PIL import Image,ImageEnhance
import numpy as np
import os

import albumentations as A

import math
import random

import subprocess

import torch
import torchvision.transforms as T
import torchvision.transforms.functional as TF

SCALE_RANGE = (0.3, 0.7)
PICAM1 = "192.168.1.2"
PICAM2 = "192.168.1.23"
PICAM3 = "192.168.1.2"
PICAM4 = "192.168.1.2"
PICAM5 = "192.168.1.2"
PICAM6 = "192.168.1.2"
PICAM7 = "192.168.1.2"
PICAM8 = "192.168.1.2"
PICAM9 = "192.168.1.2"
PICAM10 = "192.168.1.2"
PICAM_IP = [PICAM1, PICAM2, PICAM3, PICAM4, PICAM5, PICAM6, PICAM7, PICAM8, PICAM9, PICAM10]

def ping(picam_ip):
    # Configure subprocess to hide the console window
    info = subprocess.STARTUPINFO()
    info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    info.wShowWindow = subprocess.SW_HIDE

    picam_status = []
    # For each IP address in the subnet, 
    # run the ping command with subprocess.popen interface
    for i in range(len(picam_ip)):
        output = subprocess.Popen(['ping', '-n', '1', '-w', '500', str(picam_ip[i])], stdout=subprocess.PIPE, startupinfo=info).communicate()[0]
        
        if "Destination host unreachable" in output.decode('utf-8'):
            picam_status.append("Offline")
        elif "Request timed out" in output.decode('utf-8'):
            picam_status.append("Offline")
        else:
            picam_status.append("Online")
    return picam_status

def ping_single(picam_ip):
    # Configure subprocess to hide the console window
    info = subprocess.STARTUPINFO()
    info.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    info.wShowWindow = subprocess.SW_HIDE

    # For each IP address in the subnet, 
    # run the ping command with subprocess.popen interface
    output = subprocess.Popen(['ping', '-n', '1', '-w', '500', str(picam_ip)], stdout=subprocess.PIPE, startupinfo=info).communicate()[0]
    
    if "Destination host unreachable" in output.decode('utf-8'):
        return "Offline"
    elif "Request timed out" in output.decode('utf-8'):
        return "Offline"
    else:
        return "Online"

def random_rotation(img):
    angle = [45, 90, -45, -90, 0, 180]
    rotation_rate = random.choice(angle)
    h, w, _ = img.shape
    M = cv2.getRotationMatrix2D((int(w/2), int(h/2)), rotation_rate, 1)
    img_rot = cv2.warpAffine(img, M, (w, h), borderValue=(114, 114, 114))
    return img_rot

def mosaic_image(img, scale_range, filter_scale=0.):
    w, h = img.size
    img = np.array(img.convert('RGB'))
    output_img = np.zeros([h, w, 3], dtype=np.uint8)
    scale_x = scale_range[0] + random.random() * (scale_range[1] - scale_range[0])
    scale_y = scale_range[0] + random.random() * (scale_range[1] - scale_range[0])
    divid_point_x = int(scale_x * w)
    divid_point_y = int(scale_y * h)

    # top-left
    img1 = cv2.resize(img, (divid_point_x, divid_point_y))
    img1 = random_rotation(img1)
    output_img[:divid_point_y, :divid_point_x, :] = img1

    # top-right
    img2 = cv2.resize(img, (w - divid_point_x, divid_point_y))
    img2 = random_rotation(img2)
    output_img[:divid_point_y, divid_point_x:w, :] = img2

    # btm-left
    img3 = cv2.resize(img, (divid_point_x, h - divid_point_y))
    img3 = random_rotation(img3)
    output_img[divid_point_y:h, :divid_point_x, :] = img3

    # btm-right
    img4 = cv2.resize(img, (w - divid_point_x, h - divid_point_y))
    img4 = random_rotation(img4)
    output_img[divid_point_y:h, divid_point_x:w, :] = img4

    return output_img

def detect_faces(our_image):
    new_img = np.array(our_image.convert('RGB'))
    img = cv2.cvtColor(new_img,1)
    gray = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    return img,faces

def detect_eyes(our_image):
    new_img = np.array(our_image.convert('RGB'))
    img = cv2.cvtColor(new_img,1)
    gray = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    return img

def detect_smiles(our_image):
    new_img = np.array(our_image.convert('RGB'))
    img = cv2.cvtColor(new_img,1)
    gray = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
    # Detect Smiles
    smiles = smile_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw rectangle around the Smiles
    for (x, y, w, h) in smiles:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    return img

def cartonize_image(our_image):
    new_img = np.array(our_image.convert('RGB'))
    img = cv2.cvtColor(new_img,1)
    gray = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
    # Edges
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    #Color
    color = cv2.bilateralFilter(img, 9, 300, 300)
    #Cartoon
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    return cartoon

def cannize_image(our_image):
    new_img = np.array(our_image.convert('RGB'))
    img = cv2.cvtColor(new_img,1)
    img = cv2.GaussianBlur(img, (11, 11), 0)
    canny = cv2.Canny(img, 100, 150)
    return canny

def main():
    """STEAMxD"""

    st.title("STEAMxD")

    activities = ["Augmentation","Detection"]
    choice = st.sidebar.selectbox("Select Activty",activities)

    if choice == 'Augmentation':
        st.subheader("Image Augmentation Example")

        image_file = st.file_uploader("Upload Image",type=['jpg','png','jpeg'])
        enhance_type = st.sidebar.radio("Enhance Type",["Original","HSV","Rotation","Translate","Scale","Shear","Flip Up/Down","Flip Left/Right","Mosaic","Mixup"])

        if image_file is not None:
            our_image = Image.open(image_file)
            st.text("Original Image")
            # st.write(type(our_image))
            st.image(our_image)

            if enhance_type == 'Original' and image_file is not None:
                st.image(our_image)

            elif enhance_type == 'HSV':
                hue_rate = st.sidebar.slider("Hue",0.0,1.0,1.0)
                saturation_rate = st.sidebar.slider("Saturation",0.0,1.0,1.0)
                value_rate = st.sidebar.slider("Lightness",0.0,1.0,1.0)
                new_img = np.array(our_image.convert('RGB'))

                hue, sat, val = cv2.split(cv2.cvtColor(new_img, cv2.COLOR_RGB2HSV))
                dtype = new_img.dtype
                x = np.arange(0, 256, dtype=new_img.dtype)
                lut_hue = ((x * hue_rate) % 180).astype(dtype)
                lut_sat = np.clip(x * saturation_rate, 0, 255).astype(dtype)
                lut_val = np.clip(x * value_rate, 0, 255).astype(dtype)

                im_hsv = cv2.merge((cv2.LUT(hue, lut_hue), cv2.LUT(sat, lut_sat), cv2.LUT(val, lut_val)))
                im_hsv = cv2.cvtColor(im_hsv, cv2.COLOR_HSV2RGB)

                st.image(im_hsv)
       
            elif enhance_type == 'Rotation':
                rotation_rate = st.sidebar.slider("Degrees",0,360,90)
                new_img = np.array(our_image.convert('RGB'))
                w, h = our_image.size
                M = cv2.getRotationMatrix2D((int(w/2), int(h/2)), rotation_rate, 1)
                img_rot = cv2.warpAffine(new_img, M, (w, h), borderValue=(114, 114, 114))
                st.text("Rotated Image")
                st.image(img_rot)

            elif enhance_type == 'Translate':
                translate_rate = st.sidebar.slider("Scale",-1.0,1.0,0.5)
                new_img = np.array(our_image.convert('RGB'))
                w, h = our_image.size
                # center = (w/2, h/2)
                T = np.eye(3)
                T[0, 2] = translate_rate * w
                T[1, 2] = translate_rate * h
                img_translate = cv2.warpAffine(src=new_img, M=T[:2], dsize=(w, h), borderValue=(114, 114, 114))
                st.text("Translate Image")
                st.image(img_translate)

            elif enhance_type == 'Scale':
                scale_rate = st.sidebar.slider("Scale",-1.0,1.0,0.5)
                new_img = np.array(our_image.convert('RGB'))
                w, h = our_image.size
                center = (w/2, h/2)
                scale = 1 + scale_rate
                scale_matrix = cv2.getRotationMatrix2D(angle=0, center=center, scale=scale)
                img_scale = cv2.warpAffine(src=new_img, M=scale_matrix, dsize=(w, h), borderValue=(114, 114, 114))
                st.text("Scale Image")
                st.image(img_scale)     

            elif enhance_type == 'Shear':
                shear_rate = st.sidebar.slider("Degrees",-20,20,5)
                new_img = np.array(our_image.convert('RGB'))
                w, h = our_image.size
                S = np.eye(3)
                S[0, 1] = math.tan(shear_rate * math.pi / 180)  # x shear (deg)
                S[1, 0] = math.tan(shear_rate * math.pi / 180)  # y shear (deg)
                img_shear = cv2.warpAffine(src=new_img, M=S[:2], dsize=(w, h), borderValue=(114, 114, 114))
                st.text("Shear Image")
                st.image(img_shear)

            elif enhance_type == 'Flip Up/Down':
                new_img = np.array(our_image.convert('RGB'))
                img_flipud = cv2.flip(new_img, 0)
                st.text("Flip Up/Down Image")
                st.image(img_flipud)

            elif enhance_type == 'Flip Left/Right':
                new_img = np.array(our_image.convert('RGB'))
                img_fliplr = cv2.flip(new_img, 1)
                st.text("Flip Left/Right Image")
                st.image(img_fliplr)

            elif enhance_type == 'Mosaic':
                # new_img = np.array(our_image.convert('RGB'))
                img_mosaic = mosaic_image(img=our_image, scale_range=SCALE_RANGE)
                st.image(img_mosaic)

    elif choice == 'Detection':
        st.subheader("Object Detection")

        video = st.sidebar.file_uploader("Select input video", type=["mp4", "avi"], accept_multiple_files=False)

        st.subheader("Check Picams Status")
        pi1, pi2, pi3, pi4 = st.columns(4)

        if st.button("Check"):
            picam_status = ping(PICAM_IP) 
            with pi1:
                for i in range(5):
                    st.markdown(f"picam{i+1}")
            
            with pi2:
                for i in range(5):
                    st.markdown(f"{picam_status[i]}")

            with pi3:
                for i in range(5):
                    st.markdown(f"picam{i+6}")

            with pi4:
                for i in range(5):
                    st.markdown(f"{picam_status[i+5]}")     

        picam_list = ["picam1", "picam2", "picam3", "picam4", "picam5", "picam6", "picam7", "picam8", "picam9", "picam10"]
        
        st.subheader("Select Picam")
        picam_choice = st.selectbox("", picam_list)

        picam = int(picam_choice[-1])-1
        check_picam = ping_single(PICAM_IP[picam])
        st.text(f"{picam_choice}, url = http://{PICAM_IP[picam]}/index.html, status: {check_picam}")

        if check_picam == 'Online':
            stream_url = "http://"+PICAM_IP[picam]+":9000/stream.mjpg"
            components.iframe(stream_url, width=640, height=480)
            # this portion runs the python file as a subprocess
            # subprocess.call("python detect.py --weights yolov5s.pt", shell=True)
        else:
            st.text(f"Stream is offline please turn on {picam_choice}")
            # subprocess.call("python detect.py --weights yolov5s.pt", shell=True)

        # # Face Detection
        # task = ["Faces","Smiles","Eyes","Cannize","Cartonize"]
        # feature_choice = st.sidebar.selectbox("Find Features",task)
        # if st.button("Process"):

        #     if feature_choice == 'Faces':
        #         result_img,result_faces = detect_faces(our_image)
        #         st.image(result_img)
        #         st.success("Found {} faces".format(len(result_faces)))

        #     elif feature_choice == 'Smiles':
        #         result_img = detect_smiles(our_image)
        #         st.image(result_img)

        #     elif feature_choice == 'Eyes':
        #         result_img = detect_eyes(our_image)
        #         st.image(result_img)

        #     elif feature_choice == 'Cartonize':
        #         result_img = cartonize_image(our_image)
        #         st.image(result_img)

        #     elif feature_choice == 'Cannize':
        #         result_canny = cannize_image(our_image)
        #         st.image(result_canny)

if __name__ == '__main__':
    main()