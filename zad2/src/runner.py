from PIL import Image
from src.parse_image import act as parse_image
from src.knn import act as knn
import random
import numpy as np


def act(path, repeats=1):
    print(path)
    im = Image.open(path)
    points = parse_image(im)
    scores = []

    for i in range(repeats):
        random.shuffle(points)
        train_to_test_ratio = 0.90
        points_len = len(points)
        train_test_boundary = int(points_len * train_to_test_ratio)

        train_points = points[:train_test_boundary]
        test_points = points[train_test_boundary:]
        score, _ = knn(train_points, test_points, metric='dist', vote='weighted')
        scores.append(score)

    avg_score = np.mean(np.array(scores))
    print('avg score: {}'.format(avg_score))
    return avg_score
