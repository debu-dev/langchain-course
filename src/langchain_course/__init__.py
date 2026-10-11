from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

load_dotenv()


def main() -> None:
    print("Hello from langchain-course!")
    info = """
   Amazon Quick is a comprehensive, generative AI-powered business intelligence platform that makes it easy to analyze data, create visualizations, automate workflows, and collaborate across your organization. The service combines traditional business intelligence capabilities with modern AI assistance, requiring no machine learning expertise to use. You can connect to diverse data sources, create interactive dashboards, build intelligent automations, and get immediate insights through natural language conversations with AI agents.
    """

    summary_template = PromptTemplate(
        input_variables=["text"], template="Provide more information on the following text in json token optimised format: {text}"
    )

    llm = ChatOllama(temperature=1, model="gemma3", base_url="http://localhost:11434")
    chain = summary_template | llm
    result = chain.invoke({"text": info})
    print(result.content)


if __name__ == "__main__":
    main()
