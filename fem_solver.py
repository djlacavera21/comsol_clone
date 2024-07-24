import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve

class FEMSolver:
    def __init__(self, mesh_x, mesh_y, material_properties=None, element_order=1):
        self.mesh_x = mesh_x
        self.mesh_y = mesh_y
        self.num_x, self.num_y = mesh_x.shape
        self.material_properties = material_properties
        self.element_order = element_order

    def shape_functions(self, xi, eta):
        if self.element_order == 1:
            N = np.array([(1 - xi) * (1 - eta), xi * (1 - eta), xi * eta, (1 - xi) * eta])
        elif self.element_order == 2:
            N = np.array([
                (1 - xi) * (1 - eta) * (1 + xi + eta),
                xi * (1 - eta) * (1 - xi + eta),
                xi * eta * (1 - xi - eta),
                (1 - xi) * eta * (1 + xi - eta),
                4 * xi * (1 - xi) * (1 - eta),
                4 * xi * eta * (1 - eta),
                4 * (1 - xi) * xi * eta,
                4 * (1 - xi) * eta * (1 - eta)
            ])
        return N

    def assemble_system(self):
        num_nodes = self.num_x * self.num_y
        A = lil_matrix((num_nodes, num_nodes))
        b = np.zeros(num_nodes)

        dx = self.mesh_x[1, 0] - self.mesh_x[0, 0]
        dy = self.mesh_y[0, 1] - self.mesh_y[0, 0]

        for i in range(1, self.num_x - 1):
            for j in range(1, self.num_y - 1):
                n = i * self.num_y + j
                A[n, n] = -4 / (dx * dy)
                A[n, n - 1] = 1 / dy**2
                A[n, n + 1] = 1 / dy**2
                A[n, n - self.num_y] = 1 / dx**2
                A[n, n + self.num_y] = 1 / dx**2
                b[n] = -1  # Example source term

        return A, b

    def solve(self):
        A, b = self.assemble_system()
        u = spsolve(A, b)
        return u.reshape((self.num_x, self.num_y))

    def solve_heat_transfer(self):
        k = self.material_properties['k']
        num_nodes = self.num_x * self.num_y
        A = lil_matrix((num_nodes, num_nodes))
        b = np.zeros(num_nodes)

        dx = self.mesh_x[1, 0] - self.mesh_x[0, 0]
        dy = self.mesh_y[0, 1] - self.mesh_y[0, 0]

        for i in range(1, self.num_x - 1):
            for j in range(1, self.num_y - 1):
                n = i * self.num_y + j
                A[n, n] = -4 * k / (dx * dy)
                A[n, n - 1] = k / dy**2
                A[n, n + 1] = k / dy**2
                A[n, n - self.num_y] = k / dx**2
                A[n, n + self.num_y] = k / dx**2
                b[n] = 0  # Example source term

        A = A.tocsr()
        u = spsolve(A, b)
        return u.reshape((self.num_x, self.num_y))

