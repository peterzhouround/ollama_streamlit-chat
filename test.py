import ollama
import streamlit

print(f"Ollama当前可用的模型有:{ollama.list()}")
print(f"streamlit库的版本是:{streamlit.__version__}")
