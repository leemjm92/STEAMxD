import cv2
import streamlit as st
import streamlit.components.v1 as components
from deep_list import *
import torch

from PIL import Image,ImageEnhance
import numpy as np
import os

import math
import random

import subprocess
import platform

SCALE_RANGE = (0.3, 0.7)
PICAM1 = "10.21.135.99"
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

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command) == 0

def random_rotation(img):
    angle = [45, 90, -45, -90, 0, 180]
    rotation_rate = random.choice(angle)
    h, w, _ = img.shape
    M = cv2.getRotationMatrix2D((int(w/2), int(h/2)), rotation_rate, 1)
    img_rot = cv2.warpAffine(img, M, (w, h), borderValue=(114, 114, 114))
    return img_rot

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

def mixup_image(img, alpha=0.5):
    new_resize = (256, 256)
    img1 = img
    img1 = img1.resize(new_resize)
    img2 = Image.open("/home/sutd-roar/STEAMxD/data/images/human1.jpg")
    img2 = img2.resize(new_resize)
    img3 = Image.blend(img1, img2, alpha)    
    return img3

def hsv_image(img, hue_rate, saturation_rate, value_rate):
    new_img = np.array(img.convert('RGB'))

    hue, sat, val = cv2.split(cv2.cvtColor(new_img, cv2.COLOR_RGB2HSV))
    dtype = new_img.dtype
    x = np.arange(0, 256, dtype=new_img.dtype)
    lut_hue = ((x * hue_rate) % 180).astype(dtype)
    lut_sat = np.clip(x * saturation_rate, 0, 255).astype(dtype)
    lut_val = np.clip(x * value_rate, 0, 255).astype(dtype)

    im_hsv = cv2.merge((cv2.LUT(hue, lut_hue), cv2.LUT(sat, lut_sat), cv2.LUT(val, lut_val)))
    im_hsv = cv2.cvtColor(im_hsv, cv2.COLOR_HSV2RGB)

    return im_hsv

def rotation_image(img, rotation_rate):
    new_img = np.array(our_image.convert('RGB'))
    w, h = our_image.size
    M = cv2.getRotationMatrix2D((int(w/2), int(h/2)), rotation_rate, 1)
    img_rot = cv2.warpAffine(new_img, M, (w, h), borderValue=(114, 114, 114))
    return img_rot

def translate_image(img, translate_rate):
    new_img = np.array(our_image.convert('RGB'))
    w, h = our_image.size
    # center = (w/2, h/2)
    T = np.eye(3)
    T[0, 2] = translate_rate * w
    T[1, 2] = translate_rate * h
    img_translate = cv2.warpAffine(src=new_img, M=T[:2], dsize=(w, h), borderValue=(114, 114, 114))
    return img_translate

def scale_image(img, scale_rate):
    new_img = np.array(our_image.convert('RGB'))
    w, h = our_image.size
    center = (w/2, h/2)
    scale = 1 + scale_rate
    scale_matrix = cv2.getRotationMatrix2D(angle=0, center=center, scale=scale)
    img_scale = cv2.warpAffine(src=new_img, M=scale_matrix, dsize=(w, h), borderValue=(114, 114, 114))
    return img_scale

def shear_image(img, shear_rate):
    new_img = np.array(our_image.convert('RGB'))
    w, h = our_image.size
    S = np.eye(3)
    S[0, 1] = math.tan(shear_rate * math.pi / 180)  # x shear (deg)
    S[1, 0] = math.tan(shear_rate * math.pi / 180)  # y shear (deg)
    img_shear = cv2.warpAffine(src=new_img, M=S[:2], dsize=(w, h), borderValue=(114, 114, 114))
    return img_shear

def main():
    st.title("STEAMxD")

    activities = ["Augmentation","Detection"]
    choice = st.sidebar.selectbox("Select Activty",activities)

    if choice == "Augmentation":
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
                hue_rate = st.sidebar.slider("Hue",0.0,1.0,0.5)
                saturation_rate = st.sidebar.slider("Saturation",0.0,1.0,0.5)
                value_rate = st.sidebar.slider("Lightness",0.0,1.0,0.8)
                im_hsv = hsv_image(img=our_image, hue_rate=hue_rate, saturation_rate=saturation_rate, value_rate=value_rate)
                st.image(im_hsv)

            elif enhance_type == 'Rotation':
                rotation_rate = st.sidebar.slider("Degrees",0,360,90)
                img_rot = rotation_image(img=our_image, rotation_rate=rotation_rate)
                st.text("Rotated Image")
                st.image(img_rot)

            elif enhance_type == 'Translate':
                translate_rate = st.sidebar.slider("Scale",-1.0,1.0,0.5)
                img_translate = translate_image(img=our_image, translate_rate=translate_rate)
                st.text("Translate Image")
                st.image(img_translate)

            elif enhance_type == 'Scale':
                scale_rate = st.sidebar.slider("Scale",-1.0,1.0,0.5)
                img_scale = scale_image(img=our_image, scale_rate=scale_rate)
                st.text("Scale Image")
                st.image(img_scale)

            elif enhance_type == 'Shear':
                shear_rate = st.sidebar.slider("Degrees",-20,20,5)
                img_shear = shear_image(img=our_image, shear_rate=shear_rate)
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

            elif enhance_type == 'Mixup':
                alpha_rate = st.sidebar.slider("Alpha",0.0,1.0,0.5)
                img_mixup = mixup_image(img=our_image, alpha=alpha_rate)
                st.image(img_mixup)
                        

    if choice == "Detection":
        inference_msg = st.empty()
        st.sidebar.title("Configuration")

        input_source = st.sidebar.radio(
        "Select input source",
        ('HTTP', 'Webcam', 'Local video'))

        conf_thres = st.sidebar.text_input("Class confidence threshold", "0.25")

        conf_thres_drift = st.sidebar.text_input("Class confidence threshold for drift dectection", "0.75")

        fps_drop_warn_thresh = st.sidebar.text_input("FPS drop warning threshold", "8")

        save_output_video = st.sidebar.radio("Save output video?",('Yes', 'No'), index=0)
        if save_output_video == 'Yes':
            nosave = False
            display_labels = False
        else:
            nosave = True
            display_labels = True
        
        save_poor_frame = st.sidebar.radio("Save poor performing frames?",('Yes', 'No'), index=1)
        if save_poor_frame == "Yes":
            save_poor_frame__ = True
        else:
            save_poor_frame__ = False
        
        # ------------------------- LOCAL VIDEO ------------------------------
        if input_source == "Local video":
            video = st.sidebar.file_uploader("Select input video", type=["mp4", "avi"], accept_multiple_files=False)
            
            if st.sidebar.button("Start tracking"):
        
                stframe = st.empty()

                st.subheader("Inference Stats")
                kpi1, kpi2, kpi3 = st.columns(3)

                st.subheader("System Stats")
                js1, js2, js3 = st.columns(3)

                # Updating Inference results
                
                with kpi1:
                    st.markdown("**Frame Rate**")
                    kpi1_text = st.markdown("0")
                    fps_warn = st.empty()
                
                with kpi2:
                    st.markdown("**Detected objects in curret Frame**")
                    kpi2_text = st.markdown("0")
                
                with kpi3:
                    st.markdown("**Total Detected objects**")
                    kpi3_text = st.markdown("0")
                
                # Updating System stats
                
                with js1:
                    st.markdown("**Memory usage**")
                    js1_text = st.markdown("0")

                with js2:
                    st.markdown("**CPU Usage**")
                    js2_text = st.markdown("0")

                with js3:
                    st.markdown("**GPU Memory Usage**")
                    js3_text = st.markdown("0")

                st.subheader("Inference Overview")
                inf_ov_1, inf_ov_2, inf_ov_3, inf_ov_4 = st.columns(4)

                with inf_ov_1:
                    st.markdown("**Poor performing classes (Conf < {0})**".format(conf_thres_drift))
                    inf_ov_1_text = st.markdown("0")
                
                with inf_ov_2:
                    st.markdown("**No. of poor peforming frames**")
                    inf_ov_2_text = st.markdown("0")
                
                with inf_ov_3:
                    st.markdown("**Minimum FPS**")
                    inf_ov_3_text = st.markdown("0")
                
                with inf_ov_4:
                    st.markdown("**Maximum FPS**")
                    inf_ov_4_text = st.markdown("0")

                detect(source=video.name, stframe=stframe, kpi1_text=kpi1_text, kpi2_text=kpi2_text, kpi3_text=kpi3_text,\
                       js1_text=js1_text, js2_text=js2_text, js3_text=js3_text,\
                       # class portion
                       classes=[0,3,6,67]   ,\
                       conf_thres=float(conf_thres), nosave=nosave, display_labels=display_labels,\
                       conf_thres_drift = float(conf_thres_drift), save_poor_frame__= save_poor_frame__,\
                       inf_ov_1_text=inf_ov_1_text, inf_ov_2_text=inf_ov_2_text, inf_ov_3_text=inf_ov_3_text, inf_ov_4_text=inf_ov_4_text,\
                       fps_warn=fps_warn, fps_drop_warn_thresh = float(fps_drop_warn_thresh))

                inference_msg.success("Inference Complete!")

        # -------------------------- WEBCAM ----------------------------------
        if input_source == "Webcam":
            
            if st.sidebar.button("Start tracking"):

                stframe = st.empty()

                st.subheader("Inference Stats")
                kpi1, kpi2, kpi3 = st.columns(3)

                st.subheader("System Stats")
                js1, js2, js3 = st.columns(3)

                # Updating Inference results
                
                with kpi1:
                    st.markdown("**Frame Rate**")
                    kpi1_text = st.markdown("0")
                    fps_warn = st.empty()
                
                with kpi2:
                    st.markdown("**Detected objects in curret Frame**")
                    kpi2_text = st.markdown("0")
                
                with kpi3:
                    st.markdown("**Total Detected objects**")
                    kpi3_text = st.markdown("0")
                
                # Updating System stats
                
                with js1:
                    st.markdown("**Memory usage**")
                    js1_text = st.markdown("0")

                with js2:
                    st.markdown("**CPU Usage**")
                    js2_text = st.markdown("0")

                with js3:
                    st.markdown("**GPU Memory Usage**")
                    js3_text = st.markdown("0")

                st.subheader("Inference Overview")
                inf_ov_1, inf_ov_2, inf_ov_3, inf_ov_4 = st.columns(4)

                with inf_ov_1:
                    st.markdown("**Poor performing classes (Conf < {0})**".format(conf_thres_drift))
                    inf_ov_1_text = st.markdown("0")
                
                with inf_ov_2:
                    st.markdown("**No. of poor peforming frames**")
                    inf_ov_2_text = st.markdown("0")
                
                with inf_ov_3:
                    st.markdown("**Minimum FPS**")
                    inf_ov_3_text = st.markdown("0")
                
                with inf_ov_4:
                    st.markdown("**Maximum FPS**")
                    inf_ov_4_text = st.markdown("0")

                detect(source='0', stframe=stframe, kpi1_text=kpi1_text, kpi2_text=kpi2_text, kpi3_text=kpi3_text,\
                       js1_text=js1_text, js2_text=js2_text, js3_text=js3_text,\
                       # class portion
                       classes=[0,3,6,67],\
                       conf_thres=float(conf_thres), nosave=nosave, display_labels=display_labels,\
                       conf_thres_drift = float(conf_thres_drift), save_poor_frame__= save_poor_frame__,\
                       inf_ov_1_text=inf_ov_1_text, inf_ov_2_text=inf_ov_2_text, inf_ov_3_text=inf_ov_3_text, inf_ov_4_text=inf_ov_4_text,\
                       fps_warn=fps_warn, fps_drop_warn_thresh = float(fps_drop_warn_thresh))
        
        # -------------------------- RTSP ------------------------------
        if input_source == "HTTP":
            
            cam_selection  = st.sidebar.selectbox("Camera Selection", ("picam1", "picam2", "picam3", "picam4", "picam5", "picam6", "picam7", "picam8", "picam9", "picam10"))
            # PICAM_IP list of ip_address
            # get the number of picam and then subtract 1 to get it from he list
            rtsp_input = PICAM_IP[int(cam_selection[-1])-1]
            rtsp_input = f"http://{rtsp_input}:9000/stream.mjpg"
            st.write(rtsp_input)
            if st.sidebar.button("Start tracking"):
        
                stframe = st.empty()

                st.subheader("Inference Stats")
                kpi1, kpi2, kpi3 = st.columns(3)

                st.subheader("System Stats")
                js1, js2, js3 = st.columns(3)

                # Updating Inference results
                
                with kpi1:
                    st.markdown("**Frame Rate**")
                    kpi1_text = st.markdown("0")
                    fps_warn = st.empty()
                
                with kpi2:
                    st.markdown("**Detected objects in curret Frame**")
                    kpi2_text = st.markdown("0")
                
                with kpi3:
                    st.markdown("**Total Detected objects**")
                    kpi3_text = st.markdown("0")
                
                # Updating System stats
                
                with js1:
                    st.markdown("**Memory usage**")
                    js1_text = st.markdown("0")

                with js2:
                    st.markdown("**CPU Usage**")
                    js2_text = st.markdown("0")

                with js3:
                    st.markdown("**GPU Memory Usage**")
                    js3_text = st.markdown("0")

                st.subheader("Inference Overview")
                inf_ov_1, inf_ov_2, inf_ov_3, inf_ov_4 = st.columns(4)

                with inf_ov_1:
                    st.markdown("**Poor performing classes (Conf < {0})**".format(conf_thres_drift))
                    inf_ov_1_text = st.markdown("0")
                
                with inf_ov_2:
                    st.markdown("**No. of poor peforming frames**")
                    inf_ov_2_text = st.markdown("0")
                
                with inf_ov_3:
                    st.markdown("**Minimum FPS**")
                    inf_ov_3_text = st.markdown("0")
                
                with inf_ov_4:
                    st.markdown("**Maximum FPS**")
                    inf_ov_4_text = st.markdown("0")

                detect(source=rtsp_input, stframe=stframe, kpi1_text=kpi1_text, kpi2_text=kpi2_text, kpi3_text=kpi3_text,\
                       js1_text=js1_text, js2_text=js2_text, js3_text=js3_text,\
                       # class portion
                       classes=[0,3,6,67],\
                       conf_thres=float(conf_thres), nosave=nosave, display_labels=display_labels,\
                       conf_thres_drift = float(conf_thres_drift), save_poor_frame__= save_poor_frame__,\
                       inf_ov_1_text=inf_ov_1_text, inf_ov_2_text=inf_ov_2_text, inf_ov_3_text=inf_ov_3_text, inf_ov_4_text=inf_ov_4_text,\
                       fps_warn=fps_warn, fps_drop_warn_thresh = float(fps_drop_warn_thresh))
                               
        # torch.cuda.empty_cache()

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
