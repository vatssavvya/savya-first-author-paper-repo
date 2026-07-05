import torch
available_gpus = torch.cuda.device()

for i in range(torch.cuda.device_count()):

    print(available_gpus)