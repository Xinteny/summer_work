import os
import sys
import yaml
import torch
import argparse
from utils import metrics
from models import *
from dataset import *
from torch.utils.data import DataLoader


def load_config(config_path):
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    return config


def main(args):
    # config
    train_config = load_config(args.config_path)
    
    # dataset

    # scaler
    
    # model

    # dataloader dataset - model

    # trainer



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config_path', type=str, default='./config/train_config.yaml')
    # ...
    args = parser.parse_args()
    main(args)