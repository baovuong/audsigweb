import numpy as np

def dft(x):
    N = len(x)
    kv = np.arange(N)
    nv = np.arange(N)
    X = np.array([])
    for k in kv:
        s = np.exp(1j * 2 * np.pi * k / N * nv)
        X = np.append(X, sum(x * np.conjugate(s)))

    return X