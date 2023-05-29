from PIL import Image


def crop_image_by_rectangle(image, rectangle_coordinates):
    coordinates = rectangle_coordinates.top_left + rectangle_coordinates.bottom_right
    return image.crop(coordinates)
