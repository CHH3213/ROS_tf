## 这是机器人坐标系转换库函数(tf)<http://docs.ros.org/en/kinetic/api/tf/html/python/transformations.html>

Matrices (M) can be inverted using numpy.linalg.inv(M), concatenated using numpy.dot(M0, M1), or used to transform homogeneous coordinates (v) using numpy.dot(M, v) for shape (4, *) “point of arrays”, respectively numpy.dot(v, M.T) for shape (*, 4) “array of points”.

Calculations are carried out with numpy.float64 precision.

This Python implementation is not optimized for speed.

Vector, point, quaternion, and matrix function arguments are expected to be “array like”, i.e. tuple, list, or numpy arrays.

Return types are numpy arrays unless specified otherwise.

Angles are in radians unless specified otherwise.

Quaternions ix+jy+kz+w are represented as [x, y, z, w].

Use the transpose of transformation matrices for OpenGL glMultMatrixd().

A triple of Euler angles can be applied/interpreted in 24 ways, which can be specified using a 4 character string or encoded 4-tuple:

- Axes 4-string: e.g. ‘sxyz’ or ‘ryxy’

  - first character : rotations are applied to ‘s’tatic or ‘r’otating frame
  - remaining characters : successive rotation axis ‘x’, ‘y’, or ‘z’
- Axes 4-tuple: e.g. (0, 0, 0, 0) or (1, 1, 1, 1)

  - inner axis: code of axis (‘x’:0, ‘y’:1, ‘z’:2) of rightmost matrix.
  - parity : even (0) if inner axis ‘x’ is followed by ‘y’, ‘y’ is followed by ‘z’, or ‘z’ is followed by ‘x’. Otherwise odd (1).
  - repetition : first and last axis are same (1) or different (0).
  -frame : rotations are applied to static (0) or rotating (1) frame.
