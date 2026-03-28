import streamlit as st
import time
import ollama

# Ollama获取客户端
# client = ollama.Client(host="http://local:11434")

# session_state保存历史会话
# 初始化
if "message" not in st.session_state:
    st.session_state["message"] = []

# 标题
st.title("智能Agent")

# 分隔符
st.divider()

# 消息提示框
prompt = st.chat_input("请输入问题")
# 消息容器
# 1.角色2.消息{'role':"user","content":"xxx"}
if prompt:
    # 提问存到历史会话中
    st.session_state["message"].append({"role": "user", "content": prompt})
    # 将历史消息全部输出到消息容器中
    for message in st.session_state["message"]:
        st.chat_message(message["role"]).markdown(message["content"])
    with st.spinner("思考中"):
        response = ollama.chat(
            model="deepseek-r1:1.5b", messages=[{"role": "user", "content": prompt}]
        )
        # 把回答记录到历史会话中
        st.session_state["message"].append(
            {"role": "assistant", "content": response["message"]["content"]}
        )
        # 把回答渲染到界面中
        st.chat_message("assistant").markdown(response["message"]["content"])
