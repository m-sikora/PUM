import matplotlib.pyplot as plt
import numpy as np

from src.zad1 import act_1
from src.zad2 import act_2
from src.zad3 import act_3


def mean_result(results):
    mean = [np.mean([result[x] for result in results]) for x in range(len(results[0]))]
    std = [np.std([result[x] for result in results]) for x in range(len(results[0]))]
    return mean, std


def run(proc, repeats=10):
    results = [proc() for i in range(repeats)]
    x = results[0][0]
    ys = [result[1] for result in results]
    mean, std = mean_result(ys)
    return x, mean, std


def zad1():
    x, y, e = run(act_1)
    fig = plt.figure()
    plt.errorbar(x, y, e, marker='^', capsize=3)
    fig.suptitle('zad1', fontsize=10)
    plt.xlabel('ilosc wymiarow', fontsize=10)
    plt.ylabel('% dopasowanych punktow', fontsize=10)
    plt.savefig('zad1.png')
    plt.show(block=True)
    plt.close()


def zad2():
    x, y, e = run(act_2)
    fig = plt.figure()
    plt.errorbar(x, y, e, marker='^', capsize=3)
    fig.suptitle('zad1', fontsize=10)
    plt.xlabel('ilosc wymiarow', fontsize=10)
    plt.ylabel('mean/std', fontsize=10)
    plt.savefig('zad2.png')
    plt.show(block=True)
    plt.close()


def zad3():
    x, y, e = run(act_3)
    fig = plt.figure()
    plt.errorbar(x, y, e, marker='^', capsize=3)
    fig.suptitle('zad1', fontsize=10)
    plt.xlabel('ilosc wymiarow', fontsize=10)
    plt.ylabel('sredni kat miedzy wektorami [rad]', fontsize=10)
    plt.savefig('zad3.png')
    plt.show(block=True)
    plt.close()
