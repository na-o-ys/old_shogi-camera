import cv2
import glob
import numpy as np

def display_cv_image(image, format='.png'):
    decoded_bytes = cv2.imencode(format, image)[1].tobytes()
    display(Image(data=decoded_bytes))

# h * w grayscale
def normalize(img, h, w):
    size = img.shape[:2]
    f = min(1.0 * h / size[0], 1.0 * w / size[1])
    resized = cv2.resize(img, (int(size[1] * f), int(size[0] * f)), interpolation=cv2.INTER_AREA)
    
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blank = np.full((h, w), np.uint8(255), dtype=np.uint8)
    hstart = (h - gray.shape[0]) / 2
    wstart = (w - gray.shape[1]) / 2
    blank[hstart:(hstart + gray.shape[0]), wstart:(wstart + gray.shape[1])] = gray
    return blank

labels = ['gyoku', 'ou', 'kin', 'gin', 'kei', 'kyo', 'kaku', 'hi', 'fu', 'narigin', 'narikei', 'narikyo', 'uma', 'ryu', 'to']
for label in labels:
    files = glob.glob('../images/koma/%s/*' % label)
    imgs = [cv2.imread(f) for f in files]
    imgs = np.array([normalize(img, 48, 48) for img in imgs])
    np.savez_compressed('npz/%s.npz' % label, imgs)
