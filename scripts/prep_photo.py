import sys
import cv2
import numpy as np
from PIL import Image
from rembg import remove

def prep_photo(input_path, output_path='source-prepped.png'):
    print(f'Processing {input_path}...')
    img_pil = Image.open(input_path)
    img_nobg = remove(img_pil)
    
    img_np = np.array(img_nobg)
    if img_np.shape[2] == 4:
        alpha = img_np[:, :, 3] / 255.0
        rgb = img_np[:, :, :3]
        white_bg = np.ones_like(rgb) * 255
        img_composite = (rgb * alpha[:, :, None] + white_bg * (1 - alpha[:, :, None])).astype(np.uint8)
    else:
        img_composite = img_np
        
    gray = cv2.cvtColor(img_composite, cv2.COLOR_RGB2GRAY)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    enhanced = clahe.apply(gray)
    
    cv2.imwrite(output_path, enhanced)
    print(f'Saved prepped image to {output_path}')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python scripts/prep_photo.py <photo.jpg>')
    else:
        prep_photo(sys.argv[1])