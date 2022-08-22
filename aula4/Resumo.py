# Resumindo:

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

img = Image.open('imagem.extensao')
plt.imshow(img)
img_np = np.array(img)
img_pil = Image.fromarray(img_np)
img.save('imagem.extensao')
