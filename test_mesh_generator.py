import unittest
from mesh.mesh_generator import MeshGenerator

class TestMeshGenerator(unittest.TestCase):
    def test_rectangle_mesh(self):
        mesh_gen = MeshGenerator('rectangle', 10, width=1, height=1)
        mesh_x, mesh_y = mesh_gen.generate_mesh()
        self.assertEqual(mesh_x.shape, (10, 10))
        self.assertEqual(mesh_y.shape, (10, 10))

    def test_circle_mesh(self):
        mesh_gen = MeshGenerator('circle', 10, radius=1)
        mesh_x, mesh_y = mesh_gen.generate_mesh()
        self.assertEqual(mesh_x.shape, (10, 10))
        self.assertEqual(mesh_y.shape, (10, 10))

if __name__ == "__main__":
    unittest.main()

