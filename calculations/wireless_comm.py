MODULATION_BITS = {
    "QPSK": 2,
    "16-QAM": 4,
    "64QAM": 6
}

def compute_wireless_comm(
    bandwidth_khz, quantization_bits, source_ratio, channel_ratio, modulation_type="QPSK"
):
    modulation_bits = MODULATION_BITS.get(modulation_type, 0)
    results = {}

    nyquist_rate_khz = 2 * bandwidth_khz
    results["Nyquist Sampling Rate (kHz)"] = nyquist_rate_khz

    quantizer_output_kbps = nyquist_rate_khz * quantization_bits
    results["Quantizer Output Rate (kbps)"] = quantizer_output_kbps

    source_output_kbps = quantizer_output_kbps * source_ratio
    results["Source Encoder Output Rate (kbps)"] = source_output_kbps

    channel_output_kbps = source_output_kbps * channel_ratio
    results["Channel Encoder Output Rate (kbps)"] = channel_output_kbps

    interleaver_output_kbps = channel_output_kbps
    results["Interleaver Output Rate (kbps)"] = interleaver_output_kbps

    
    burst_output_kbps = interleaver_output_kbps * 2.376
    results["Burst Formatter Output Rate (kbps)"] = burst_output_kbps

    if modulation_bits > 0:
        results["Data Rate After Modulation (kbps)"] = burst_output_kbps
        results["Modulation Bits per Symbol"] = modulation_bits
    else:
        results["Modulation Error"] = "Please select a valid modulation type."

    return results
