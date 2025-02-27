import google.generativeai as genai #libraries import
import streamlit as strlit
import my_key as key #another file thi import karu che

strlit.title("Dhruvi's AI Buddy") #to set the title

genai.configure(api_key=key.My_API_KEY) #to set the API key

model=genai.GenerativeModel("gemini-2.0-flash")#to set the model or llm

prompt=strlit.text_input("Enter your prompt: ") #to set the prompt

if strlit.button("Ask me"):  #set button prompt
    with strlit.spinner(): #set loader to show loading
        reponse=model.generate_content(prompt, stream=True) #generate and display line by line
        for line in reponse:
            strlit.markdown(line.text) # for display in the output file