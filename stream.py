import streamlit as st
import time

# 标题
st.title("智能助手")
# 渲染内容
st.write("你好！")
# 分隔符
st.divider()
# 聊天输入框
name = st.chat_input("请输入你的名字___")
if name:
    st.write(f"你好,{name}")

# 等待提示框
with st.spinner("思考中"):
    time.sleep(5)

# 消息容器 角色支持user assistant ai human
st.chat_message("user").markdown("你是谁")
st.chat_message("assistant").markdown("我是智能助手")
