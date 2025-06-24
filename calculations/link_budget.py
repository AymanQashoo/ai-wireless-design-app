# calculations/link_budget.py
import math

def compute(tx_power_dbm, tx_gain_dbi, rx_gain_dbi, freq_mhz, distance_km):
    results = {}

    # Convert frequency and distance for FSPL formula
    f = freq_mhz  # MHz
    d = distance_km  # km

    # Free-space path loss (FSPL) in dB
    fspl = 20 * math.log10(d) + 20 * math.log10(f) + 32.44

    # Received power in dBm
    received_power_dbm = tx_power_dbm + tx_gain_dbi + rx_gain_dbi - fspl

    results['Free-Space Path Loss (dB)'] = round(fspl, 2)
    results['Received Power (dBm)'] = round(received_power_dbm, 2)

    return results
