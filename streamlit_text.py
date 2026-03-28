import streamlit as st
import time

# session_state保存历史会话
# 初始化
if "count" not in st.session_state:
    st.session_state["count"] = 1

# 标题
st.title("智能Agent")

# 分隔符
st.divider()

# 消息提示框
prompt = st.chat_input("请输入问题")

# 消息容器
if prompt:
    # user,assistant
    st.chat_message("user").markdown(prompt)

    # 回答
    with st.spinner("思考中"):
        time.sleep(3)
        st.chat_message("assistant").markdown(f"我不会{st.session_state["count"]}")
        st.session_state["count"] += 1
