#!/bin/bash
cd /root/ChatAT/finetune_demo
source activate chatAT
python train_and_infer.py data/ /root/autodl-tmp/chatglm3-6b configs/lora.yaml
