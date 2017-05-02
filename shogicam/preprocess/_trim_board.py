import cv2
import numpy as np
from ._detect_corners import detect_corners

def trim_board(raw_img):
    rect, score = detect_corners(raw_img)
    return trim(raw_img, rect), score

BASE_SIZE = 64
def trim(img, corners):
    w = BASE_SIZE * 14
    h = BASE_SIZE * 15
    transform = cv2.getPerspectiveTransform(np.float32(corners), np.float32([[0, 0], [w, 0], [w, h], [0, h]]))
    normed = cv2.warpPerspective(img, transform, (w, h))
    return normed