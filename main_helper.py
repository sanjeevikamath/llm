import streamlit as st
import langchain_helper
import pandas as pd


class MainClass:
    if "test_scenarios" not in st.session_state:
        st.session_state.test_scenarios = "Enter a test scenario"

    if "test_script" not in st.session_state:
        st.session_state.test_script = "Enter a test script"

    if "test_steps" not in st.session_state:
        st.session_state.test_steps = None

    if "temp" not in st.session_state:
        st.session_state.temp = None

    @staticmethod
    def generate_test_scenario(acceptance_criteria=None):
        click = st.button(label="Generate test scenarios")
        if click:
            response = langchain_helper.generate_test_scenarios(acceptance_criteria)
            st.session_state.test_scenarios = response["test_scenarios"]
        edit = st.checkbox(label="edit scenarios")
        if edit:
            edited_scenarios = st.text_area("Edit Test Scenarios", st.session_state.test_scenarios)
            st.session_state.test_scenarios = edited_scenarios

    @staticmethod
    def display_test_scenarios():
        if hasattr(st.session_state, "test_scenarios"):
            st.header("***Test Scenarios***")
            st.write(st.session_state.test_scenarios)

    @staticmethod
    def generate_test_case(test_scenario):
        click_test_steps = st.button(label="Generate test steps")
        if click_test_steps:
            response1 = langchain_helper.generate_test_steps(test_scenario)
            st.session_state.temp = response1
            st.header("***Test Steps***")
            test_steps, expected_results = response1.split("Expected Results:")
            test_steps = test_steps.replace("Test Steps:", "").strip().split("\n")
            expected_results = expected_results.replace("Expected Results:", "").strip().split("\n")
            df = pd.DataFrame({'Test Step': test_steps, 'Expected Result': expected_results})
            st.session_state.test_steps = df
        edit = st.checkbox(label="edit test steps")
        if edit:
            edited_steps = st.text_area("Edit Test Steps", st.session_state.temp)
            test_steps, expected_results = edited_steps.split("Expected Results:")
            test_steps = test_steps.replace("Test Steps:", "").strip().split("\n")
            expected_results = expected_results.replace("Expected Results:", "").strip().split("\n")
            df = pd.DataFrame({'Test Step': test_steps, 'Expected Result': expected_results})
            st.session_state.test_steps = df

    @staticmethod
    def display_test_steps():

        st.table(st.session_state.test_steps)
        if hasattr(st.session_state.test_steps, "test_steps"):
            download = st.download_button(label="Download test steps",
                                          data=st.session_state.test_steps.to_csv().encode('utf-8'),
                                          file_name='test_steps.csv')

    @staticmethod
    def generate_test_data(test_data_scenario):
        click_data = st.button(label="Generate test data for scenario")
        if click_data:
            response_data = langchain_helper.generate_test_data(test_data_scenario)
            st.write(response_data["test_data"])
            download_data = st.download_button(label="Download test data", data=response_data["test_data"],
                                               file_name="test_data.csv")

    @staticmethod
    def generate_automation_script(test_scenario, lang_dropdown):
        if lang_dropdown == 'Java':
            framework_dropdown = st.selectbox('Which framework you want to automate?', ('Testng',))
        elif lang_dropdown == 'python':
            framework_dropdown = st.selectbox('Which framework you want to automate?', ('Pytest', 'Robot'))
        click_test_script = st.button(label="Generate test automation script")
        if click_test_script:
            response2 = langchain_helper.generate_test_script(test_scenario, framework=framework_dropdown,
                                                              lang=lang_dropdown)
            st.session_state.test_script = response2["test_script"]
        edit = st.checkbox(label="edit test script")
        if edit:
            edited_script = st.text_area("Edit Test Script", st.session_state.test_script)
            st.session_state.test_script = edited_script

    @staticmethod
    def display_test_script(lang_dropdown):
        if hasattr(st.session_state, "test_script"):
            st.header("***Test Automation Script***")
            st.code(st.session_state.test_script, language=lang_dropdown)
