import requests
import json
import os
import random

# 第一段代码：聊天对话记录和结束控制
def create_chat_completion(model, messages, use_stream=False):
    base_url = "http://127.0.0.1:6006"
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

# 第二段代码：处理对话和随机样本选择的函数
def load_existing_data(file_path):
    data = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                data.append(json.loads(line))
    except FileNotFoundError:
        pass
    except json.JSONDecodeError as e:
        print(f"JSON解析错误：{e}")
    return data

def merge_datasets(existing_data, new_data):
    return existing_data + new_data

def process_conversations_from_file(file_path, base_data_path, output_file_path):
    try:
        os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
        
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        new_data = []
        conversation_pair = {}
        skip_first_user_line = True

        for line in lines:
            if line.startswith("用户：") and skip_first_user_line:
                skip_first_user_line = False
                continue
            elif line.startswith("机器："):
                machine_content = line.replace("机器：", "").strip()
                conversation_pair = {"conversations": [{"role": "user", "content": machine_content}]}
            elif line.startswith("用户："):
                user_content = line.replace("用户：", "").strip()
                if 'conversations' in conversation_pair:
                    conversation_pair["conversations"].append({"role": "assistant", "content": user_content})
                    new_data.append(conversation_pair)
                    conversation_pair = {}

        existing_data = load_existing_data(base_data_path)
        merged_data = merge_datasets(existing_data, new_data)
        
        with open(output_file_path, 'w', encoding='utf-8') as outfile:
            for data in merged_data:
                json.dump(data, outfile, ensure_ascii=False)
                outfile.write('\n')
        
        return "File processed and output saved to " + output_file_path
    except Exception as e:
        return {"error": str(e)}

def select_and_save_random_samples(input_file_path, output_file_path, num_samples=50):
    data = []
    with open(input_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                conversation = json.loads(line)
                data.append(conversation)
            except json.JSONDecodeError as e:
                print(f"解析错误: {e.msg}, 行: {line}")
    selected_items = random.sample(data, min(num_samples, len(data)))
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for item in selected_items:
            json.dump(item, file, ensure_ascii=False)
            file.write('\n')
    print(f"已成功保存选中的记录到 {output_file_path}")

# 结合代码的主执行逻辑
if __name__ == "__main__":
    chat_messages = [{"role": "system", "content": "从现在开始扮演一个可爱的萌妹和我对话"}]
    file_path = "xxx.txt"
    base_data_path = "qqq.json"
    train_output_file_path = "../finetune_demo/data/train.json"
    dev_output_file_path = "../finetune_demo/data/dev.json"

    with open(file_path, "w", encoding="utf-8") as file:
        while True:
            user_input = input("用户：").strip()
            if user_input.lower() == "stop":
                break
            chat_messages.append({"role": "user", "content": user_input})
            response = create_chat_completion("chatglm3-6b", chat_messages, use_stream=False)
            if response:
                print("机器：", response)
                file.write(f"用户：{user_input}\n机器：{response}\n")
    
    # 对话结束，处理并保存数据
    print(process_conversations_from_file(file_path, base_data_path, train_output_file_path))
    select_and_save_random_samples(train_output_file_path, dev_output_file_path)
