import streamlit as st
from calculations.wireless_comm import compute_wireless_comm
from calculations.ofdm import compute_ofdm_parameters
from calculations.link_budget import compute_link_budget
from calculations.cellular_design import compute_cellular_design
from ai_agent import explain_results

st.set_page_config(page_title="Wireless Communication App", layout="wide")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["Wireless Comm System", "OFDM System", "Link Budget", "Cellular Design"])

# Tab 1 - Wireless Communication System
with tab1:
    st.title("Wireless Communication System")
    
    sampling_rate = st.number_input("Sampling Rate (Hz)", value=1000.0)
    bits_per_sample = st.number_input("Bits per Sample", value=1)
    source_encoder_rate = st.slider("Source Encoder Rate (0-1)", 0.0, 1.0, 0.8)
    channel_encoder_rate = st.slider("Channel Encoder Rate (0-1)", 0.0, 1.0, 0.6)
    interleaver_overhead = st.number_input("Interleaver Overhead (e.g. 1.1 = 10%)", value=1.1)
    burst_formatter_overhead = st.number_input("Burst Formatter Overhead", value=1.2)

    if st.button("Compute Wireless Comm"):
        results = compute_wireless_comm(sampling_rate, bits_per_sample, source_encoder_rate,
                                        channel_encoder_rate, interleaver_overhead, burst_formatter_overhead)
        st.json(results)

        explanation = explain_results("wireless_comm", results)
        st.info(explanation)

# Tab 2 - OFDM System
with tab2:
    st.title("OFDM System")
    
    total_bandwidth = st.number_input("Total Bandwidth (Hz)", value=20000.0)
    subcarrier_spacing = st.number_input("Subcarrier Spacing (Hz)", value=15.0)
    cp_length = st.number_input("Cyclic Prefix Length (samples)", value=16)

    if st.button("Compute OFDM"):
        results = compute_ofdm_parameters(total_bandwidth, subcarrier_spacing, cp_length)
        st.json(results)

        explanation = explain_results("ofdm", results)
        st.info(explanation)

# Tab 3 - Link Budget
with tab3:
    st.title("Link Budget Calculator")

    tx_power = st.number_input("Transmit Power (dBm)", value=30.0)
    tx_gain = st.number_input("Transmit Antenna Gain (dBi)", value=14.0)
    rx_gain = st.number_input("Receive Antenna Gain (dBi)", value=14.0)
    path_loss = st.number_input("Path Loss (dB)", value=100.0)
    other_losses = st.number_input("Other Losses (dB)", value=2.0)

    if st.button("Compute Link Budget"):
        results = compute_link_budget(tx_power, tx_gain, rx_gain, path_loss, other_losses)
        st.json(results)

        explanation = explain_results("link_budget", results)
        st.info(explanation)

# Tab 4 - Cellular Design
with tab4:
    st.title("Cellular Network Design")

    area_km2 = st.number_input("Total Area (km²)", value=100.0)
    cell_radius_km = st.number_input("Cell Radius (km)", value=1.0)
    users_per_cell = st.number_input("Users per Cell", value=1000)
    spectral_efficiency = st.number_input("Spectral Efficiency (bps/Hz)", value=2.0)
    bandwidth_mhz = st.number_input("Bandwidth (MHz)", value=10.0)

    if st.button("Compute Cellular Design"):
        results = compute_cellular_design(area_km2, cell_radius_km, users_per_cell, spectral_efficiency, bandwidth_mhz)
        st.json(results)

        explanation = explain_results("cellular_design", results)
        st.info(explanation)
