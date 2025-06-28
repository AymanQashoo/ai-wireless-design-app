import streamlit as st
from calculations.wireless_comm import compute_wireless_comm
from calculations.link_budget import compute_link_budget
from calculations.ofdm import compute_ofdm_parameters
from calculations.cellular_design import compute_cellular_parameters
from ai_agent import explain_results

st.set_page_config(page_title="AI Wireless Design", layout="wide")
st.title("AI-Powered Wireless Communication Design Tool")

tabs = {
    "Wireless Communication System": "wireless_comm",
    "Link Budget Calculator": "link_budget",
    "OFDM System Parameters": "ofdm",
    "Cellular Network Design": "cellular"
}

page = st.sidebar.radio("Choose a Module", list(tabs.keys()))
task_id = tabs[page]

if task_id == "wireless_comm":
    st.header("Wireless Communication System")

    bandwidth_khz = st.number_input("Signal Bandwidth (kHz)", value=8000)
    quantization_bits = st.number_input("Quantization Bits", value=8)
    source_ratio = st.number_input("Source Encoder Ratio (Rs)", min_value=0.0, max_value=1.0, value=0.5)
    channel_ratio = st.number_input("Channel Encoder Ratio (Rc)", min_value=0.0, max_value=1.0, value=0.75)
    modulation_type = st.selectbox("Modulation Type", ["QPSK", "16-QAM", "64QAM"], index=0)

    if st.button("Calculate"):
        results = compute_wireless_comm(
            bandwidth_khz,
            quantization_bits,
            source_ratio,
            channel_ratio,
            modulation_type
        )
        if isinstance(results, dict):
            st.json(results)
            explanation = explain_results("wireless_comm", results)
            st.info(str(explanation))
        else:
            st.warning("Results are not in the expected dictionary format.")



elif task_id == "ofdm":
    st.header("OFDM System Parameters")

    rb_bandwidth_khz = st.number_input("Resource Block (RB) Bandwidth (kHz)", value=180)
    subcarrier_spacing_khz = st.number_input("Subcarrier Spacing (kHz)", value=15)
    num_symbols_per_rb = st.number_input("Number of OFDM Symbols per RB", value=14)
    rb_duration_ms = st.number_input("RB Duration (ms)", value=1.0)
    modulation_type = st.selectbox("Modulation Type", ["QPSK", "16-QAM", "64-QAM", "1024-QAM"])
    parallel_blocks = st.number_input("Parallel Transmission Blocks", value=100)

    if st.button("Calculate OFDM Parameters"):
        results = compute_ofdm_parameters(
            rb_bandwidth_khz,
            subcarrier_spacing_khz,
            num_symbols_per_rb,
            rb_duration_ms,
            modulation_type,
            parallel_blocks
        )

        if isinstance(results, dict):
            st.json(results)
            explanation = explain_results("ofdm", results)
            st.info(str(explanation))
        else:
            st.warning("Results are not in the expected dictionary format.")


elif task_id == "link_budget":
    st.header("Link Budget Calculator")

    tx_power_dbm = st.number_input("Transmitted Power (dBm)", value=30)
    tx_gain_dbi = st.number_input("Transmitter Antenna Gain (dBi)", value=15)
    rx_gain_dbi = st.number_input("Receiver Antenna Gain (dBi)", value=12)
    distance_km = st.number_input("Distance (km)", value=2.0)
    frequency_mhz = st.number_input("Frequency (MHz)", value=2400)
    system_losses_db = st.number_input("System Losses (dB)", value=3.0)

    if st.button("Compute Link Budget"):
        results = compute_link_budget(
            tx_power_dbm,
            tx_gain_dbi,
            rx_gain_dbi,
            distance_km,
            frequency_mhz,
            system_losses_db
        )
        if isinstance(results, dict):
            st.json(results)
            explanation = explain_results("link_budget", results)
            st.info(str(explanation))
        else:
            st.warning("Results are not in the expected dictionary format.")



elif task_id == "cellular":
    st.header("Cellular Network Design")

    total_bandwidth = st.number_input("Total Bandwidth (MHz)", value=25.0)
    channel_bandwidth = st.number_input("Channel Bandwidth (MHz)", value=0.2)
    num_cells = st.number_input("Number of Cells", value=50)
    cell_radius = st.number_input("Cell Radius (km)", value=1.0)
    reuse_factor = st.number_input("Reuse Factor (N)", value=7)
    distance = st.number_input("Distance for Layout (km)", value=10.0)

    if st.button("Calculate Cellular Design"):
        results = compute_cellular_parameters(
            total_bandwidth,
            channel_bandwidth,
            num_cells,
            cell_radius,
            reuse_factor,
            distance
        )
        if isinstance(results, dict):
            st.json(results)
            explanation = explain_results("cellular", results)
            st.info(str(explanation))
        else:
            st.warning("Results are not in the expected dictionary format.")

