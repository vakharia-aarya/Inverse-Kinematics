import numpy as np

def line_sphere_intersection(p1, p2, c, r):
    """
    Implements the line-sphere intersection algorithm.
    https://en.wikipedia.org/wiki/Line-sphere_intersection

    :param p1: start of line segment
    :param p2: end of line segment
    :param c: sphere center
    :param r: sphere radius
    :returns: discriminant (value under the square root) of the line-sphere
        intersection formula, as a np.float64 scalar
    """
    # FILL in your code here
    vector = p2-p1
    unit_vector =  vector / np.linalg.norm(vector)
    difference = p1-c  
    
    nabla = np.square(np.dot(unit_vector,difference)) - (np.square(np.linalg.norm(difference)) - r*r)


    return nabla