# calculations/cellular_design.py
import math

def compute(area_km2, cell_radius_km, reuse_factor, users_per_cell, traffic_per_user):
    results = {}

    # Area of one hexagonal cell
    cell_area = 2.598 * (cell_radius_km ** 2)  # approx. area of hexagon in km^2
    num_cells = math.ceil(area_km2 / cell_area)
    total_users = num_cells * users_per_cell
    total_traffic = total_users * traffic_per_user
    cluster_size = reuse_factor
    reused_channels = math.floor(num_cells / cluster_size)

    results['Cell Area (km²)'] = round(cell_area, 3)
    results['Number of Cells'] = num_cells
    results['Total Users Supported'] = total_users
    results['Total Traffic (Erlangs)'] = round(total_traffic, 3)
    results['Reuse Clusters'] = reused_channels

    return results
