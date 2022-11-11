import subprocess
import platform
import os
import math
import random
import cv2
from PIL import Image,ImageEnhance

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