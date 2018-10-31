from src.metrics import dist, build_maha


def std_vote(neighbours, _):
    color_classes = [c for (_, _, c) in neighbours]
    return max(set(color_classes), key=color_classes.count)


def weighted_vote(neighbours, me):
    scores = {}
    for x, y, c in neighbours:
        if scores.get(c) is None:
            scores[c] = 0
        neighbour_dist = dist(me, (x, y, c))
        scores[c] += neighbour_dist

    min_score = 9000
    winner = None
    for c, score in scores.items():
        if score < min_score:
            winner = c

    return winner


metrics = {
    'dist': lambda _: dist,
    'maha': build_maha,
}

votes = {
    'std': std_vote,
    'weighted': weighted_vote,
}


def act(train_points, test_points, metric='dist', vote='std'):
    metric_proc = metrics[metric](train_points)
    vote_proc = votes[vote]

    k = 3
    matches = 0
    errors = 0
    result = []
    test_len = len(test_points)
    passed = 0

    for point in test_points:
        x, y, c = point
        print('{} , {} : {}'.format(x, y, 100 * passed / test_len))
        train_points.sort(key=lambda p_f: metric_proc(point, p_f))
        closest_neighbours = train_points[0:k]
        outcome = vote_proc(closest_neighbours, point)
        result.append((x, y, outcome))
        if outcome == c:
            matches += 1
        else:
            errors += 1
        passed += 1

    efficiency = matches / (matches + errors)
    print('  efficiency: {}'.format(efficiency))
    return efficiency, result
