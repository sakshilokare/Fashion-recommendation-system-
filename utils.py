import requests
from PIL import Image
from io import BytesIO
import os
import numpy as np
import cv2

def download_sample_images():
    """Download sample fashion images for demo"""
    image_urls = [
        "https://images.unsplash.com/photo-1551232864-3f0890e580d9?w=300&h=400&fit=crop",
        "https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?w=300&h=400&fit=crop",
        "https://images.unsplash.com/photo-1583394838336-acd977736f90?w=300&h=400&fit=crop",
        "https://images.unsplash.com/photo-1567401893414-76b7b1e5a7a5?w=300&h=400&fit=crop",
        "https://images.unsplash.com/photo-1617137968427-85924c800a22?w=300&h=400&fit=crop",
    ]
    
    os.makedirs('fashion_images', exist_ok=True)
    downloaded_images = []
    
    for i, url in enumerate(image_urls):
        try:
            response = requests.get(url, timeout=10)
            img = Image.open(BytesIO(response.content))
            img_path = f'fashion_images/item_{i+1:02d}.jpg'
            img.save(img_path, 'JPEG')
            downloaded_images.append(img_path)
            print(f" Downloaded: {img_path}")
        except Exception as e:
            print(f" Error downloading {url}: {e}")
            placeholder = np.ones((400, 300, 3), dtype=np.uint8) * 50
            img_path = f'fashion_images/item_{i+1:02d}.jpg'
            cv2.imwrite(img_path, placeholder)
            downloaded_images.append(img_path)
    
    return downloaded_images
