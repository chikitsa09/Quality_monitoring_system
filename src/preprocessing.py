import numpy as np

def normalize_image(image):
    image=image.astype(np.float32)
    min_value=np.nanmin(image)
    max_value=np.nanmax(image)
    if max_value == min_value:
        return np.zeros_like(image,dtype=np.uint8)
    normalized=(
        (image-min_value)/(max_value-min_value)*255
    )
    normalized=np.clip(normalized,0,255)
    return normalized.astype(np.uint8)
