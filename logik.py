from scipy.integrate import odeint
import numpy as np

def lorenzAttraktor(t, u0 = [1, 1, 1], sigma=10, rho=28, beta=8/3):
    def lorenz(u, t):
        x, y, z = u
        dxdt = sigma * (y - x)
        dydt = x * (rho - z) - y
        dzdt = x * y - beta * z
        return [dxdt, dydt, dzdt]
    
    sol = odeint(lorenz, u0, t)
    x = sol[:, 0]
    y = sol[:, 1]
    z = sol[:, 2]
    return x, y, z

def projectionMatrixCalculation(*arg):
    projectionMatrix = np.array([[1, 0, 0],
                                 [0, 1, 0],
                                 [0, 0, 1]])
    x, y, z = arg[0], arg[1], arg[2]
    helpVar = len(x)
    x, y, z = x.reshape(-1, 1), y.reshape(-1, 1), z.reshape(-1, 1)
    vectoren = np.hstack((x, y, z)).reshape(-1, 3, 1)
    return projectionMatrix @ vectoren

def rotation(**kwargs):
    rotX, rotY, rotZ, points= kwargs.get("rotX", 0), kwargs.get("rotY", 0), kwargs.get("rotZ", 0), kwargs.get("points")
    if rotX:
        return _rotationX(points, rotX)
    if rotY:
        return _rotationY(points, rotY)
    if rotZ:
        return _rotationZ(points, rotZ)
    return points.squeeze()

def _rotationX(points, angle):
    matrix = np.array([[1, 0, 0],
                       [0, np.cos(angle), -np.sin(angle)],
                       [0, np.sin(angle), np.cos(angle)]])
    return np.matmul(matrix, points).squeeze()

def _rotationY(points, angle):
    matrix = np.array([[np.cos(angle), 0, np.sin(angle)],
                       [0, 1, 0],
                       [-np.sin(angle), 0, np.cos(angle)]])
    return np.matmul(matrix, points).squeeze()

def _rotationZ(points, angle):
    matrix = np.array([[np.cos(angle), -np.sin(angle), 0],
                       [np.sin(angle), np.cos(angle), 0],
                       [0, 0, 1]])
    return np.matmul(matrix, points).squeeze()
