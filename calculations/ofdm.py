def compute_ofdm_parameters(bandwidth, num_subcarriers):
    subcarrier_spacing = bandwidth / num_subcarriers
    symbol_duration = 1 / subcarrier_spacing
    cyclic_prefix_duration = symbol_duration * 0.25  # typically 25% of symbol duration
    total_symbol_duration = symbol_duration + cyclic_prefix_duration

    return {
        "Bandwidth (Hz)": bandwidth,
        "Number of Subcarriers": num_subcarriers,
        "Subcarrier Spacing (Hz)": subcarrier_spacing,
        "Symbol Duration (s)": symbol_duration,
        "Cyclic Prefix Duration (s)": cyclic_prefix_duration,
        "Total Symbol Duration (s)": total_symbol_duration
    }
