MODULATION_BITS = {
    "QPSK": 2,
    "16-QAM": 4,
    "64-QAM": 6,
    "1024-QAM": 10
}

def compute_ofdm_parameters(
    rb_bandwidth_khz,
    subcarrier_spacing_khz,
    num_symbols_per_rb,
    rb_duration_ms,
    modulation_type,
    parallel_blocks
):
    num_subcarriers = 12
    bits_per_symbol = MODULATION_BITS.get(modulation_type, 0)

    total_bits_per_symbol = num_subcarriers * bits_per_symbol
    total_bits_per_rb = total_bits_per_symbol * num_symbols_per_rb

    rb_duration_s = rb_duration_ms / 1000.0

    rb_rate_bps = total_bits_per_rb / rb_duration_s

    total_rate_bps = rb_rate_bps * parallel_blocks

    return {
        "Number of Subcarriers": num_subcarriers,
        "Total Bits per Symbol": total_bits_per_symbol,
        "Total Bits per Resource Block": total_bits_per_rb,
        "Max Transmission Rate (bps)": total_rate_bps
    }
