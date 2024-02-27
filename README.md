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
搭建虚拟环境
``` 
conda create -n ChatAT python=3.10 -y
source activate ChatAT
``` 

下载安装lfs（帮助下载大文件）
``` 
apt-get update
apt-get install git-lfs
git init
git lfs install

cd LLM-model
git clone https://huggingface.co/THUDM/chatglm3-6b
``` 

在第一个终端中输入以下命令：
``` 
cd ChatAT

bash one.sh
``` 
在第二个终端中输入以下命令开始和模型对话：
``` 
bash two.sh
``` 
最后训练模型，并一键对话：

``` 
bash 插入结束.sh
```
如果想再和微调后的模型对话可以运行
```
bash 推理.sh
``` 
