import requests
import json

base_url = "http://127.0.0.1:8501"  # 本地部署的地址

def create_chat_completion(model, messages, use_stream=False):
    data = {
        "model": model,
        "messages": messages,
        "stream": use_stream,
        "max_tokens": 100,
        "temperature": 0.8,
        "top_p": 0.8,
    }

    response = requests.post(f"{base_url}/v1/chat/completions", json=data, stream=use_stream)
    if response.status_code == 200:
        decoded_line = response.json()
        content = decoded_line.get("choices", [{}])[0].get("message", {}).get("content", "")
        return content
    else:
        return "Error: " + str(response.status_code)

if __name__ == "__main__":
    chat_messages = [
        {
            "role": "system",
            "content": "从现在开始扮演一个可爱的萌妹和我对话",
        }
    ]

    # 打开或创建一个文本文件用于记录聊天内容
    with open("xxx.txt", "w", encoding="utf-8") as file:
        while True:
            user_input = input("用户：").strip()
            if user_input:  # 确保用户输入不为空
                chat_messages.append({"role": "user", "content": user_input})
                response = create_chat_completion("chatglm3-6b", chat_messages, use_stream=False)
                if response:  # 确保模型响应不为空
                    print("机器：", response)
                    # 将对话内容写入文本文件
                    file.write(f"用户：{user_input}\n")
                    file.write(f"机器：{response}\n")
