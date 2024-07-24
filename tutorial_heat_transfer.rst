Tutorial: Solving Heat Transfer Problems
========================================

This tutorial guides you through solving heat transfer problems using the COMSOL Clone software.

1. Set up the problem:
    - Geometry: Rectangle
    - Width: 1
    - Height: 1
    - Number of elements in X direction: 10
    - Number of elements in Y direction: 10
    - Thermal Conductivity (k): 200

2. Run the simulation and visualize the results.

.. code-block:: python

    from physics.heat_transfer import solve_heat_transfer
    thermal_properties = {"k": 200}
    mesh_x, mesh_y, solution = solve_heat_transfer(1, 1, 10, 10, thermal_properties)

