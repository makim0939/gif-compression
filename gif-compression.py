from skvideo.io import vread
import cv2
from PIL import Image
from skvideo.io import vread

FLAME_DROP = 5
SIZE_REDUCE = 4

gif = vread("src.gif")
width, height = gif.shape[2] // SIZE_REDUCE, gif.shape[1] // SIZE_REDUCE
imgs = []
i = 0
for img in gif:
    if i % 5 != 0:
        i += 1
        continue
    print("#", i)
    new_img = cv2.resize(img, (width, height))
    imgs.append(Image.fromarray(new_img))
    i += 1


imgs[0].save(
    "dst.gif",
    save_all=True,
    append_images=imgs[1:],
    optimize=True,
    duration=50 * (FLAME_DROP - 1),
    loop=0,
)
