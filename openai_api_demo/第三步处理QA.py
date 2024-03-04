import json

def process_and_transform_file(input_path, intermediate_path, output_path):
    try:
        # 第一步：处理原始文件，提取问答对
        with open(input_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        intermediate_data = []
        prompt = ""
        response = ""
        for line in lines:
            if line.startswith("q:"):
                if prompt and response:
                    intermediate_data.append({"prompt": prompt.strip(), "response": response.strip()})
                prompt = line[2:].strip()
                response = ""
            elif line.startswith("a:"):
                response = line[2:].strip()

        if prompt and response:
            intermediate_data.append({"prompt": prompt.strip(), "response": response.strip()})

        # 第二步：转换格式并写入最终文件
        with open(output_path, 'w', encoding='utf-8') as output_file:
            for entry in intermediate_data:
                transformed_data = {
                    "conversations": [
                        {"role": "user", "content": entry["prompt"]},
                        {"role": "assistant", "content": entry["response"]}
                    ]
                }
                output_file.write(json.dumps(transformed_data, ensure_ascii=False) + '\n')

        print("转换完成，中文字符未被转义，并已保存至：" + output_path)

    except Exception as e:
        print("处理文件时发生错误：", e)

# 指定原始文件路径、中间文件路径和输出文件路径
input_path = "/root/ATAI Workshop/openai_api_demo/内容回复.txt"
intermediate_path = "/root/ATAI Workshop/openai_api_demo/处理后的qa.txt"  # 此路径在代码逻辑中实际上未使用
output_path = "/root/ATAI Workshop/openai_api_demo/train.json"

# 调用函数处理文件
process_and_transform_file(input_path, intermediate_path, output_path)
