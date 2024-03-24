import re

def format_text(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    questions = re.split('问[：:]\s*', content)[1:]

    formatted_text = ''
    for q in questions:
        if re.search('答[：:]\s*', q):
            parts = re.split('答[：:]\s*', q, 1)
            question, answer = parts[0], parts[1]
            formatted_question = '问：' + question.strip()
            # 移除答案文本中的所有换行符
            formatted_answer = '答：' + answer.replace('\n', ' ').strip()
            # 保留数字列表格式，但不引入新的换行符
            formatted_answer = re.sub(r'(\d+)\.', r' \1.', formatted_answer)
            formatted_text += f'{formatted_question}\n{formatted_answer}\n\n'
        else:
            formatted_text += '问：' + q.strip() + '\n\n'

    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(formatted_text)

# 指定源文件路径和输出文件路径
source_file_path = '/root/ChatAT/openai_api_demo/内容回复.txt'
output_file_path = '/root/ChatAT/openai_api_demo/内容回复2.txt'

# 调用函数
format_text(source_file_path, output_file_path)
