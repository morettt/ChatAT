import subprocess
import sys

def train_and_infer(data_dir, model_dir, config_file, checkpoint_dir):
    # 训练模型
    finetune_command = f"python finetune_hf.py {data_dir} {model_dir} {config_file}"
    print(f"Executing training command: {finetune_command}")
    subprocess.run(finetune_command, shell=True)
    
    # 推理
    # 注意：这里假设训练脚本会在`checkpoint_dir`中保存模型，你可能需要根据实际情况调整路径
    infer_command = f"python duolun.py {checkpoint_dir}"
    print(f"Executing inference command: {infer_command}")
    subprocess.run(infer_command, shell=True)

if __name__ == "__main__":
    # 假设命令行参数顺序依次是：data_dir model_dir config_file
    if len(sys.argv) != 4:
        print("Usage: python train_and_infer.py data_dir model_dir config_file")
        sys.exit(1)
    
    data_dir = sys.argv[1]
    model_dir = sys.argv[2]
    config_file = sys.argv[3]
    
    # 你需要根据`finetune_hf.py`的实际行为来确定checkpoint的保存路径
    # 这里假设它保存在某个基于训练配置命名的默认路径下
    checkpoint_dir = "output/checkpoint-2500/"
    
    train_and_infer(data_dir, model_dir, config_file, checkpoint_dir)
