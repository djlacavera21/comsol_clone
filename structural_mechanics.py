from mesh.mesh_generator import MeshGenerator
from solvers.fem_solver import FEMSolver

def solve_elasticity(width, height, num_x, num_y, material_properties):
    mesh_gen = MeshGenerator('rectangle', num_x, num_y, width=width, height=height)
    mesh_x, mesh_y = mesh_gen.generate_mesh()
    solver = FEMSolver(mesh_x, mesh_y, material_properties)
    solution = solver.solve_elasticity()
    return mesh_x, mesh_y, solution

