import openai

# 你的OpenAI API密钥
api_key = "sk-19Xit42KAHxmBIOB76Ea1a97D26045388d69Eb63Af419eC7"
openai.api_base = "https://api.xty.app/v1"

def chat_with_gpt3_5(user_input, max_retries=3):
    system_message = {
        "role": "system",
        "content": "把其中关键的内容提取出来，制作成我需要的对话数据集的格式，也就是常见的问答数据语料，请不要用第三视角制作数据集。请你用第一或者第二视角例如：问:你觉得为什么我总是倒霉？答:我觉得你太消极了，你可以多关注一些别的好的一方面。不要总关心坏的一方面。仿照我给的例子用问: 答: 这样的格式制作数据集。最后，问答对中，在答的部分，要给出足够长的回答。下面是原文："
    }
    user_message = {"role": "user", "content": user_input}

    for attempt in range(1, max_retries + 1):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[system_message, user_message],
                api_key=api_key
            )
            assistant_reply = response['choices'][0]['message']['content']
            return assistant_reply
        except Exception as e:
            print(f"处理问题时出错，尝试次数：{attempt}/{max_retries}。错误信息：{e}")
            if attempt == max_retries:
                return f"重试{max_retries}次后仍然失败，错误信息：{e}"

def batch_chat_with_gpt3_5_immediate_print_and_save(question_list, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for question in question_list:
            # 获取每个问题的回答
            answer = chat_with_gpt3_5(question)
            # 立即打印每个问题的回答
            print(f"Assistant: {answer}\n")
            # 将回答写入文件，不包含任何前缀
            file.write(f"{answer}\n\n")

def load_questions_from_file(file_path):
    questions = []
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        questions = content.split("《问题》")[1:]  # 分割文本以获取问题列表
        questions = [q.strip() for q in questions]  # 去除每个问题前后的空格
    return questions

# 假设的文件路径，请替换为您的实际文件路径
file_path = "/root/ChatAT/openai_api_demo/重生文本.txt"
# 输出文件的名称
output_file = "内容回复.txt"

# 从文件加载问题
questions = load_questions_from_file(file_path)

# 使用加载的问题与模型进行交云，并保存回复到文件
batch_chat_with_gpt3_5_immediate_print_and_save(questions, output_file)
