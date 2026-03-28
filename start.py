import ollama


# 获得ollama客户端对象
client = ollama.Client(host="http://localhost:11434")
print("=== 客户端对象信息 ===")
print(f"客户端对象: {client}")  # 打印客户端实例
print(f"客户端创建成功: {client is not None}")

# list列出有哪些可用模型
print(client.list())
models = client.list()
for m in models.models:
    # m  =  当前这个模型的全部数据 m.model  =  只拿这个模型的【名字】！
    print(f"✅ {m.model}")

# show 展示模型详细信息
# print(client.show('deepseek-r1:1.5b'))
# ps哪些模型在运行中
print(client.ps())

# chat对话
while True:
    prompt = input("请输入问题")
    response = client.chat(
        model="deepseek-r1:1.5b", messages=[{"role": "user", "content": prompt}]
    )
    print(response["message"]["content"])
