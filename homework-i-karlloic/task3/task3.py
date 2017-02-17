import numpy as np
from sklearn.datasets import load_iris


def summary(data, axis=0):
    r"""
    This function computes mean and standard deviation of a
    dataset along the specified “axis”

    Parameters
    ----------
    data : numpy-array
        Dataset for calculations

    axis : int
        Axis for mean and std calculation. Default 0


    Returns
    -------
    tuple
        2-tuple of mean and standard deviation values

    Raises
    ------
    ValueError
        If data parameter is not a numpy-array

    """
    if type(data) is not np.ndarray:
        raise ValueError("Dataset is not a numpy-array")

    m = np.mean(data, axis=axis)
    s = np.std(data, axis=axis)
    return m, s


iris_dataset = load_iris()
print(summary(iris_dataset.data, None))

