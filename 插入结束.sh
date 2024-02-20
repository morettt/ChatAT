#!/bin/bash
cd /root/ChatGLM3/finetune_demo
source activate py310_chat
python train_and_infer.py data/ /root/autodl-tmp/chatglm3-6b configs/lora.yaml