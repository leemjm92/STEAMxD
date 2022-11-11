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