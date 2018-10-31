from src.runner import act as run

dataset_paths = ['../data/r01.png', '../data/r02.png', '../data/r03.png']
# dataset_paths = ['../data/r02.png']
repeats = 1

for path in dataset_paths:
    run(path, repeats)
