import cv2
import numpy as np
import matplotlib.pyplot as plt
import json

cap = cv2.VideoCapture('CIMG6630.AVI')

region_mask = 0

frame_level = []

frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)

frame_no = 0

while(1):
    correct, frame = cap.read()
    if(not correct):
        break
    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv=frame
    color_threshold_low = np.array([50,100,0])
    color_threshold_high = np.array([255,255,255])

    mask = cv2.inRange(hsv, color_threshold_low, color_threshold_high)
    color_filtered = cv2.bitwise_and(frame,frame, mask= mask)

    # color_filtered = hsv

    if not region_mask:
        region_mask = cv2.selectROI(frame)

    region_of_interest = color_filtered[int(region_mask[1]):int(region_mask[1]+region_mask[3]), int(region_mask[0]):int(region_mask[0]+region_mask[2])]

    # cv2.imshow('frame',frame)
    # cv2.imshow('color_filtered',color_filtered)
    # cv2.imshow('region_of_interest',region_of_interest)

    avg_color_per_row = np.average(region_of_interest, axis=0)
    avg_color = np.average(avg_color_per_row, axis=0)
    frame_level.append(avg_color[1])
    print("Frame {} of {}, {}".format(frame_no,frame_count,avg_color[1]))
    frame_no+=1
    # k = cv2.waitKey(5) & 0xFF
    # if k == 27:
    #     break

cv2.destroyAllWindows()
cap.release()

with open("frame_color_2.json",'w+') as f: #should be CSV, whatever.
    f.write(json.dumps(frame_level))
