import os
os.environ["USER_AGENT"] = (
    "Mozilla/5.0 (X11; Linux x86_64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120 Safari/537.36"
)

from langchain_community.document_loaders import WebBaseLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
import os

def summerize(url):
    loader = WebBaseLoader(
        web_path=url,
        header_template={
            "User-Agent": os.environ["USER_AGENT"]
        }
    )
    documents = loader.load()
    prompt = ChatPromptTemplate([
        ("system", "you are a very helpful professional assistent"),
        ("human", "Summerize this given Texts\n\n"
                "Texts:\n{texts}"
        )
    ])
    llm = HuggingFaceEndpoint(
        repo_id='mistralai/Mistral-7B-Instruct-v0.2',
        task = 'text-generation'
    )
    model = ChatHuggingFace(llm=llm)
    parser = StrOutputParser()
    chain = prompt | model | parser
    result = chain.invoke({
        'texts':documents[0].page_content
    })
    return result