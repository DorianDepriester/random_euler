"""Random rotation matrix generators."""

import numpy as np


def generate(dim):
    """Generate a random rotation matrix.

    Args:
        dim (int): The dimension of the matrix.

    Returns:
        np.matrix: A rotation matrix.

    Raises:
        ValueError: If `dim` is not 2 or 3.

    """
    if dim == 2:
        return generate_2d()
    elif dim == 3:
        return generate_3d()
    else:
        raise ValueError('Dimension {} is not supported. Use 2 or 3 instead.'
                         .format(dim))


def generate_2d():
    """Generate a 2D random rotation matrix.

    Returns:
        np.matrix: A 2D rotation matrix.

    """
    x = np.random.random()
    M = np.matrix([[np.cos(2 * np.pi * x), -np.sin(2 * np.pi * x)],
                   [np.sin(2 * np.pi * x), np.cos(2 * np.pi * x)]])
    return M


def generate_3d():
    """Generate a 3D random rotation matrix.

    Returns:
        np.matrix: A 3D rotation matrix.

    """
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

def generate_Euler():
	M = generate_3d()
	Phi = np.arccos(M[2,2])
	if Phi == 0.0:
		phi1 = np.arctan2(-M[1,0], M[0,0])
		phi2 = 0	
	elif Phi == np.pi:
		phi1 = np.arctan2(M[1,0], M[0,0])
		phi2 = 0
	else:
		phi1 = np.arctan2(M[2,0], -M[2,1])
		phi2 = np.arctan2(M[0,2], M[1,2])
	if phi1 < 0:
		phi1 += 2*np.pi
	if phi2 < 0:
		phi2 += 2*np.pi
	return phi1,Phi,phi2
