[data_anlyst_bot.webm](https://github.com/omarboukherys/data_analyst_bot/assets/73399025/20dad5b8-c06f-4acf-bcc7-a7f9f04ef668)

# Data Analyst Bot

The Data Analyst Bot is an interactive tool designed for data analysis enthusiasts, providing a seamless experience without requiring any programming language knowledge. With the bot, users can ask questions about their data, receive insights, and explore datasets effortlessly. Whether you're a beginner or an experienced analyst, the Data Analyst Bot is here to assist you in your data exploration journey.

The application was developed using ***LangChain*** Agent (SQL agents) and ***GPT-4*** LLM. The ***GPT-4*** helped us transform user requests into ***SQL*** queries, which the agent then executed. The agent returned the final answer to our query.

## Features

- **Natural Language Interface:** Interact with the bot using everyday language, no need for complex commands or programming.
- **Data Exploration:** Ask questions about your dataset and get instant answers, summaries, and visualizations.
- **Insightful Analysis:** Receive meaningful insights and trends from your data, helping you make informed decisions.
- **User-Friendly:** Designed for ease of use, making data analysis accessible to everyone.

## How to Use

1. **Input your Data:** Upload your dataset to your PostgreSQL database.
2. **Activate the Virtual Environment:** Activate the `ai_env` virtual environment:
   ```bash
   source ai_env/bin/activate  # for Linux/Mac
   ai_env\Scripts\activate      # for Windows
   in your terminal run the following: streamlit run app_st2.py

## NOTE:
In the code, there is a # commentaire to change it if you want to connect to a specific database or schema.

No programming language required, just your curiosity and a desire to explore data. Try the Data Analyst Bot today and unlock the power of your data!
