def compute_wireless_comm(
    bandwidth_khz, quantization_bits, source_ratio, channel_ratio,
    interleaver_overhead=0.0, burst_overhead=0.0, modulation_type="QPSK"
):
    modulation_bits = MODULATION_BITS.get(modulation_type, 0)  # default 0 if none selected
    results = {}

    # Step 1: Nyquist Sampling Rate (kHz)
    nyquist_rate_khz = 2 * bandwidth_khz
    results["Nyquist Sampling Rate (kHz)"] = nyquist_rate_khz

    # Step 2: Quantizer Output Rate (kbps)
    quantizer_output_kbps = nyquist_rate_khz * quantization_bits
    results["Quantizer Output Rate (kbps)"] = quantizer_output_kbps

    # Step 3: Source Encoder Output Rate (kbps)
    source_output_kbps = quantizer_output_kbps * source_ratio
    results["Source Encoder Output Rate (kbps)"] = source_output_kbps

    # Step 4: Channel Encoder Output Rate (kbps)
    channel_output_kbps = source_output_kbps / channel_ratio
    results["Channel Encoder Output Rate (kbps)"] = channel_output_kbps

    # Step 5: Interleaver Output Rate (kbps)
    interleaver_output_kbps = channel_output_kbps * (1 + interleaver_overhead)
    results["Interleaver Output Rate (kbps)"] = interleaver_output_kbps

    # Step 6: Burst Formatting Output Rate (kbps)
    burst_output_kbps = interleaver_output_kbps * (1 + burst_overhead)
    results["Burst Formatter Output Rate (kbps)"] = burst_output_kbps

    # Step 7: Data Rate After Modulation
    if modulation_bits > 0:
        results["Data Rate After Modulation (kbps)"] = burst_output_kbps
        results["Modulation Bits per Symbol"] = modulation_bits
        results["Symbols per Second Needed"] = burst_output_kbps / modulation_bits
    else:
        results["Modulation Error"] = "Invalid or Unselected Modulation Type"

    return results
