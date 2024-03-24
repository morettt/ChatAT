import json

def process_and_transform_file(input_path, output_path):
    try:
        intermediate_data = []
        prompt, response = "", ""

        with open(input_path, 'r', encoding='utf-8') as file:
            for line in file:
                if line.startswith(("问：", "问:")):
                    if prompt and response:
                        intermediate_data.append({"prompt": prompt, "response": response})
                    prompt, response = line[2:].strip(), ""
                elif line.startswith(("答：", "答:")):
                    response = line[2:].strip()

        if prompt and response:
            intermediate_data.append({"prompt": prompt, "response": response})

        with open(output_path, 'w', encoding='utf-8') as output_file:
            for entry in intermediate_data:
                transformed_data = {
                    "conversations": [
                        {"role": "user", "content": entry["prompt"]},
                        {"role": "assistant", "content": entry["response"]}
                    ]
                }
                output_file.write(json.dumps(transformed_data, ensure_ascii=False) + '\n')

        print(f"转换完成，中文字符未被转义，并已保存至：{output_path}")

    except Exception as e:
        print(f"处理文件时发生错误：{e}")

# 指定原始文件路径和输出文件路径
input_path = "/root/ChatAT/openai_api_demo/内容回复2.txt"  # 这里替换成你的输入文件路径
output_path = "/root/ChatAT/finetune_demo/data/train.json"  # 这里替换成你的输出文件路径

# 调用函数处理文件
process_and_transform_file(input_path, output_path)
