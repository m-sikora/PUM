from PIL import Image
from src.parse_image import act as parse_image
from src.knn import act as knn
import random
import numpy as np


def generate_test_points(im):
    r = []
    width, height = im.size
    for i in range(width):
        for j in range(height):
            r.append((i, j, 0))
    return r


colors = [
    (0, 0, 0, 255),
    (255, 0, 0, 255),
    (0, 255, 0, 255),
    (0, 0, 255, 255),
]


def act(path, mask_path=None):
    print(path)
    im = Image.open(path)
    points = parse_image(im)
    scores = []
    width, height = im.size

    random.shuffle(points)
    train_to_test_ratio = 0.90
    points_len = len(points)
    train_test_boundary = int(points_len * train_to_test_ratio)

    train_points = points[:train_test_boundary]
    test_points = generate_test_points(im)
    if mask_path is not None:
        mask_im = Image.open(mask_path)
        mask_pix = mask_im.load()
        mask_points = []
        for i in range(width):
            for j in range(height):
                pixel = mask_pix[i, j]
                r, g, b, a = pixel
                if r + g + b == 0:
                    mask_points.append((i, j, 0))
        test_points = mask_points
    _, result = knn(train_points, test_points, metric='dist', vote='weighted')

    result_image = Image.new('RGB', (width, height))
    pixels = result_image.load()
    for x, y, c in result:
        pixels[x, y] = colors[c]
    result_image.save('out.png'.format(path))

