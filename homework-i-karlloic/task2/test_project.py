from __future__ import division
import numpy as np
import os
import io
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris


def test_division():
    assert (2 / 8) == 0.25

    a = np.array([2])
    b = np.array([8])
    # assert (a/b)[0] == 0.25
    np.testing.assert_array_equal(np.true_divide(a, b), 0.25)


def test_expected_num_chars():
    # content = int(os.popen('wc -m input.txt').read().strip().split()[0])
    text = io.open('input.txt', 'r', encoding='utf-8').read().strip()
    num = len(text)
    assert (num == 6)


def test_iris_crosseval():
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target,
                                                        test_size=0.3, random_state=0)
    clf = KNeighborsClassifier(n_neighbors=3)
    scores = cross_val_score(clf, X_train, y_train, cv=5)
    assert np.mean(scores) >= 0.70
