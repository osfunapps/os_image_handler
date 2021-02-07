from PIL import Image, ImageDraw
from PIL import ImageFont
from os_tools import tools


def load_img(img_path):
    """Will load image to a variable.

    Parameters:
    :param img_path: the path to the image file
    :return image file to work on
    """
    img = Image.open(img_path)
    return img.convert('RGBA')


def create_new_image(width,
                     height,
                     fixed_background_color=None,
                     gradient_background_color_start=None,
                     gradient_background_color_end=None):
    """Will create a new image

    Parameters:
    :param width: the width of the new image
    :param height: the height of the new image
    :param fixed_background_color: (optional) a static background color (none for transparent)
    :param gradient_background_color_start: (optional) for a gradient background color, this will be the starting color
    :param gradient_background_color_end: (optional) for a gradient background color, this will be the ending color
    """
    if fixed_background_color is None:
        fixed_background_color = (255, 0, 0, 0)
        image = Image.new('RGBA', (width, height), fixed_background_color)
    else:
        image = Image.new('RGBA', (width, height), tools.hex_to_rgb(fixed_background_color))

    if gradient_background_color_start is not None and gradient_background_color_end is not None:
        image = set_gradient(width, height, gradient_background_color_start, gradient_background_color_end)
    return image


def tilt_image(image, degrees):
    """Will tilt an image by degrees

    Parameters:
    :param image: the image you loaded (from load_img)
    :param degrees: the degrees to tilt
    :return the tilted image
    """
    return image.rotate(degrees, expand=1)


def paste_image(background_img, img_to_paste, x, y):
    """Will paste image on a given background

    Parameters:
    :param background_img: the img which will be served as the background
    (load it from load_img)
    :param img_to_paste: the image to paste on the background (load it from load_img)
    :param x: the x position in which to paste the image
    :param y: the y position in which to paste the image
    """
    background_img.paste(img_to_paste, (int(x), int(y)), img_to_paste)


def draw_text_on_img(img, text, x, y, hex_color, path_to_font, font_size):
    img_draw = img
    if type(img_draw) != ImageDraw:
        img_draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(path_to_font, font_size)
    img_draw.text((x, y), text, tools.hex_to_rgb(hex_color), font=font)
    return img


def resize_img_by_height(img, desired_height):
    """Will resize an image by height

    Parameters:
    :param img: the img which will be resized (load it from load_img)
    :param desired_height: the image desired height
    :return resized image by height (the width will be resized by ratio)
    """
    percent_multiplier = (desired_height / float(img.size[1]))
    desired_width = int((float(img.size[0]) * float(percent_multiplier)))
    return img.resize((desired_width, desired_height), Image.ANTIALIAS)


def resize_img_by_width(img, desired_width):
    """Will resize an image by width

    Parameters:
    :param img: the img which will be resized (load it from load_img)
    :param desired_width: the image desired width
    :return resized image by width (the height will be resized by ratio)
    """
    percent_multiplier = (desired_width / float(img.size[0]))
    desired_height = int((float(img.size[1]) * float(percent_multiplier)))
    return img.resize((desired_width, desired_height), Image.ANTIALIAS)


def resize_img_by_width_and_height(img, desired_width, desired_height):
    """Will resize an image by width and height

    Parameters:
    :param img: the img which will be resized (load it from load_img)
    :param desired_width: the image desired width
    :param desired_height: the image desired height
    :return resized image by width and height
    """
    return img.resize((desired_width, desired_height), Image.ANTIALIAS)


def save_img(img, dest):
    """Will save the image to a given destination

    Parameters:
    :param img: the image to save
    :param dest the path to save the file
    """
    img.save(dest, 'PNG')


def set_gradient(width, height, color_start, color_end):
    gradient = Image.new('RGBA', (width, height), color=0)
    draw = ImageDraw.Draw(gradient)
    color_start_rgb = tools.hex_to_rgb(color_start)
    color_end_rgb = tools.hex_to_rgb(color_end)

    def interpolate(f_co, t_co, interval):
        det_co = [(t - f) / interval for f, t in zip(f_co, t_co)]
        for j in range(interval):
            yield [round(f + det * j) for f, det in zip(f_co, det_co)]

    for i, color in enumerate(interpolate(color_start_rgb, color_end_rgb, width * 2)):
        draw.line([(i, 0), (0, i)], tuple(color), width=1)
    return gradient

