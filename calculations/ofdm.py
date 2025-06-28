def compute_ofdm_parameters(bandwidth, fft_size, cyclic_prefix_ratio,
                            modulation_order, num_resource_blocks, symbols_per_slot=14):
    subcarrier_spacing = bandwidth / fft_size
    symbol_duration = 1 / subcarrier_spacing
    cyclic_prefix_duration = symbol_duration * cyclic_prefix_ratio
    total_symbol_duration = symbol_duration + cyclic_prefix_duration

    # 1 Resource Element = 1 subcarrier in 1 symbol
    data_rate_per_re = modulation_order / total_symbol_duration
    data_rate_per_symbol = fft_size * data_rate_per_re
    data_rate_per_rb = 12 * symbols_per_slot * data_rate_per_re  # 12 subcarriers × N symbols
    total_capacity = num_resource_blocks * data_rate_per_rb
    spectral_efficiency = total_capacity / bandwidth

    return {
        "Subcarrier Spacing (Hz)": subcarrier_spacing,
        "Symbol Duration (s)": symbol_duration,
        "Cyclic Prefix Duration (s)": cyclic_prefix_duration,
        "Total Symbol Duration (s)": total_symbol_duration,
        "Data Rate per Resource Element (bps)": data_rate_per_re,
        "Data Rate per OFDM Symbol (bps)": data_rate_per_symbol,
        "Data Rate per Resource Block (bps)": data_rate_per_rb,
        "Maximum Transmission Capacity (bps)": total_capacity,
        "Spectral Efficiency (bps/Hz)": spectral_efficiency
    }
