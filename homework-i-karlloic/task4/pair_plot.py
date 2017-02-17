# !/usr/bin/python

from sklearn.datasets import load_iris
import matplotlib.pyplot as plt


def iris_pairplot():
    """
    This function just creates a pair plot of the iris dataset

    .. plot:: ../task4/pair_plot.py

    """
    iris_dataset = load_iris()
    data = iris_dataset.data

    count = 1
    plt.figure(num=1, figsize=(14, 12))
    for i in range(0, 4):
        for j in range(0, 4):
            plt.subplot(4, 4, count)
            if i == j:
                plt.hist(data[:, i], 20)
            else:
                plt.scatter(data[:, i], data[:, j], c=iris_dataset.target)
            if j == 0:
                plt.ylabel(iris_dataset.feature_names[i])
            if i == 3:
                plt.xlabel(iris_dataset.feature_names[j])
            count += 1
            plt.legend(iris_dataset.target_names, loc='upper right')

iris_pairplot()
