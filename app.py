import streamlit as st
from calculations import wireless_comm, ofdm, link_budget, cellular_design
from ai_agent import explain_results

st.set_page_config(page_title="AI-Powered Wireless Design App", layout="wide")
st.title("📡 AI-Powered Wireless and Mobile Network Design")
st.markdown("""
This web application allows you to simulate and analyze wireless and mobile network scenarios
with the help of an AI agent that explains the results in natural language.

Choose one of the tabs below to get started:
""")

# Tabs for the 4 scenarios
tabs = st.tabs([
    "Wireless Comm System", 
    "OFDM System", 
    "Link Budget", 
    "Cellular Design"
])

# 1. Wireless Communication System
with tabs[0]:
    st.header("Wireless Communication System")
    fs = st.number_input("Sampling Rate (Hz)", min_value=1000.0)
    bits = st.number_input("Bits per Sample", min_value=1)
    src_rate = st.slider("Source Encoder Rate (0-1)", 0.0, 1.0, 0.8)
    ch_rate = st.slider("Channel Encoder Rate (0-1)", 0.0, 1.0, 0.6)
    interleave_ratio = st.number_input("Interleaver Overhead (e.g. 1.1 = 10%)", min_value=1.0, value=1.1)
    burst_ratio = st.number_input("Burst Formatter Overhead", min_value=1.0, value=1.2)

    if st.button("Compute Wireless Comm"):
        results = wireless_comm.compute(fs, bits, src_rate, ch_rate, interleave_ratio, burst_ratio)
        st.write(results)
        explanation = explain_results("wireless_comm", results)
        st.info(explanation)


# 2. OFDM System
with tabs[1]:
    st.header("OFDM System")
    sc_spacing = st.number_input("Subcarrier Spacing (Hz)", value=15000.0)
    num_subcarriers = st.number_input("Number of Subcarriers", value=64)
    bits_per_symbol = st.number_input("Bits per Symbol (modulation)", value=2)
    cp_ratio = st.number_input("Cyclic Prefix Ratio", value=0.1)
    num_rb = st.number_input("Number of Resource Blocks", value=10)

    if st.button("Compute OFDM"):
        results = ofdm.compute(sc_spacing, num_subcarriers, bits_per_symbol, cp_ratio, num_rb)
        st.write(results)
        st.info(explain_results("ofdm", results))

# 3. Link Budget Calculation
with tabs[2]:
    st.header("Link Budget Calculation")
    tx_power = st.number_input("Transmit Power (dBm)", value=30.0)
    tx_gain = st.number_input("Transmitter Gain (dBi)", value=5.0)
    rx_gain = st.number_input("Receiver Gain (dBi)", value=5.0)
    freq_mhz = st.number_input("Frequency (MHz)", value=900.0)
    distance_km = st.number_input("Distance (km)", value=2.0)

    if st.button("Compute Link Budget"):
        results = link_budget.compute(tx_power, tx_gain, rx_gain, freq_mhz, distance_km)
        st.write(results)
        st.info(explain_results("link_budget", results))

# 4. Cellular System Design
with tabs[3]:
    st.header("Cellular System Design")
    area_km2 = st.number_input("Coverage Area (km²)", value=100.0)
    cell_radius_km = st.number_input("Cell Radius (km)", value=1.0)
    reuse_factor = st.number_input("Frequency Reuse Factor", value=3)
    users_per_cell = st.number_input("Users per Cell", value=1000)
    traffic_per_user = st.number_input("Traffic per User (Erlangs)", value=0.02)

    if st.button("Design Cellular System"):
        results = cellular_design.compute(area_km2, cell_radius_km, reuse_factor, users_per_cell, traffic_per_user)
        st.write(results)
        st.info(explain_results("cellular_design", results))
