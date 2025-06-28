import math

def compute_cellular_parameters(total_area, cell_radius, cluster_size,
                                user_density, bandwidth_per_cell,
                                traffic_per_user, gos):
    cell_area = (3 * math.sqrt(3) / 2) * (cell_radius ** 2)
    num_cells = math.ceil(total_area / cell_area)
    total_users = total_area * user_density
    channels_per_cell = math.ceil((user_density * cell_area * traffic_per_user) / gos)
    max_users_per_cell = channels_per_cell // traffic_per_user
    total_bandwidth_required = num_cells * bandwidth_per_cell

    return {
        "Single Cell Area (km²)": cell_area,
        "Number of Cells": num_cells,
        "Channels per Cell": channels_per_cell,
        "Max Users per Cell": max_users_per_cell,
        "Total Users": total_users,
        "Total Bandwidth Required (MHz)": total_bandwidth_required
    }
