import cv2
import glob
import numpy as np
from pathlib import Path

# h * w / gray
def normalize(img, h, w):
    size = img.shape[:2]
    f = min(h / size[0], w / size[1])
    resized = cv2.resize(img, (int(size[1] * f), int(size[0] * f)), interpolation=cv2.INTER_AREA)
    
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blank = np.full((h, w), np.uint8(255), dtype=np.uint8)
    hstart = (h - gray.shape[0]) / 2
    wstart = (w - gray.shape[1]) / 2
    blank[hstart:(hstart + gray.shape[0]), wstart:(wstart + gray.shape[1])] = gray
    return blank

labels = ['gyoku', 'ou', 'kin', 'gin', 'kei', 'kyo', 'kaku', 'hi', 'fu', 'narigin', 'narikei', 'narikyo', 'uma', 'ryu', 'to']

src = Path(__file__).parent / '../images/koma/series'
dst = Path(__file__).parent
for i, directory in enumerate(src.resolve().glob('*')):
    found = []
    imgs = []
    if not directory.is_dir():
        continue
    for label in labels:
        path = "%s/%s.png" % (directory, label)
        if Path(path).is_file():
            img = cv2.imread(path)
            img = normalize(img, 64, 64)
            imgs.append(img)
            found.append(label)
    np.savez_compressed('{0}/{1:02d}.npz'.format(str(dst.resolve()), i), labels=found, imgs=imgs)
