"""Random rotation matrix generators."""
import numpy as np


def generate(dim: int) -> np.matrix:
    """Generate a random rotation matrix."""
    if dim == 2:
        return generate_2d()
    elif dim == 3:
        return generate_3d()


def generate_2d() -> np.matrix:
    """Generate a 2D random rotation matrix."""
    x = np.random.random()
    M = np.matrix([[np.cos(2 * np.pi * x), -np.sin(2 * np.pi * x)],
                   [np.sin(2 * np.pi * x), np.cos(2 * np.pi * x)]])
    return M


def generate_3d() -> np.matrix:
    """Generate a 3D random rotation matrix."""
    x1, x2, x3 = np.random.rand(3)
    R = np.matrix([[np.cos(2 * np.pi * x1), np.sin(2 * np.pi * x1), 0],
                   [-np.sin(2 * np.pi * x1), np.cos(2 * np.pi * x1), 0],
                   [0, 0, 1]])
    v = np.matrix([[np.cos(2 * np.pi * x2) * np.sqrt(x3)],
                   [np.sin(2 * np.pi * x2) * np.sqrt(x3)],
                   [np.sqrt(1 - x3)]])
    H = np.eye(3) - 2 * v * v.T
    M = -H * R
    return M
