import numpy as np

class MeshGenerator:
    def __init__(self, geometry, num_elements, element_order=1, **kwargs):
        self.geometry = geometry
        self.num_elements = num_elements
        self.element_order = element_order
        self.kwargs = kwargs

    def generate_mesh(self):
        if self.geometry == 'rectangle':
            return self._generate_rectangle_mesh()
        elif self.geometry == 'circle':
            return self._generate_circle_mesh()
        elif self.geometry == 'ellipse':
            return self._generate_ellipse_mesh()
        else:
            raise ValueError("Unsupported geometry")

    def _generate_rectangle_mesh(self):
        if self.element_order == 1:
            x = np.linspace(0, self.kwargs.get('width', 1), self.num_elements)
            y = np.linspace(0, self.kwargs.get('height', 1), self.num_elements)
            xv, yv = np.meshgrid(x, y)
        elif self.element_order == 2:
            x = np.linspace(0, self.kwargs.get('width', 1), 2*self.num_elements-1)
            y = np.linspace(0, self.kwargs.get('height', 1), 2*self.num_elements-1)
            xv, yv = np.meshgrid(x, y)
        return xv, yv

    def _generate_circle_mesh(self):
        theta = np.linspace(0, 2 * np.pi, self.num_elements)
        r = np.linspace(0, self.kwargs.get('radius', 1), self.num_elements)
        theta, r = np.meshgrid(theta, r)
        xv = r * np.cos(theta)
        yv = r * np.sin(theta)
        return xv, yv

    def _generate_ellipse_mesh(self):
        theta = np.linspace(0, 2 * np.pi, self.num_elements)
        a = self.kwargs.get('a', 1)
        b = self.kwargs.get('b', 0.5)
        r = np.linspace(0, 1, self.num_elements)
        theta, r = np.meshgrid(theta, r)
        xv = a * r * np.cos(theta)
        yv = b * r * np.sin(theta)
        return xv, yv

