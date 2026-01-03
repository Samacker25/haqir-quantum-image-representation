import numpy as np
from qiskit import QuantumCircuit

def frqi_encode(image):
    n = int(np.log2(image.size))
    qc = QuantumCircuit(n + 1)
    qc.h(range(n))

    idx = 0
    for pixel in image.flatten():
        theta = pixel * np.pi / 2
        qc.cry(2 * theta, idx % n, n)
        idx += 1

    return qc