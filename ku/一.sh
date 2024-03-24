#!/bin/bash

pkill -f "python openai_api-qwen.py"

source activate py310_chat     
cd ../ChatAT/finetune_demo

python finetune_hf.py data/ ../LLM-model/chatglm3-6b configs/lora.yaml

python ../ChatAT/finetune_demo/cli_demo.py
