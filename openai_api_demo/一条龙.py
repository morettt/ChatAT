import subprocess

# 运行脚本1
subprocess.run(["python", "/root/ATAI Workshop/openai_api_demo/第一步处理文本.py"])

# 脚本1运行完成后，运行脚本2
subprocess.run(["python", "/root/ATAI Workshop/openai_api_demo/第二步模型.py"])

# 脚本1运行完成后，运行脚本2
subprocess.run(["python", "/root/ATAI Workshop/openai_api_demo/第三步处理QA.py"])
