import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QComboBox, QLineEdit, QFormLayout
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from physics.poisson import solve_poisson
from physics.structural_mechanics import solve_elasticity
from physics.heat_transfer import solve_heat_transfer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("COMSOL Clone")
        self.setGeometry(100, 100, 800, 600)

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        layout = QVBoxLayout(self.main_widget)

        self.canvas = FigureCanvas(plt.figure())
        layout.addWidget(self.canvas)

        self.physics_combo = QComboBox(self)
        self.physics_combo.addItem("Poisson")
        self.physics_combo.addItem("Elasticity")
        self.physics_combo.addItem("Heat Transfer")
        layout.addWidget(self.physics_combo)

        self.form_layout = QFormLayout()
        self.width_input = QLineEdit("1")
        self.height_input = QLineEdit("1")
        self.num_x_input = QLineEdit("10")
        self.num_y_input = QLineEdit("10")
        self.form_layout.addRow("Width", self.width_input)
        self.form_layout.addRow("Height", self.height_input)
        self.form_layout.addRow("Num X", self.num_x_input)
        self.form_layout.addRow("Num Y", self.num_y_input)
        layout.addLayout(self.form_layout)

        self.material_properties = {"E": QLineEdit("210e9"), "nu": QLineEdit("0.3")}
        self.form_layout.addRow("Young's Modulus (E)", self.material_properties["E"])
        self.form_layout.addRow("Poisson's Ratio (nu)", self.material_properties["nu"])

        self.thermal_properties = {"k": QLineEdit("200")}
        self.form_layout.addRow("Thermal Conductivity (k)", self.thermal_properties["k"])

        self.button = QPushButton("Solve", self)
        self.button.clicked.connect(self.solve)
        layout.addWidget(self.button)

    def solve(self):
        physics = self.physics_combo.currentText()
        width = float(self.width_input.text())
        height = float(self.height_input.text())
        num_x = int(self.num_x_input.text())
        num_y = int(self.num_y_input.text())

        if physics == "Poisson":
            mesh_x, mesh_y, solution = solve_poisson(width, height, num_x, num_y)
        elif physics == "Elasticity":
            material_properties = {
                "E": float(self.material_properties["E"].text()),
                "nu": float(self.material_properties["nu"].text())
            }
            mesh_x, mesh_y, solution = solve_elasticity(width, height, num_x, num_y, material_properties)
        elif physics == "Heat Transfer":
            thermal_properties = {
                "k": float(self.thermal_properties["k"].text())
            }
            mesh_x, mesh_y, solution = solve_heat_transfer(width, height, num_x, num_y, thermal_properties)

        self.canvas.figure.clear()
        ax = self.canvas.figure.add_subplot(111)
        c = ax.contourf(mesh_x, mesh_y, solution, cmap='viridis')
        self.canvas.figure.colorbar(c, ax=ax)
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

