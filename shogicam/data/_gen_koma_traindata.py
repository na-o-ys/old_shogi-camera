import cv2
import glob
import numpy as np
from pathlib import Path
from shogicam.constant import *

# h * w / gray
def normalize(img, h, w):
    size = img.shape[:2]
    f = min(h / size[0], w / size[1])
    resized = cv2.resize(img, (int(size[1] * f), int(size[0] * f)), interpolation=cv2.INTER_AREA)
    
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blank = np.full((h, w), np.uint8(255), dtype=np.uint8)
    hstart = int((h - gray.shape[0]) / 2)
    wstart = int((w - gray.shape[1]) / 2)
    blank[hstart:(hstart + gray.shape[0]), wstart:(wstart + gray.shape[1])] = gray
    return blank

def gen_koma_traindata(img_dir, outdata_dir):
    saved_files = []
    for directory in sorted(glob.glob(img_dir + '/*')):
        found = []
        imgs = []
        if not Path(directory).is_dir():
            continue
        for label in LABELS:
            path = "%s/%s.png" % (directory, label)
            if Path(path).is_file():
                img = cv2.imread(path)
                img = normalize(img, IMG_ROWS, IMG_COLS)
                imgs.append(img)
                found.append(label)
        if not imgs:
            continue
        file_path = '{0}/{1}.npz'.format(outdata_dir, Path(directory).stem)
        saved_files.append(file_path)
        np.savez_compressed(file_path, labels=found, imgs=imgs)
    return saved_files

def gen_empty_cell_traindata(img_dir, outdata_path):
    imgs = []
    saved_files = []
    for path in sorted(glob.glob(img_dir + '/*.png')):
        img = cv2.imread(path)
        img = normalize(img, IMG_ROWS, IMG_COLS)
        imgs.append(img)
        saved_files.append(path)
    np.savez_compressed(outdata_path, imgs=imgs)
    return saved_files
