from PIL import Image


def hash_color(r, g, b):
    return r + g * 2 ** 8 + b * 2 ** 16


def act(path):
    image = Image.open(path)
    pix = image.load()
    width, height = image.size
    points = []
    color_labels = [
        'r',
        'g',
        'b',
        'y',
    ]

    for i in range(width):
        for j in range(height):
            pixel = pix[i, j]
            if pixel == 0:
                continue
            class_match = pixel - 1
            points.append((i, j, color_labels[class_match]))

    return points
