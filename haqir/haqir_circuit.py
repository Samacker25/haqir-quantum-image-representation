from qiskit import QuantumCircuit
import numpy as np

def haqir_encode(block_scores):
    qc = QuantumCircuit(7)
    qc.h(range(6))

    for score in block_scores:
        angle = min(score * np.pi, np.pi / 2)
        qc.ry(angle, 6)

    return qc
