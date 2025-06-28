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
    bandwidth = st.number_input("Bandwidth (Hz)", value=20000000)
    fft_size = st.number_input("FFT Size", value=1024)
    cyclic_prefix_ratio = st.number_input("Cyclic Prefix Ratio", 0.0, 1.0, 0.25)
    modulation_order = st.number_input("Modulation Order (bits per symbol)", value=4)
    num_resource_blocks = st.number_input("Number of Resource Blocks", value=50)
    symbols_per_slot = st.number_input("Symbols per Slot", value=14)

    if st.button("Compute OFDM Parameters"):
        results = compute_ofdm_parameters(
            bandwidth, fft_size, cyclic_prefix_ratio,
            modulation_order, num_resource_blocks, symbols_per_slot)
        st.json(results)
        st.info(explain_results("ofdm", results))

elif task_id == "link_budget":
    st.header("Link Budget Calculator")
    tx_power = st.number_input("Transmitter Power (dBm)", value=40)
    tx_gain = st.number_input("Transmitter Gain (dBi)", value=18)
    rx_gain = st.number_input("Receiver Gain (dBi)", value=12)
    distance_km = st.number_input("Distance (km)", value=5.0)
    frequency_mhz = st.number_input("Frequency (MHz)", value=2400)
    path_loss_exponent = st.number_input("Path Loss Exponent", value=3.0)

    if st.button("Compute Link Budget"):
        results = compute_link_budget(
            tx_power, tx_gain, rx_gain,
            distance_km, frequency_mhz, path_loss_exponent)
        st.json(results)
        st.info(explain_results("link_budget", results))

elif task_id == "cellular":
    st.header("Cellular Network Design")
    area = st.number_input("Total Area (km²)", value=150)
    cell_radius = st.number_input("Cell Radius (km)", value=1.0)
    cluster_size = st.number_input("Cluster Size", value=7)
    user_density = st.number_input("User Density (users/km²)", value=500)
    bandwidth_per_cell = st.number_input("Bandwidth per Cell (MHz)", value=5.0)
    traffic_per_user = st.number_input("Traffic per User (Erlang)", value=0.02)
    gos = st.number_input("Grade of Service (%)", value=2.0)

    if st.button("Compute Cellular Design"):
        results = compute_cellular_parameters(
            area, cell_radius, cluster_size,
            user_density, bandwidth_per_cell,
            traffic_per_user, gos)
        st.json(results)
        st.info(explain_results("cellular", results))
