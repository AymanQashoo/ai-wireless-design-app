import math

def compute_cellular_parameters(
    total_bandwidth_mhz,
    channel_bandwidth_mhz,
    num_cells,
    cell_radius_km,
    reuse_factor,
    distance_km
):
    total_channels = total_bandwidth_mhz / channel_bandwidth_mhz

    channels_per_cell = total_channels / reuse_factor

    total_system_capacity = channels_per_cell * num_cells

    reuse_distance = cell_radius_km * math.sqrt(3 * reuse_factor)

    return {
        "Channels per Cell": channels_per_cell,
        "Total System Capacity": total_system_capacity,
        "Frequency Reuse Distance (km)": reuse_distance
    }
