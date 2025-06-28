import streamlit as st
from calculations.wireless_comm import compute_wireless_comm
from calculations.link_budget import compute_link_budget
from calculations.ofdm import compute_ofdm_parameters
from calculations.cellular_design import compute_cellular_parameters
from ai_agent import explain_results  # Now uses Gemini API

# Streamlit page setup
st.set_page_config(page_title="AI Wireless Design", layout="wide")
st.title("AI-Powered Wireless Communication Design Tool")

# Sidebar tab options
tabs = {
    "Wireless Communication System": "wireless_comm",
    "Link Budget Calculator": "link_budget",
    "OFDM System Parameters": "ofdm",
    "Cellular Network Design": "cellular"
}

# Choose task
page = st.sidebar.radio("Choose a Module", list(tabs.keys()))
task_id = tabs[page]

# Main logic
try:
    if task_id == "wireless_comm":
        st.header("Compute Wireless Communication System")
        sampling_rate = st.number_input("Sampling Rate (Hz)", value=8000)
        quantization_bits = st.number_input("Quantization Bits (bits/sample)", value=8)
        compression_ratio = st.number_input("Source Compression Ratio (e.g., 0.6)", min_value=0.1, max_value=1.0, value=0.6)
        coding_rate = st.number_input("Channel Coding Rate (e.g., 0.7)", min_value=0.1, max_value=1.0, value=0.7)
        interleaver_overhead = st.number_input("Interleaver Overhead (%)", min_value=0.0, value=10.0) / 100
        burst_overhead = st.number_input("Burst Formatter Overhead (%)", min_value=0.0, value=20.0) / 100


        if st.button("Compute Wireless Comm"):
            results = compute_wireless_comm(
                                            sampling_rate,
                                            quantization_bits,
                                            compression_ratio,
                                            coding_rate,
                                            interleaver_overhead,
                                            burst_overhead
                                        )
            if isinstance(results, dict):
                st.json(results)
                explanation = explain_results("wireless_comm", results)
                st.info(str(explanation))
            else:
                st.warning("Results are not in the expected dictionary format.")

    elif task_id == "link_budget":
        st.header("Link Budget Calculator")
        tx_power = st.number_input("Transmitter Power (dBm)", value=30)
        tx_gain = st.number_input("Transmitter Gain (dBi)", value=15)
        rx_gain = st.number_input("Receiver Gain (dBi)", value=12)
        path_loss = st.number_input("Path Loss (dB)", value=100)

        if st.button("Compute Link Budget"):
            results = compute_link_budget(tx_power, tx_gain, rx_gain, path_loss)
            if isinstance(results, dict):
                st.json(results)
                explanation = explain_results("link_budget", results)
                st.info(str(explanation))
            else:
                st.warning("Results are not in the expected dictionary format.")

    elif task_id == "ofdm":
        st.header("OFDM System Parameters")
        bandwidth = st.number_input("Channel Bandwidth (Hz)", value=20000)
        num_subcarriers = st.number_input("Number of Subcarriers", value=64)

        if st.button("Compute OFDM Parameters"):
            results = compute_ofdm_parameters(bandwidth, num_subcarriers)
            if isinstance(results, dict):
                st.json(results)
                explanation = explain_results("ofdm", results)
                st.info(str(explanation))
            else:
                st.warning("Results are not in the expected dictionary format.")

    elif task_id == "cellular":
        st.header("Cellular Network Design")
        area = st.number_input("Total Area (km²)", value=100)
        cell_radius = st.number_input("Cell Radius (km)", value=1)

        if st.button("Compute Cellular Design"):
            results = compute_cellular_parameters(area, cell_radius)
            if isinstance(results, dict):
                st.json(results)
                explanation = explain_results("cellular", results)
                st.info(str(explanation))
            else:
                st.warning("Results are not in the expected dictionary format.")

except ImportError as imp_err:
    st.error(f"Import error detected: {imp_err}")
except Exception as ex:
    st.error(f"Error encountered: {ex}")
