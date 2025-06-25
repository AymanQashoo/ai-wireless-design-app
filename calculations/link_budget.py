def compute_link_budget(tx_power, tx_gain, rx_gain, path_loss):
    received_power = tx_power + tx_gain + rx_gain - path_loss

    return {
        "Transmitter Power (dBm)": tx_power,
        "Transmitter Gain (dBi)": tx_gain,
        "Receiver Gain (dBi)": rx_gain,
        "Path Loss (dB)": path_loss,
        "Received Power (dBm)": received_power
    }
