import math

def compute_link_budget(
    tx_power_dbm,
    tx_gain_dbi,
    rx_gain_dbi,
    distance_km,
    frequency_mhz,
    system_losses_db
):
    path_loss_db = 20 * math.log10(distance_km) + 20 * math.log10(frequency_mhz) + 32.44

    received_power_dbm = tx_power_dbm + tx_gain_dbi + rx_gain_dbi - path_loss_db - system_losses_db

    return {
        "Transmitted Power (dBm)": tx_power_dbm,
        "Received Power (dBm)": received_power_dbm
    }
