from langchain import PromptTemplate, LLMChain
from langchain.llms import OpenAI
from secret import openapi_key
import os
import csv

os.environ["OPENAI_API_KEY"] = openapi_key

llm = OpenAI(temperature=0.7)


def generate_test_scenarios(acceptance_criteria):
    # Chain1: to generate test scenarios
    prompt_template_acceptance = PromptTemplate(
        input_variables=['acceptance_criteria'],
        template="Can you generate test scenarios for this user {acceptance_criteria} in a list format."
    )
    scenario_chain = LLMChain(llm=llm, prompt=prompt_template_acceptance, output_key='test_scenarios')

    response = scenario_chain({'acceptance_criteria': acceptance_criteria})

    return response


def generate_test_steps(test_scenario):
    # Chain2: to generate test steps for test scenarios
    prompt_template_steps = PromptTemplate(
        input_variables=['test_scenario'],
        template="Can you generate test steps on how to test the scenario with expected result where all"
                 "test steps are in 1 list and all expected results for each test step are in another list "
                 "{test_scenario}"
    )
    step_chain = LLMChain(llm=llm, prompt=prompt_template_steps, output_key="test_steps")

    response = step_chain({'test_scenario': test_scenario})

    return response["test_steps"]


def generate_test_script(test_scenario, framework=None, lang=None):
    # Chain3: to generate test automation script for test scenarios
    prompt_template_steps = PromptTemplate(
        input_variables=["test_scenario", "framework", "lang"],
        template="Can you generate automation code using {lang} in {framework} for this {test_scenario}"
    )
    prompt_template_steps.format(test_scenario=test_scenario, framework=framework, lang=lang)
    step_chain = LLMChain(llm=llm, prompt=prompt_template_steps, output_key="test_script")
    response = step_chain({'test_scenario': test_scenario, 'framework': framework, 'lang': lang})

    return response


def generate_test_data(test_data_scenario):
    # Chain4: to generate test data for test scenarios
    prompt_template_data = PromptTemplate(
        input_variables=["test_data_scenario"],
        template="generate test data for {test_data_scenario} in a csv format"
    )
    data_chain = LLMChain(llm=llm, prompt=prompt_template_data, output_key="test_data")
    response = data_chain({'test_data_scenario': test_data_scenario})

    return response


