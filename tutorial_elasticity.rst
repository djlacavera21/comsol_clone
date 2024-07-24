Tutorial: Solving Elasticity Problems
=====================================

This tutorial guides you through solving elasticity problems using the COMSOL Clone software.

1. Set up the problem:
    - Geometry: Rectangle
    - Width: 1
    - Height: 1
    - Number of elements in X direction: 10
    - Number of elements in Y direction: 10
    - Young's Modulus (E): 210e9
    - Poisson's Ratio (nu): 0.3

2. Run the simulation and visualize the results.

.. code-block:: python

    from physics.structural_mechanics import solve_elasticity
    material_properties = {"E": 210e9, "nu": 0.3}
    mesh_x, mesh_y, solution = solve_elasticity(1, 1, 10, 10, material_properties)

