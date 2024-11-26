# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 14:37:41 2024

@author: yong
"""

# Create configuration
import yaml
config = {'path': 'G:\\phd\\resume\\footfall\\object detection',
         'train': 'G:\\phd\\resume\\footfall\\object detection\\train',
         'val': 'G:\\phd\\resume\\footfall\\object detection\\valid',
         'test': 'G:\\phd\\resume\\footfall\\object detection\\test',
         'nc': 1,
         'names': ['Tag']}
 
with open("G:\\phd\\resume\\footfall\\object detection\\data.yaml", "w") as file:
   yaml.dump(config, file, default_flow_style=False)
   
   

import train
import torch
#import wandb
#wandb.login()

torch.cuda.is_available()

if torch.cuda.is_available():
    dev = "cuda:0"
else:
    dev = "cpu"

# device = torch.device(dev)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

torch.cuda.empty_cache()


train.run(imgsz = 224,
                 batch=1, epochs=15, 
                 data="interview_footfall.yaml",
                 #weights='yolov5m.pt',
                 weights='',
                 cfg='yolov5n.yaml',
                 #workers=0,
                 device=0,
                 )
