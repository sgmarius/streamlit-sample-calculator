import streamlit as st
from apps.SampleSizeCalculator.home import home_page
from apps.SampleSizeCalculator.pages.calculator import calculator_page


home, calculator = st.tabs(["Home", "Calculator"])

with home:
   st.header("Home page")
   home_page()

with calculator:
   st.header("Calculator")
   calculator_page()