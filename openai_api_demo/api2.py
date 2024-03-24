import requests
import base64
import random
import time

# 假设的API URL和认证信息，根据实际情况替换
api_url = "http://127.0.0.1:8000/v1/chat/completions"
api_username = "myapikey"
api_password = "myapikey"

def chat_with_api(user_input, max_retries=3):
    credentials = base64.b64encode(f"{api_username}:{api_password}".encode()).decode('utf-8')
    headers = {
        "Authorization": f"Basic {credentials}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "qwen_turbo",
        "messages": [
            {'role': 'system', 'content': '把其中关键的内容提取出来，制作成我需要的对话数据集的格式，也就是常见的问答数据语料，请不要用第三视角制作数据集。请你用第一或者第二视角，例如：问:答:  这样的格式。最后，问答对中，在答的部分，要给出足够长的回答。下面是原文：'},
            {'role': 'user', 'content': user_input}
        ],
        "seed": random.randint(1, 10000),
        "result_format": "message"
    }
    
    for attempt in range(1, max_retries + 1):
        try:
            response = requests.post(api_url, json=data, headers=headers)
            if response.status_code == 200:
                return response.json()['choices'][0]['message']['content']
            else:
                print('Attempt:', attempt, 'Error:', response.status_code, response.text)
        except Exception as e:
            print(f"Attempt: {attempt}. Error: {e}")
        time.sleep(1)
    return "After maximum retries, the request failed."

def batch_chat_and_save(question_list, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for question in question_list:
            answer = chat_with_api(question)
            print(answer)  # 直接打印回答，不打印问题
            file.write(f"{answer}\n\n")  # 文件中保存回答


def load_questions_from_file(file_path):
    questions = []
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        questions = content.split("《问题》")[1:]
        questions = [q.strip() for q in questions]
    return questions

# 示例文件路径和输出文件路径，根据实际情况替换
file_path = "/root/ChatAT/openai_api_demo/重生文本.txt"
output_file = "内容回复.txt"

questions = load_questions_from_file(file_path)
batch_chat_and_save(questions, output_file)
