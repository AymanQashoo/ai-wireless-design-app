import math

def compute_link_budget(required_rx_power, tx_gain, rx_gain, distance_km, frequency_mhz):
    # Calculate path loss (Free Space Path Loss)
    path_loss = 20 * math.log10(distance_km) + 20 * math.log10(frequency_mhz) + 32.44

    # Calculate required transmitted power to achieve desired received power
    required_tx_power = required_rx_power + path_loss - tx_gain - rx_gain

    # Conversely, calculate actual received power if transmitter power was given
    actual_rx_power = required_tx_power + tx_gain + rx_gain - path_loss

    return {
        "Required Received Signal Strength (dBm)": required_rx_power,
        "Calculated Path Loss (dB)": path_loss,
        "Required Transmitted Power (dBm)": required_tx_power,
        "Actual Received Power (dBm)": actual_rx_power
    }
