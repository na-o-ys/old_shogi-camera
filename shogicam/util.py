import cv2
import numpy as np

def load_img(img_path):
    return cv2.imread(img_path)

def draw_rect(img, rect):
    cntr = np.int32(rect.reshape((4, 2)))
    blank = np.copy(img)
    cv2.drawContours(blank, [cntr], -1, (0,255,0), 2)
    return blank

def save(img, path):
    cv2.imwrite(path, img)
