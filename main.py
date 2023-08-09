import streamlit as st
from main_helper import MainClass

st.title("Test Case Generator")
acceptance_criteria = st.text_input(label="User Acceptance Criteria", value="")
# Test method to generate test scenarios
MainClass.generate_test_scenario(acceptance_criteria)
MainClass.display_test_scenarios()
test_scenario = st.text_input(label="enter test scenario", value="")
# Test method to generate test steps and download
MainClass.generate_test_case(test_scenario=test_scenario)
MainClass.display_test_steps()
# Test method to generate test data and download it
test_data_scenario = st.text_input(label="Enter kind of data user needs", value="")
MainClass.generate_test_data(test_data_scenario)
# Test method to choose an automation language famework and generate an automation script
lang_dropdown = st.selectbox('Which automation language you choose?', ('python', 'Java'))
MainClass.generate_automation_script(test_scenario, lang_dropdown)
MainClass.display_test_script(lang_dropdown)
