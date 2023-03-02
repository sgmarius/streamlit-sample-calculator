import streamlit as st
import pandas as pd
from common.SampleCalculatorLogic.CalculatorLogic import CalculatorLogic


def calculator_page():
    st.markdown("# Sample size calculator")
    st.sidebar.header("Based on the adobe experience league one.")

    confidence_level = st.slider(label="Confidence Level", min_value=0, max_value=100, value=95)
    statistical_power = st.slider(label="Statistical Power", min_value=0, max_value=100, value=80)
    st.slider(
        label="Baseline Conversion Rate (Control Offer)", min_value=0.0, max_value=100.0, value=11.8)
    st.slider(label="Total Number of Daily Visitors", min_value=0, max_value=100000, value=10000)
    st.slider(label="Number of Offers Including Control", min_value=0, max_value=10000, value=5)
    st.slider(label="Lift", min_value=0, max_value=100, value=5)
