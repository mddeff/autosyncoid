#!/usr/bin/env python


import yaml
import subprocess as sp
import os
import sys

if len(sys.argv) > 1:
    configFile =  sys.argv[1]
else:
    configFile = "/etc/sanoid/autosyncoid.yaml"

# read yaml config file
try:
    config = yaml.safe_load( open(configFile, 'r') )
except FileNotFoundError:
    print(configFile + " was not found. Exiting!")
    sys.exit(1)

# read global args

defaultArgs = []
if 'defaultArgs' in config and isinstance(config['defaultArgs'], list):
    defaultArgs = config['defaultArgs']

# loop through datasets
for dataset in config["datasets"]:

    # read local args
    datasetArgs = ""
    if 'options' in dataset and isinstance(dataset['options'], list):
        datasetArgs = dataset['options']

    # construct command string
    cmdString = "sanoid " + ' '.join(config['defaultArgs']) + " " + ' '.join(dataset['options']) + " " + dataset['source'] + " " + dataset['target']
    print("Running the following command:\n" + cmdString)

    # construct command list
    cmdList = ['syncoid']
    cmdList.extend(defaultArgs)
    cmdList.extend(dataset['options'])
    cmdList.append(dataset['source'])
    cmdList.append(dataset['target'])

    # do it
    sp.run(cmdList)