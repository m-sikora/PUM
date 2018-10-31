def hash_color(r, g, b):
    return r + g * 2**8 + b * 2**16


def act(image):
    pix = image.load()
    width, height = image.size
    points = []
    color_classes = {}

    for i in range(width):
        for j in range(height):
            pixel = pix[i, j]
            r, g, b, a = pixel
            if r + g + b == 255 * 3:
                continue

            color_hash = hash_color(r, g, b)
            try:
                class_match = color_classes[color_hash]
            except KeyError:
                color_classes[color_hash] = len(color_classes) + 1
                class_match = color_classes[color_hash]
                assert class_match

            points.append((i, j, class_match))

    return points
