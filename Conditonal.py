import os
from dotenv import load_dotenv
from typing import TypedDict, Annotated
from langchain_mistralai import ChatMistralAI
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START , END 
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()


embeddings = HuggingFaceEmbeddings(model_name ="sentence-transformers/all-MiniLM-L6-v2")


def build_retriever(pdf_path : str):
    loader = PyPDFLoader(pdf_path)
    document = loader.load()


    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 800,
        chunk_overlap = 100
    )

    chunks = splitter.split_documents(document)
    vectorstore = FAISS.from_documents(chunks,embeddings)

    return vectorstore.as_retriever(search_kwargs = {"k":4})


oops_pdf = build_retriever("Object Oriented Programming (1) (1).pdf")
cn_pdf = build_retriever("Computer Networking Notes for Tech Placements (1).pdf")
os_pdf =build_retriever("Operating System Notes.pdf")
dbms_pdf = build_retriever("DBMS_Notes (2).pdf")

llm = ChatMistralAI(model="mistral-small-2506",temperature=0.5)

class State(TypedDict):
    programme : str
    messages : Annotated[list,add_messages]
    query_type : str
    retrieved_context : str


def classifier_node(state:State) ->  dict:

    last_message = state['messages'][-1].content
   
    prompt = (
    "Classify the following technical interview question into exactly one category: "
    "'oops', 'os', 'cn', or 'dbms'.\n\n"

    "Use 'oops' for questions about classes, objects, inheritance, polymorphism, "
    "encapsulation, abstraction, constructors, interfaces, method overloading, "
    "method overriding, object-oriented principles, or design patterns.\n"

    "Use 'os' for questions about processes, threads, CPU scheduling, deadlocks, "
    "memory management, paging, segmentation, virtual memory, synchronization, "
    "file systems, or operating system concepts.\n"

    "Use 'cn' for questions about the OSI model, TCP/IP, HTTP, HTTPS, DNS, "
    "IP addressing, routing, switching, sockets, network security, or communication protocols.\n"

    "Use 'dbms' for questions about SQL, normalization, transactions, ACID properties, "
    "joins, indexing, keys, ER diagrams, database design, concurrency control, "
    "or query optimization.\n\n"

    f"Question: {last_message}\n\n"

    "Return only one word: oops, os, cn, or dbms."
    )

    response = llm.invoke(prompt)
    category = response.content.strip().lower()
    
    if "oops" in category:
        category = "oops"
    elif "os" in category:
        category = "os"
    elif "cn" in category:
        category = "cn"
    else:
        category = "dbms"

    return {"query_type":category}

def oops_node(state:State) -> dict:
    query = state["messages"][-1].content
    docs = oops_pdf.invoke(query)
    context = "\n\n".join([doc.page_content for doc in docs])
    return {"retrieved_context":context}

def cn_node(state:State) -> dict:
    query = state["messages"][-1].content
    docs = cn_pdf.invoke(query)
    context = "\n\n".join([doc.page_content for doc in docs])
    return {"retrieved_context":context}

def os_node(state:State) -> dict:
    query = state["messages"][-1].content
    docs = os_pdf.invoke(query)
    context = "\n\n".join([doc.page_content for doc in docs])
    return {"retrieved_context":context}

def dbms_node(state:State) -> dict:
    query = state["messages"][-1].content
    docs = dbms_pdf.invoke(query)
    context = "\n\n".join([doc.page_content for doc in docs])
    return {"retrieved_context":context}
    

def none_node(state:State) -> dict:
    return {"retrieved_context":"NO_RETRIEVAL_NEEDED"}


def response_node(state:State) -> dict:
    query = state["messages"][-1].content
    programme = state.get("programme","unknown")
    context = state["retrieved_context"]

    if context == "NO_RETRIEVAL_NEEDED":
        prompt = (
            f"You are a friendly Teacher assistant talking to a {programme} student. "
            f"Answer this question using your own general knowledge:\n\n{query}"
        )
    
    else:
        prompt = (
            f"You are a AI Teacher assistant helping a {programme} student. "
            f"Use the following context from the documents to answer "
            f"the question accurately. If the context mentions specific figures for "
            f"different programmes, highlight the one relevant to {programme} if possible.\n\n"
            f"Context:\n{context}\n\n"
            f"Question: {query}\n\n"
            f"Give a clear, friendly, and precise answer."
        )

    response = llm.invoke(prompt)
    return {"messages":[("ai",response.content.strip())]}



def route_query(state:State):
    if state['query_type'] == "oops":
        return "oops_node"
    elif state["query_type"] == "os":
        return "os_node"
    elif state["query_type"] == "cn":
        return "cn_node"
    else:
        return "dbms_node"
    


graph = StateGraph(State)

graph.add_node("classifier",classifier_node)
graph.add_node("oops_node",oops_node)
graph.add_node("os_node",os_node)
graph.add_node("cn_node",cn_node)
graph.add_node("dbms_node",dbms_node)
graph.add_node("response",response_node)


graph.add_edge(START,"classifier")
graph.add_conditional_edges("classifier",route_query)

graph.add_edge("oops_node","response")
graph.add_edge("os_node","response")
graph.add_edge("cn_node","response")
graph.add_edge("dbms_node","response")
graph.add_edge("response",END)

app = graph.compile()

print("Welcome to the Techincal Interview Prep ")

print("Which subject you want to ask the questions")
print("1.OOPS")
print("2.OS")
print("3.CN")
print("4.DBMS")

choice = input("\n Enter 1,2,3 or 4")

programme_map = {
    "1":"OOPs",
    "2":"OS",
    "3":"CN",
    "4":"DBMS"
}

choice = programme_map.get(choice,"OOPS")

print(f"\nGreat! You can ask {choice} Techincal Question.")

while True:
    user_query = input("You:  ")

    if user_query.lower() in ["exit","quit"]:
        break
    
    result = app.invoke({
        "programme": choice,
        "messages": [("human",user_query)]
    })

    print(f"Assistant : {result['messages'][-1].content}")