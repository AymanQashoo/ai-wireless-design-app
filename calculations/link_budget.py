import math

def compute_link_budget(tx_power, tx_gain, rx_gain, distance_km, frequency_mhz, path_loss_exponent):
    path_loss = (20 * math.log10(distance_km) +
                 20 * math.log10(frequency_mhz) +
                 (10 * path_loss_exponent) + 32.44)
    received_power = tx_power + tx_gain + rx_gain - path_loss
    link_margin = received_power - (-100)

    return {
        "Transmitter Power (dBm)": tx_power,
        "Transmitter Gain (dBi)": tx_gain,
        "Receiver Gain (dBi)": rx_gain,
        "Distance (km)": distance_km,
        "Frequency (MHz)": frequency_mhz,
        "Path Loss (dB)": path_loss,
        "Received Power (dBm)": received_power,
        "Link Margin (dB)": link_margin
    }
