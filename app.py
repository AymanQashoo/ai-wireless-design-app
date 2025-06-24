import streamlit as st
from calculations.wireless_comm import compute_wireless_comm
from calculations.link_budget import compute_link_budget
from calculations.ofdm import compute_ofdm_parameters
from calculations.cellular_design import compute_cellular_parameters
from ai_agent import explain_results

st.set_page_config(page_title="AI Wireless Design", layout="wide")

st.title("📡 AI-Powered Wireless and Mobile Networks Calculator")

tab1, tab2, tab3, tab4 = st.tabs(["Wireless Comm", "Link Budget", "OFDM", "Cellular"])

# Wireless Communication Tab
with tab1:
    st.header("Digital Wireless Communication System")
    sampling_rate = st.number_input("Sampler Output Rate (Hz)", min_value=1, value=8000)
    bits_per_sample = st.number_input("Quantizer Output Rate (bps)", min_value=1, value=64000)
    source_encoder_rate = st.number_input("Source Encoder Output Rate (bps)", min_value=1, value=38400)
    channel_encoder_rate = st.slider("Channel Encoder Output Rate (%)", min_value=0, max_value=100, value=80)
    interleaver_overhead = st.slider("Interleaver Overhead (%)", min_value=0, max_value=100, value=10)
    burst_formatter_overhead = st.slider("Burst Formatter Overhead (%)", min_value=0, max_value=100, value=20)

    if st.button("Compute Wireless Comm"):
        results = compute_wireless_comm(
            sampling_rate,
            bits_per_sample,
            source_encoder_rate,
            channel_encoder_rate,
            interleaver_overhead,
            burst_formatter_overhead
        )

        if results:
            try:
                if isinstance(results, dict):
                    st.json(results)
                    explanation = explain_results("wireless_comm", results)
                    st.info(explanation)
                else:
                    st.write(results)
                    st.warning("Note: Output is not a dictionary.")
            except Exception as e:
                st.error(f"An error occurred while displaying results: {e}")
        else:
            st.error("Computation failed. Please check input values.")




# Link Budget Tab
with tab2:
    st.header("Link Budget Calculation")
    tx_power = st.number_input("Transmitted Power (dBm)", value=30)
    tx_gain = st.number_input("Transmitter Antenna Gain (dBi)", value=15)
    rx_gain = st.number_input("Receiver Antenna Gain (dBi)", value=12)
    path_loss = st.number_input("Path Loss (dB)", value=100)

    if st.button("Compute Link Budget"):
        results = compute_link_budget(tx_power, tx_gain, rx_gain, path_loss)
        st.json(results)
        explanation = explain_results("link_budget", results)
        st.info(explanation)

# OFDM Tab
with tab3:
    st.header("OFDM System Parameters")
    bandwidth = st.number_input("System Bandwidth (Hz)", value=20_000_000)
    num_subcarriers = st.number_input("Number of Subcarriers", value=64)
    cp_duration = st.number_input("Cyclic Prefix Duration (us)", value=4.0)

    if st.button("Compute OFDM Parameters"):
        results = compute_ofdm_parameters(bandwidth, num_subcarriers, cp_duration)
        st.json(results)
        explanation = explain_results("ofdm", results)
        st.info(explanation)

# Cellular Design Tab
with tab4:
    st.header("Cellular Network Design")
    cell_radius = st.number_input("Cell Radius (km)", value=1.0)
    freq_reuse = st.number_input("Frequency Reuse Factor (N)", value=7)
    num_channels = st.number_input("Total Number of Channels", value=350)

    if st.button("Compute Cellular Design"):
        results = compute_cellular_parameters(cell_radius, freq_reuse, num_channels)
        st.json(results)
        explanation = explain_results("cellular_design", results)
        st.info(explanation)
