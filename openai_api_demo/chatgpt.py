import openai

# 你的OpenAI API密钥
api_key = "sk-RZFk2k35us1IllZu569a6829Ef4449A68784C502F1170815"
openai.api_base = " https://oneapi.xty.app/v1"

def chat_with_gpt3_5(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        api_key=api_key
    )
    assistant_reply = response['choices'][0]['message']['content']
    return assistant_reply


# 初始对话，可以通过增加更多的“助手”和“用户”消息来持续对话
conversation = [
    {"role": "system", "content": "你现在要模仿一个傲娇萌娘和我对话"}
]

# 无限循环，直到用户输入“退出”才停止
while True:
    # 获取用户输入
    user_input = input("You: ")

    # 检查是否要退出
    if user_input.lower() == '退出':
        print("Assistant: 再见！")
        break

    # 添加用户消息到对话中
    conversation.append({"role": "user", "content": user_input})

    # 获取助手的回复并打印
    assistant_message = chat_with_gpt3_5(conversation)
    print("Assistant: ", assistant_message)

    # 将助手的回复添加到对话中，以便继续上下文
    conversation.append({"role": "assistant", "content": assistant_message})