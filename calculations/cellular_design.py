import math

def compute_cellular_parameters(total_area, cell_radius):
    cell_area = (3 * math.sqrt(3) / 2) * (cell_radius ** 2)
    num_cells = math.ceil(total_area / cell_area)

    return {
        "Total Area (km²)": total_area,
        "Cell Radius (km)": cell_radius,
        "Single Cell Area (km²)": cell_area,
        "Number of Cells": num_cells
    }
