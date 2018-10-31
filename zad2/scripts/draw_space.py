from src.draw import act as run

# dataset_paths = ['../data/r01.png', '../data/r02.png', '../data/r03.png']
# dataset_paths = ['../data/mini.png']
# dataset_paths = ['../data/r01.png']
dataset_paths = ['../data/r02.png']
# dataset_paths = ['../data/r03.png']

for path in dataset_paths:
    run(path, '../data/r02_mask.png')
