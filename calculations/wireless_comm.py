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
