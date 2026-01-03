import numpy as np
import cv2

def importance_score(block, alpha=0.6, beta=0.4):
    variance = np.var(block)
    edges = cv2.Sobel(block, cv2.CV_64F, 1, 1, ksize=3)
    edge_density = np.mean(abs(edges))
    return alpha * variance + beta * edge_density