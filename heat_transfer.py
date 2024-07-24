from mesh.mesh_generator import MeshGenerator
from solvers.fem_solver import FEMSolver

def solve_heat_transfer(width, height, num_x, num_y, thermal_properties):
    mesh_gen = MeshGenerator('rectangle', num_x, num_y, width=width, height=height)
    mesh_x, mesh_y = mesh_gen.generate_mesh()
    solver = FEMSolver(mesh_x, mesh_y, thermal_properties)
    solution = solver.solve_heat_transfer()
    return mesh_x, mesh_y, solution

