from image_utils import convert, resize

convert("keras_or_images", "keras_or_images_g", showProgress=False)
resize("keras_or_images_g", "keras_or_images_gr", showProgress=False)

convert("keras_ng_images", "keras_ng_images_g", showProgress=False)
resize("keras_ng_images_g", "keras_ng_images_gr", showProgress=False)
