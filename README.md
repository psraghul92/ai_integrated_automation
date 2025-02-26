# **UI Automation Framework Powered By AI**

**Language:** Python-3.12

**Tools:** [browser-use](https://docs.browser-use.com/introduction), [langchain-google-genai](https://pypi.org/project/langchain-google-genai/)

**LLM:** gemini-2.0-flash-exp

**Test Framework:** pytest

**Report:** allure 

This is  POC project to explore AI capabilities in UI automation testing

## How to run the tests

1. Clone the repository
2. Install the dependencies in `requirements.txt`
3. Install playwright using `playwright install`
4. Add the LLM API_KEY in the system environment variable (Here the variable is names as `GEMINI_API_KEY`)

To run the tests, use the following command:

`pytest -v -s --alluredir=allure-results`


After the test Run is completed, you can generate the allure report using the following command:

`allure serve allure-results`

**GIF File generated by browser-use for a successful transaction Testcase**

![b474412e-bb4c-4a80-81c6-0a219f2d6be2-attachment](https://github.com/user-attachments/assets/48d27f47-eae6-404d-a9d5-42890e876883)
