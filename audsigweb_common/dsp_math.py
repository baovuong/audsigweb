import matplotlib.pyplot as plt
import numpy as np

def plot(x, xbounds, ybounds, xlabel, ylabel):
    plt.plot(xbounds, x)
    plt.axis(xbounds + ybounds)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

def genSine(A, f, phi, fs, t):
    return A * np.cos(2 * np.pi * f * np.arange(0, t, 1.0/fs) + phi)

def genComplexSine(k, N):
    return np.exp(-1j * 2 * np.pi * k * np.arange(N) / N)

def DFT(x):
    N = len(x)
    kv = np.arange(N)
    nv = np.arange(N)
    X = np.array([])
    for k in kv:
        s = np.exp(1j * 2 * np.pi * k / N * nv)
        X = np.append(X, sum(x * np.conjugate(s)))
    return X

def IDFT(X):
    N = len(X)
    nv = np.arange(N) # time indexes
    kv = np.arange(N) # frequency indexes
    x = np.array([])
    for n in nv:
        s = np.exp(1j * 2 * np.pi * n / N * kv)
        x = np.append(x, 1.0/N * sum(X*s))

    return x

def genMagSpec(x):
    return abs(DFT(x))

def genPhasSpec(x):
    return np.unwrap(DFT(x))