from keras.models import load_model
from bottle import route, request, run, template, static_file
from PIL import Image
import os
import numpy as np
from datetime import datetime

model = load_model('ore_model.h5')

def image_to_array(file, src_dir="images", resize=(57, 75)):
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

@route('/')
def index():
    return template('index')

@route('/clf', method='POST')
def clf():
    upload = request.files.get('upload')
    if upload is None:
        return 'File not uploaded.'
    print(upload)
    name, ext = os.path.splitext(upload.filename)
    print(name, ext)
    if ext not in ('.png','.jpg','.jpeg'):
        return 'File extension not allowed.'

    upload.save('images', overwrite=True)

    result = model.predict(image_to_array(upload.filename))
    rate = result[0,1]
    return template('clf', rate=rate, img='images/' + upload.filename)


@route('/images/<filename>')
def images(filename):
    return static_file(filename, root='images')

run(host='0.0.0.0', port=18080)
