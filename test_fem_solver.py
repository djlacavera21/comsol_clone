import unittest
import numpy as np
from mesh.mesh_generator import MeshGenerator
from solvers.fem_solver import FEMSolver

class TestFEMSolver(unittest.TestCase):
    def test_poisson_solver(self):
        mesh_gen = MeshGenerator('rectangle', 10, width=1, height=1)
        mesh_x, mesh_y = mesh_gen.generate_mesh()
        solver = FEMSolver(mesh_x, mesh_y)
        solution = solver.solve()
        self.assertIsInstance(solution, np.ndarray)

    def test_elasticity_solver(self):
        mesh_gen = MeshGenerator('rectangle', 10, width=1, height=1)
        mesh_x, mesh_y = mesh_gen.generate_mesh()
        material_properties = {"E": 210e9, "nu": 0.3}
        solver = FEMSolver(mesh_x, mesh_y, material_properties)
        solution = solver.solve_elasticity()
        self.assertIsInstance(solution, np.ndarray)

if __name__ == "__main__":
    unittest.main()

