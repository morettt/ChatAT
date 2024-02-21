#!/bin/bash
cd finetune_demo
source activate chatAT
python train_and_infer.py data/ ../LLM-model/chatglm3-6b configs/lora.yaml
