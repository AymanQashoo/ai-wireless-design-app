# calculations/ofdm.py

def compute(subcarrier_spacing, num_subcarriers, bits_per_symbol, cp_ratio, num_rb):
    results = {}

    # Useful OFDM symbol duration (seconds)
    T_u = 1 / subcarrier_spacing
    T_cp = cp_ratio * T_u
    T_symbol = T_u + T_cp

    # Data rate per OFDM symbol (bps)
    data_per_symbol = num_subcarriers * bits_per_symbol
    rate_per_symbol = data_per_symbol / T_symbol

    # Assume 12 subcarriers per resource block
    subcarriers_per_rb = 12
    rb_data = subcarriers_per_rb * bits_per_symbol
    rb_rate = rb_data / T_symbol

    # Total data rate using all resource blocks
    total_capacity = num_rb * rb_rate

    # Bandwidth = subcarrier spacing * total subcarriers
    total_bandwidth = subcarrier_spacing * num_subcarriers
    spectral_efficiency = total_capacity / total_bandwidth

    results['OFDM Symbol Duration (s)'] = round(T_symbol, 8)
    results['Data Rate per OFDM Symbol (bps)'] = round(rate_per_symbol, 2)
    results['Data Rate per Resource Block (bps)'] = round(rb_rate, 2)
    results['Total Capacity (bps)'] = round(total_capacity, 2)
    results['Spectral Efficiency (bps/Hz)'] = round(spectral_efficiency, 4)

    return results
