import glob
import importlib
import os

from util.registry import Registry
TRAINER = Registry('Trainer')

files = glob.glob('trainer/[!_]*.py')
for file in files:
	model_lib = importlib.import_module(file.split('.')[0].replace(os.sep, '.'))


def get_trainer(cfg):
	return TRAINER.get_module(cfg.trainer.name)(cfg)
