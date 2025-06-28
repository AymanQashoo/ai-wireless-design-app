def compute_wireless_comm(sampling_rate, quantization_bits, compression_ratio,
                          coding_rate, interleaver_overhead, burst_overhead):
    quantizer_rate = sampling_rate * quantization_bits
    source_encoder_output_rate = quantizer_rate * compression_ratio
    channel_encoder_output_rate = source_encoder_output_rate / coding_rate
    interleaver_output_rate = channel_encoder_output_rate * (1 + interleaver_overhead)
    burst_formatter_output_rate = interleaver_output_rate * (1 + burst_overhead)

    return {
        "Sampler Output Rate (Hz)": sampling_rate,
        "Quantizer Output Rate (bps)": quantizer_rate,
        "Source Encoder Output Rate (bps)": source_encoder_output_rate,
        "Channel Encoder Output Rate (bps)": channel_encoder_output_rate,
        "Interleaver Output Rate (bps)": interleaver_output_rate,
        "Burst Formatter Output Rate (bps)": burst_formatter_output_rate
    }
