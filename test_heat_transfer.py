import unittest
import numpy as np
from mesh.mesh_generator import MeshGenerator
from solvers.fem_solver import FEMSolver

class TestHeatTransferSolver(unittest.TestCase):
    def test_heat_transfer_solver(self):
        mesh_gen = MeshGenerator('rectangle', 10, width=1, height=1)
        mesh_x, mesh_y = mesh_gen.generate_mesh()
        thermal_properties = {"k": 200}
        solver = FEMSolver(mesh_x, mesh_y, thermal_properties)
        solution = solver.solve_heat_transfer()
        self.assertIsInstance(solution, np.ndarray)

if __name__ == "__main__":
    unittest.main()

