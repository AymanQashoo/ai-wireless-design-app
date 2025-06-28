import math

def compute_cellular_parameters(total_area, cell_radius, cluster_size=7, user_density=1000, bandwidth_per_cell=5):
    cell_area = (3 * math.sqrt(3) / 2) * (cell_radius ** 2)
    num_cells = math.ceil(total_area / cell_area)
    total_users = total_area * user_density
    total_bandwidth_required = num_cells * bandwidth_per_cell

    return {
        "Total Area (km²)": total_area,
        "Cell Radius (km)": cell_radius,
        "Single Cell Area (km²)": cell_area,
        "Cluster Size (N)": cluster_size,
        "Number of Cells Required": num_cells,
        "User Density (users/km²)": user_density,
        "Estimated Total Users": total_users,
        "Bandwidth per Cell (MHz)": bandwidth_per_cell,
        "Total Network Bandwidth (MHz)": total_bandwidth_required
    }
