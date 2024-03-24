# ChatAT

首先克隆代码：
``` 
git clone https://github.com/morettt/ChatAT
``` 
安装依赖：
``` 
cd ChatAT
pip install -r requirements.txt
```


下载安装lfs（帮助下载大文件）
``` 
git lfs install

cd LLM-model
git clone https://huggingface.co/THUDM/chatglm3-6b
``` 

您在左侧可发现一个名为“数据集全自动处理”的文件夹。点开后，您将看到一个名为“受刑文本”的文件，请将您需要的文本粘贴到此文件并保存。此系统支持几乎所有类型的文本，包括但不限于小说、公司资料、技术手册、教科书、法律和医学资料等等。我在这里放了一篇关于人工智能的一些文章，大家可以删除，替换为自己要训练的内容。或者也可以直接用我的这个来测试。

本项目有两种处理模式：《本地模型》和《ChatGPT》模型。通过实践发现，ChatGPT模型效果更为优质，而本地模型则无需任何额外条件即可使用。
您可以按照自己实际体验选择其中一种，接下来，我将分别介绍两种操作方法。


《本地模型》
在第一个终端运行：

cd ChatAT/openai_api_demo

python openai_api-qwen.py

在第二个终端运行：

cd ChatAT/openai_api_demo

python 一条龙qwen.py

处理结束后，你可以去ChatAT/finetune_demo/data 路径下看看数据集是否满足自己的要求，也可以手动清洗，
以保证更优质的数据集。确保数据集满足自己要求后，即可运行（依旧粘贴在第二个终端）：

python finetune_hf.py data/ ../LLM-model/chatglm3-6b configs/lora.yaml



《ChatGPT》

直接在终端运行：

bash /root/ChatAT/ku/半自动.sh

处理结束后，你可以去ChatAT/finetune_demo/data 路径下看看数据集是否满足自己的要求，也可以手动清洗，
以保证更优质的数据集。确保数据集满足自己要求后，即可运行：

bash /root/ChatAT/ku/全自动.sh

接下来就只需要等待，模型会自动训练，且训练完会自动推理

python finetune_hf.py data/ ../LLM-model/chatglm3-6b configs/lora.yaml

