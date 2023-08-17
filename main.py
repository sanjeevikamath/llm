import streamlit as st
from main_helper import MainClass
import os
import requests
from requests.auth import HTTPBasicAuth


# login page code
def login_page():
    st.title("Open AI key")
    key = st.text_input("Open AI key", type="password")
    os.environ["OPENAI_API_KEY"] = key
    st.title("Jira Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:

        #auth_response = authenticate_with_jira(username, password)
        response = jira_project(username, password)
        if response.status_code == 200:

        #if auth_response.status_code == 200:
            #auth_token = auth_response.json().get("token")

            st.session_state.auth_token = "1"
            st.success("Login successful!")
            st.session_state.logged_in = True
            st.experimental_rerun()


def main_app():

    st.title("Test Case Generator")
    acceptance_criteria = st.text_input(label="User Acceptance Criteria", value="")
    # Test method to generate test scenarios
    mc = MainClass()
    mc.generate_test_scenario(acceptance_criteria)
    mc.display_test_scenarios()
    test_scenario = st.text_input(label="enter test scenario", value="")
    # Test method to generate test steps and download
    mc.generate_test_case(test_scenario=test_scenario)
    mc.display_test_steps()
    # Test method to generate test data and download it
    test_data_scenario = st.text_input(label="Enter kind of data user needs", value="")
    mc.generate_test_data(test_data_scenario)
    # Test method to choose an automation language famework and generate an automation script
    lang_dropdown = st.selectbox('Which automation language you choose?', ('python', 'Java'))
    mc.generate_automation_script(test_scenario, lang_dropdown)
    mc.display_test_script(lang_dropdown)

# if we get Jira API for authorization this can be used/moved to jira helper file
# def authenticate_with_jira(username, password):
#     auth_url = "https://jira.tools.deloitteinnovation.us/rest/api/2/project"
#     payload = {
#         "username": username,
#         "password": password
#     }
#     response = requests.post(auth_url, json=payload)
#     return response

#workaround to test login until authorization api is available
def jira_project(username, password):
    url = "https://jira.tools.deloitteinnovation.us/rest/api/2/project"

    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.get(url, headers=headers, auth=HTTPBasicAuth(username, password))
    print(response.status_code)
    print(response.json())
    return response




