#!/usr/bin/env python
# -*- coding:utf-8 -*- 
#Author: RogerNI

import cv2, os
import argparse
import time
import platform

parser = argparse.ArgumentParser()
parser.add_argument("Video", help="the video address")
args = parser.parse_args()

video = cv2.VideoCapture(args.Video)

# Get OS
clear = "cls" if platform.system()=="Windows" else "clear"

# Get FPS Frams
fps = video.get(cv2.CAP_PROP_FPS)
frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
print("FPS: "+str(fps)+" Frames: "+str(frames))

# Get width and height
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
ratio = width/height

def resizeAndGray(img):
    size = os.get_terminal_size()
    win_ratio = size.columns / (2*size.lines)
    resize_ratio = height/size.lines if win_ratio > ratio else 2*width/size.columns
    new_size = (int(width/resize_ratio),int(height/resize_ratio))
    return cv2.cvtColor(cv2.resize(img,new_size),cv2.COLOR_BGR2GRAY)

def prepare(img):
    replace = ' .-+*#@'
    len_replace = len(replace)
    return [[replace[i * len_replace//256]*2 for i in line] for line in img]

def display(img):
    print('\n'.join([''.join(['{:1}'.format(item) for item in row]) for row in img]))

for f in range(int(frames)):
    _,frame = video.read()
    next = prepare(resizeAndGray(frame))
    time.sleep(1/fps)
    os.system(clear)
    display(next)