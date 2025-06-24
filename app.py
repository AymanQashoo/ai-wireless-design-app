import streamlit as st
from calculations.wireless_comm import compute_wireless_comm
from calculations.link_budget import compute_link_budget
from calculations.ofdm import compute_ofdm_parameters
from calculations.cellular_design import compute_cellular_parameters
from ai_agent import explain_results

st.set_page_config(page_title="AI Wireless Design", layout="wide")
st.title("📡 AI-Powered Wireless Communication Design Tool")

# Sidebar for navigation
tabs = {
    "Wireless Communication System": "wireless_comm",
    "Link Budget Calculator": "link_budget",
    "OFDM System Parameters": "ofdm",
    "Cellular Network Design": "cellular"
}
page = st.sidebar.radio("Choose a Module", list(tabs.keys()))
task_id = tabs[page]

# Input + Computation Handling
if task_id == "wireless_comm":
    st.header("Compute Wireless Comm")
    try:
        sampler_rate = st.number_input("Sampler Output Rate (Hz)", value=8000)
        quantizer_rate = st.number_input("Quantizer Output Rate (bps)", value=64000)

        if st.button("Compute Wireless Comm"):
            results = compute_wireless_comm(sampler_rate, quantizer_rate)
            if isinstance(results, dict):
                st.json(results)
                try:
                    explanation = explain_results("wireless_comm", results)
                    st.info(explanation)
                except Exception as e:
                    st.warning(f"AI explanation error: {e}")
            else:
                st.write(results)
    except Exception as e:
        st.error(f"Error: {e}")

elif task_id == "link_budget":
    st.header("Link Budget Calculator")
    try:
        tx_power = st.number_input("Transmitter Power (dBm)", value=30)
        tx_gain = st.number_input("Transmitter Gain (dBi)", value=15)
        rx_gain = st.number_input("Receiver Gain (dBi)", value=12)
        path_loss = st.number_input("Path Loss (dB)", value=100)

        if st.button("Compute Link Budget"):
            results = compute_link_budget(tx_power, tx_gain, rx_gain, path_loss)
            if isinstance(results, dict):
                st.json(results)
                try:
                    explanation = explain_results("link_budget", results)
                    st.info(explanation)
                except Exception as e:
                    st.warning(f"AI explanation error: {e}")
            else:
                st.write(results)
    except Exception as e:
        st.error(f"Error: {e}")

elif task_id == "ofdm":
    st.header("OFDM System Parameters")
    try:
        bandwidth = st.number_input("Channel Bandwidth (Hz)", value=20000)
        num_subcarriers = st.number_input("Number of Subcarriers", value=64)

        if st.button("Compute OFDM Parameters"):
            results = compute_ofdm_parameters(bandwidth, num_subcarriers)
            if isinstance(results, dict):
                st.json(results)
                try:
                    explanation = explain_results("ofdm", results)
                    st.info(explanation)
                except Exception as e:
                    st.warning(f"AI explanation error: {e}")
            else:
                st.write(results)
    except Exception as e:
        st.error(f"Error: {e}")

elif task_id == "cellular":
    st.header("Cellular Network Design")
    try:
        area = st.number_input("Total Area (km²)", value=100)
        cell_radius = st.number_input("Cell Radius (km)", value=1)

        if st.button("Compute Cellular Design"):
            results = compute_cellular_parameters(area, cell_radius)
            if isinstance(results, dict):
                st.json(results)
                try:
                    explanation = explain_results("cellular", results)
                    st.info(explanation)
                except Exception as e:
                    st.warning(f"AI explanation error: {e}")
            else:
                st.write(results)
    except Exception as e:
        st.error(f"Error: {e}")
