import math

def compute_link_budget(
    tx_power_dbm,
    tx_gain_dbi,
    rx_gain_dbi,
    distance_km,
    frequency_mhz,
    system_losses_db
):
    # Free Space Path Loss (FSPL) formula in dB
    path_loss_db = 20 * math.log10(distance_km) + 20 * math.log10(frequency_mhz) + 32.44

    # Received Power in dBm
    received_power_dbm = tx_power_dbm + tx_gain_dbi + rx_gain_dbi - path_loss_db - system_losses_db

    return {
        "Transmitted Power (dBm)": tx_power_dbm,
        "Transmitter Gain (dBi)": tx_gain_dbi,
        "Receiver Gain (dBi)": rx_gain_dbi,
        "Distance (km)": distance_km,
        "Frequency (MHz)": frequency_mhz,
        "System Losses (dB)": system_losses_db,
        "Path Loss (dB)": path_loss_db,
        "Received Power (dBm)": received_power_dbm
    }
