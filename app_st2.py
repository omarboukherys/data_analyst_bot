import re
import os
import json
import pathlib
import streamlit as st
from streamlit_lottie import st_lottie


import os
 
os.environ['OPENAI_API_KEY']= 'xxxxxxxxxxxxxxxxxx' #enter your parameters here
os.environ['OPENAI_API_TYPE']= 'xxxxxxxxxxx' #enter your parameters here
os.environ['OPENAI_API_VERSION']= 'xxxxxxxxxxxxxxxxxxxxxx' #enter your parameters here
os.environ['OPENAI_API_BASE']= "xxxxxxxxxxxxxxxx" #enter your parameters here




 
 
from langchain.chat_models import AzureChatOpenAI
llm = AzureChatOpenAI(
    deployment_name="xxxxxxxxx",
    model_name="xxxxxxxxxxxxxxx"
) #enter your parameters here
 
from langchain.embeddings import OpenAIEmbeddings 
embed = OpenAIEmbeddings(deployment='embedding',model='text-embedding-ada-002')


from sqlalchemy import create_engine

# Database connection parameters
dbname = 'xxxxxxxxxxxxxxxxx' #enter your parameters here
user = 'xxxxxxxxxxxxx' #enter your parameters here
password = 'xxxxxxxxxxxxx' #enter your parameters here
host = 'localhost'  # Default is 'localhost' if running locally
port = '5432'  # Default is '5432'

# Create a connection URL for SQLAlchemy
connection_url = f'postgresql://{user}:{password}@{host}:{port}/{dbname}'

# Create an engine
db_engine = create_engine(connection_url)

# Attempt to connect to the database
try:
    # Open a connection
    connection = db_engine.connect()
    print("Connected to database!")

    # Perform database operations here
    
    # Close the connection (optional, since SQLAlchemy manages it)
    # connection.close()
    # print("Connection closed.")

except Exception as e:
    print("Error connecting to database:", e)






st.set_page_config(
    page_title="DATA AI-Analyst",
    page_icon="✨",
    layout= "wide",
    initial_sidebar_state="expanded",
    menu_items={
    'Get Help': 'https://github.com/omarboukherys',
    'Report a bug': "mailto:omarboukheryspro@gmail.com",
    'About': "## DATA AI-Analyst"
    } )

@st.cache_data()
def lottie_local(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

@st.cache_data()
def hide_footer():
    hide_st_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("DATA AI-Analyst 🚀")


hide_footer()

col1, col2 = st.columns(2)
with col1:
    anim = lottie_local(r"./animation_folder/orange.json")
    st_lottie(anim,
            speed=1,
            reverse=False,
            loop=True,
            height = 500,
            width = 700,
            quality="high",
            key=None)

with col2:
    query = st.text_area("Enter your question", height = 250)
    from langchain.prompts.chat import ChatPromptTemplate

    final_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", 
            """
            You are a helpful AI assistant expert in querying SQL Database to find answers to user's question about Categories, Products and Orders.
            """
            ),
            ("user", "{question}\n ai: "),
        ]
    )

    from langchain.agents import AgentType, create_sql_agent
    from langchain.sql_database import SQLDatabase
    from langchain.agents.agent_toolkits.sql.toolkit import SQLDatabaseToolkit

    db = SQLDatabase(db_engine)

    sql_toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    sql_toolkit.get_tools()

    sqldb_agent = create_sql_agent(
        llm=llm,
        toolkit=sql_toolkit,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

    st.markdown("-----------------------------")

    if st.button("Do The ANALYSIS 💫✨", use_container_width=True):
        with st.spinner("Working.. 💫"):
            try:
                response = sqldb_agent.run(final_prompt.format(question=query))
                st.balloons()
                st.markdown("### Output:")
                st.success(f"{response}")
            except Exception as e:
                st.error(f"Error: {e}")