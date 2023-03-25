import streamlit as st
import pandas as pd
from common.SampleCalculatorLogic.CalculatorLogic import CalculatorLogic


def calculator_page():
    col1, col2, col3 = st.columns(3)

    with col1:
        confidence_level = st.number_input(
            label="Confidence Level (%)", 
            min_value=0, max_value=100, value=95)

        number_of_visitors = st.number_input(
            label="Total Number of Daily Visitors", 
            min_value=0, max_value=100000, value=10000)

    with col2:
        statistical_power = st.number_input(
            label="Statistical Power (%)", 
            min_value=0, max_value=100, value=80)

        number_of_offers = st.number_input(
            label="Number of Offers Including Control", 
            min_value=0, max_value=10000, value=5)

    with col3:
        baseline_conv_rate = st.number_input(
            label="Baseline Conversion Rate (%)",
            min_value=0.0,max_value=100.0, value=11.8)

        lift = st.number_input(
            label="Lift (%)", 
            min_value=0, max_value=100, value=5)

    calculator = CalculatorLogic({
        "statistical_power": statistical_power/100,
        "confidence_level": confidence_level/100,
        "baseline_conversion_rate": baseline_conv_rate/100,
        "lift": lift/100,
        "daily_visitors": number_of_visitors,
        "number_of_offers": number_of_offers
    })

    st.number_input(
        label="Absolute Difference in Conversion Rate (that can be detected with power (80%) probability)",
        value=calculator.outputs.get('absolute_difference_conversion_rate')
    )

    st.number_input(
        label="Conversion Rate of Alternative (that can be detected with power (80%) probability)",
        value=calculator.outputs.get('rate_alternative')
    )

    st.number_input(
        label="Sample Size per Offer (# of visitors)",
        value=calculator.outputs.get('sample_size_offer_visitors')
    )
    
    st.number_input(
        label="Sample Size per Offer (# of conversions)",
        value=calculator.outputs.get('sample_size_offer_conversion')
    )

    st.number_input(
        label="Days to Complete Test",
        value=calculator.outputs.get('days_to_complete_test')
    )