#!/bin/bash

pkill -f "python openai_api-qwen.py"

source activate py310_chat     
cd /root/ChatAT/finetune_demo

python finetune_hf.py data/ /root/autodl-tmp/chatglm3-6b configs/lora.yaml

python /root/ChatAT/finetune_demo/cli_demo.py