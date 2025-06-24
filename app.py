import streamlit as st
from ai_agent import explain_results

st.set_page_config(page_title="Wireless Comm Designer", layout="wide")
st.title("Wireless Communication System Design Tool")

# Tabs for sections
tab1, tab2, tab3, tab4 = st.tabs([
    "Wireless Comm System", "OFDM System", "Link Budget", "Cellular Design"
])

# ---------------------- TAB 1: Wireless Communication System ----------------------
with tab1:
    st.header("Wireless Communication System")

    sampling_rate = st.number_input("Sampling Rate (Hz)", value=1000.0)
    bits_per_sample = st.number_input("Bits per Sample", min_value=1, step=1, value=1)
    source_encoder_rate = st.slider("Source Encoder Rate (0-1)", 0.0, 1.0, 0.8)
    channel_encoder_rate = st.slider("Channel Encoder Rate (0-1)", 0.0, 1.0, 0.6)
    interleaver_overhead = st.number_input("Interleaver Overhead (e.g. 1.1 = 10%)", value=1.1)
    burst_formatter_overhead = st.number_input("Burst Formatter Overhead", value=1.2)

    if st.button("Compute Wireless Comm"):
        sampler_output_rate = sampling_rate * bits_per_sample
        quantizer_output_rate = sampler_output_rate
        source_encoder_output_rate = quantizer_output_rate * source_encoder_rate
        channel_encoder_output_rate = source_encoder_output_rate / channel_encoder_rate
        interleaver_output_rate = channel_encoder_output_rate * interleaver_overhead
        burst_formatter_output_rate = interleaver_output_rate * burst_formatter_overhead

        results = {
            "Sampler Output Rate (Hz)": sampler_output_rate,
            "Quantizer Output Rate (bps)": quantizer_output_rate,
            "Source Encoder Output Rate (bps)": source_encoder_output_rate,
            "Channel Encoder Output Rate (bps)": channel_encoder_output_rate,
            "Interleaver Output Rate (bps)": interleaver_output_rate,
            "Burst Formatter Output Rate (bps)": burst_formatter_output_rate,
        }

        st.json(results)
        explanation = explain_results("wireless_comm", results)
        st.info(explanation)

# ---------------------- TAB 2: OFDM System ----------------------
with tab2:
    st.header("OFDM System")

    subcarriers = st.number_input("Number of Subcarriers", min_value=1, value=64)
    cp_length = st.number_input("Cyclic Prefix Length (samples)", min_value=0, value=16)
    symbol_duration = st.number_input("Symbol Duration (μs)", value=3.2)
    data_rate_per_subcarrier = st.number_input("Data Rate per Subcarrier (bps)", value=100.0)

    if st.button("Compute OFDM System"):
        ofdm_symbol_time = symbol_duration + (cp_length * symbol_duration / subcarriers)
        total_data_rate = subcarriers * data_rate_per_subcarrier

        results = {
            "OFDM Symbol Time (μs)": ofdm_symbol_time,
            "Total Data Rate (bps)": total_data_rate
        }

        st.json(results)
        explanation = explain_results("ofdm", results)
        st.info(explanation)

# ---------------------- TAB 3: Link Budget ----------------------
with tab3:
    st.header("Link Budget")

    tx_power = st.number_input("Transmit Power (dBm)", value=30.0)
    tx_gain = st.number_input("Transmit Antenna Gain (dBi)", value=2.0)
    rx_gain = st.number_input("Receive Antenna Gain (dBi)", value=2.0)
    path_loss = st.number_input("Path Loss (dB)", value=100.0)
    noise_figure = st.number_input("Receiver Noise Figure (dB)", value=5.0)

    if st.button("Compute Link Budget"):
        received_power = tx_power + tx_gain + rx_gain - path_loss
        snr = received_power - noise_figure

        results = {
            "Received Power (dBm)": received_power,
            "Estimated SNR (dB)": snr
        }

        st.json(results)
        explanation = explain_results("link_budget", results)
        st.info(explanation)

# ---------------------- TAB 4: Cellular Design ----------------------
with tab4:
    st.header("Cellular Design")

    area_km2 = st.number_input("Service Area (km²)", value=100.0)
    users_per_km2 = st.number_input("Users per km²", value=500)
    sector_capacity = st.number_input("Sector Capacity (users)", value=200)
    sectors_per_cell = st.number_input("Sectors per Cell", value=3)

    if st.button("Compute Cellular Design"):
        total_users = area_km2 * users_per_km2
        total_sectors = total_users / sector_capacity
        required_cells = total_sectors / sectors_per_cell

        results = {
            "Total Users": total_users,
            "Total Sectors Needed": total_sectors,
            "Required Cells": required_cells
        }

        st.json(results)
        explanation = explain_results("cellular", results)
        st.info(explanation)
