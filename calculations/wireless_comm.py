# calculations/wireless_comm.py

def compute(fs, bits, src_rate, ch_rate, interleave_ratio, burst_ratio):
    results = {}

    # 1. Sampler output rate (Hz)
    r1 = fs
    results['Sampler Output Rate (Hz)'] = r1

    # 2. Quantizer output rate (bps)
    r2 = fs * bits
    results['Quantizer Output Rate (bps)'] = r2

    # 3. Source Encoder output rate (bps)
    r3 = r2 * src_rate
    results['Source Encoder Output Rate (bps)'] = r3

    # 4. Channel Encoder output rate (bps)
    r4 = r3 / ch_rate
    results['Channel Encoder Output Rate (bps)'] = r4

    # 5. Interleaver output rate (bps)
    r5 = r4 * interleave_ratio
    results['Interleaver Output Rate (bps)'] = r5

    # 6. Burst Formatter output rate (bps)
    r6 = r5 * burst_ratio
    results['Burst Formatter Output Rate (bps)'] = r6

    return results

def compute_wireless_comm(sampler_rate, quantizer_rate):
    sampler_output_rate = sampler_rate
    quantizer_output_rate = quantizer_rate
    source_encoder_output_rate = quantizer_output_rate * 0.6
    channel_encoder_output_rate = source_encoder_output_rate / 0.7
    interleaver_output_rate = channel_encoder_output_rate * 1.1
    burst_formatter_output_rate = interleaver_output_rate * 1.2

    results = {
        "Sampler Output Rate (Hz)": sampler_output_rate,
        "Quantizer Output Rate (bps)": quantizer_output_rate,
        "Source Encoder Output Rate (bps)": source_encoder_output_rate,
        "Channel Encoder Output Rate (bps)": channel_encoder_output_rate,
        "Interleaver Output Rate (bps)": interleaver_output_rate,
        "Burst Formatter Output Rate (bps)": burst_formatter_output_rate
    }

    return results
