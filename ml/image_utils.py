from PIL import Image
import os
import numpy as np

def convert(src_dir, dest_dir, showProgress=True):
    os.makedirs(dest_dir, exist_ok=True)
    for f in os.listdir(src_dir):
        if f.startswith(".") == False :
            img = Image.open(src_dir + "/" + f)
            img = img.convert('L') # Gray
            # img = img.convert('1') # W/B
            img.save(dest_dir + "/" + f)
            if showProgress: print(f)
    pass


def resize(src_dir, dest_dir, resize=(57, 75), showProgress=True):
    os.makedirs(dest_dir, exist_ok=True)
    for f in os.listdir(src_dir):
        if f.startswith(".") == False :
            img = Image.open(src_dir + "/" + f)
            img = img.resize(resize)
            img.save(dest_dir + "/" + f)
            if showProgress: print(f)
    pass

def to_array(dir, label):
    train_data = []
    train_label = []
    for f in os.listdir(dir):
        if f.startswith(".") == False :
            img = Image.open(dir + "/" + f)
            row = []
            for i in range(img.width):
                for j in range(img.height):
                    row.append(img.getpixel((i, j)))
            train_data.append(row)
            train_label.append(label)
    return (train_data, train_label)

def image_to_array(file, src_dir="keras_sample_images", resize=(57, 75)):
    img = Image.open(src_dir + "/" + file)
    img = img.convert('L') # Gray
    img = img.resize(resize)
    row = []
    img_data = []
    for i in range(img.width):
        for j in range(img.height):
            row.append(img.getpixel((i, j)))
    img_data.append(row)

    img_data = np.array(img_data)

    img_data = img_data.astype('float32')
    img_data /= 255
    img_data = img_data.reshape(1, 75, 57, 1)
    return img_data


# convert("keras_or_images", "keras_or_images_g", showProgress=False)
# resize("keras_or_images_g", "keras_or_images_gr", showProgress=False)

# convert("keras_ng_images", "keras_ng_images_g", showProgress=False)
# resize("keras_ng_images_g", "keras_ng_images_gr", showProgress=False)
