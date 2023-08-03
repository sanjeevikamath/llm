import streamlit as st
import langchain_helper
import pandas as pd

st.title("Test Case Generator")
acceptance_criteria = st.text_input(label="user acceptance criteria", value="")
click = st.button(label="Generate test scenarios")

if click:
    response = langchain_helper.generate_test_scenarios(acceptance_criteria)
    st.header("***Test Scenarios***")
    st.write(response["test_scenarios"])

test_scenario = st.text_input(label="enter test scenario", value="")
click_test_steps = st.button(label="Generate test steps")

if click_test_steps:
    response1 = langchain_helper.generate_test_steps(test_scenario)
    st.header("***Test Steps***")
    test_steps, expected_results = response1.split("Expected Results:")
    test_steps = test_steps.replace("Test Steps:", "").strip().split("\n")
    expected_results = expected_results.replace("Expected Results:", "").strip().split("\n")
    df = pd.DataFrame({'Test Step': test_steps, 'Expected Result': expected_results})
    st.table(df)
    download = st.download_button(label="Download test steps", data=df.to_csv().encode('utf-8'),
                                  file_name='test_steps.csv')

test_data_scenario = st.text_input(label="Enter kind of data user needs", value="")
print(test_data_scenario)
click_data = st.button(label="Generate test data for scenario")
if click_data:
    response_data = langchain_helper.generate_test_data(test_data_scenario)
    st.write(response_data["test_data"])
   # my_list = response_data["test_data"]
   # df = pd.DataFrame(my_list[1:])
    download_data = st.download_button(label="Download test data", data=response_data["test_data"],
                                       file_name="test_data.csv")

lang_dropdown = st.selectbox('Which automation language you choose?', ('python', 'Java'))
if lang_dropdown == 'Java':
    framework_dropdown = st.selectbox('Which framework you want to automate?', ('Testng',))
elif lang_dropdown == 'python':
    framework_dropdown = st.selectbox('Which framework you want to automate?', ('Pytest', 'Robot'))
click_test_script = st.button(label="Generate test automation script")
if click_test_script:
    response2 = langchain_helper.generate_test_script(test_scenario, framework=framework_dropdown, lang=lang_dropdown)
    st.header("***Test Automation Script***")
    st.code(response2["test_script"], language=lang_dropdown)
