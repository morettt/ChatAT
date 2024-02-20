# ChatAT
只需和机器人聊天就可以训练出你自己！全自动llm大语言模型训练！
建议去autodl部署，因为我也是在那里制作的，你直接在本地运行100%会报错而且一头雾水，等我两天，或者直接加我QQ1010277101 我把项目整理一下。

首先构建虚拟环境：

conda create -n chatAT python=3.10 -y       创建新环境
source activate chatAT               激活环境

安装依赖：

cd ChatAT
pip install -r requirements.txt


在第一个终端中输入以下命令：

bash /root/ChatAT/one.sh

在第二个终端中输入以下命令开始和模型对话：

bash /root/ChatAT/two.sh

最后训练模型，并一键对话：

bash /root/ChatAT/插入结束.sh
