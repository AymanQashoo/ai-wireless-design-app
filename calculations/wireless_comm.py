def compute_wireless_comm(sampler_rate, quantizer_rate):
    source_encoder_output_rate = quantizer_rate * 0.6  # assuming 40% compression
    channel_encoder_output_rate = source_encoder_output_rate / 0.7  # assuming 30% redundancy
    interleaver_output_rate = channel_encoder_output_rate * 1.1  # assuming 10% overhead
    burst_formatter_output_rate = interleaver_output_rate * 1.2  # assuming 20% overhead

    return {
        "Sampler Output Rate (Hz)": sampler_rate,
        "Quantizer Output Rate (bps)": quantizer_rate,
        "Source Encoder Output Rate (bps)": source_encoder_output_rate,
        "Channel Encoder Output Rate (bps)": channel_encoder_output_rate,
        "Interleaver Output Rate (bps)": interleaver_output_rate,
        "Burst Formatter Output Rate (bps)": burst_formatter_output_rate
    }
