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

# read 'options' section of config file

defaultArgs = []
syncoidCommand = ""
dryrun = None

if 'defaultArgs' in config['options'] and isinstance(config['options']['defaultArgs'], list):
    defaultArgs = config['options']['defaultArgs']

if 'syncoidCommand' in config['options']:
    syncoidCommand = config['options']['syncoidCommand']
if 'dryrun' in config['options'] and config['options']['dryrun']:
    dryrun = True


# loop through datasets
for dataset in config["datasets"]:

    # read local args
    datasetArgs = []
    if 'options' in dataset and isinstance(dataset['options'], list):
        datasetArgs = dataset['options']

    # construct command string - just for pretty printing
    cmdList = [syncoidCommand]
    cmdList.extend(defaultArgs)
    cmdList.extend(datasetArgs)
    cmdList.append(dataset['source'])
    cmdList.append(dataset['target'])

    cmdString = ' '.join(cmdList)
    print("Running the following command:\n" + cmdString)

    # do it
    if dryrun:
        print( ".....DRYRUN enabled, not actually running...")
    else:
        sp.run(cmdList)