#!/usr/bin/env python

########################################################################################################
#                                                                                                      #
#  AWS Opsworks Backup                                                                                 #
#  Developed by Thiago Vinhas                                                                          #
#                                                                                                      #
########################################################################################################

import boto3
import json
import datetime
import time
import argparse

date = datetime.datetime.now().strftime('%Y-%m-%d')

parser = argparse.ArgumentParser(description='You have to specify at least the name of the instance')

parser.add_argument('-s', '--stack', action="store", dest="stack_id", required=True, help="Define the id of the stack you want to backup")
parser.add_argument('-p', '--path', action="store", dest="path", default="./", help="Define the path where the backup will be saved")

args = parser.parse_args()
stack_id = args.stack_id
backup_path = args.path

##############################################
####           AWS Credentials            ####
##############################################

conn = {
    'aws_access_key_id': 'AKIA****************',
    'aws_secret_access_key': '************************************',
    'region_name': 'us-east-1'
}

##############################################
####               Stacks                 ####
##############################################

stacks = boto3.client('opsworks', **conn)
export_stacks = stacks.describe_stacks(
    StackIds=[
        stack_id,
    ]
)
stacks_json=json.dumps(export_stacks, indent=2)

filename = (backup_path + "stacks-" + date + ".json")
stacks_file = open(filename, 'w')
stacks_file.write(stacks_json)
stacks_file.close()

##############################################
####               Layers                 ####
##############################################

layers = boto3.client('opsworks', **conn)
export_layers = layers.describe_layers(
    StackId=stack_id
)
layers_json=json.dumps(export_layers, indent=2)

filename = (backup_path + "layers-" + date + ".json")
layers_file = open(filename, 'w')
layers_file.write(layers_json)
layers_file.close()

##############################################
####              Instances               ####
##############################################

instances = boto3.client('opsworks', **conn)
export_instances = instances.describe_instances(
    StackId=stack_id
)
instances_json=json.dumps(export_instances, indent=2)

filename = (backup_path + "instances-" + date + ".json")
instances_file = open(filename, 'w')
instances_file.write(instances_json)
instances_file.close()

##############################################
####                Apps                  ####
##############################################

apps = boto3.client('opsworks', **conn)
export_apps = apps.describe_apps(
    StackId=stack_id
)
apps_json=json.dumps(export_apps, indent=2)

filename = (backup_path + "apps-" + date + ".json")
apps_file = open(filename, 'w')
apps_file.write(apps_json)
apps_file.close()


print "Backup executed on: " , date
