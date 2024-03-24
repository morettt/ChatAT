#!/bin/bash

cd /root/ChatAT/finetune_demo
source activate py310_chat
python finetune_hf.py data/ /root/autodl-tmp/chatglm3-6b configs/lora.yaml

python /root/ChatAT/finetune_demo/cli_demo.py