from PIL import Image


def enlarge_image(image, percent):
    width, height = image.size

    delta_height = int(height * percent / 100)
    delta_width = int(width * percent / 100)

    new_size = (width + delta_width, height + delta_height)
    resized_image = image.resize(new_size)

    return resized_image


def crop_image_by_rectangle(image, rectangle_coordinates):
    coordinates = rectangle_coordinates.top_left + rectangle_coordinates.bottom_right
    return image.crop(coordinates)
