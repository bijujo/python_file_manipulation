#!/usr/bin/env python
import boto3
import json
##
ec2client =  boto3.client('ec2')
status = ec2client.describe_instance_status(IncludeAllInstances=True)
#print(status['InstanceStatuses'])
for namestat in status['InstanceStatuses']:
	instid = namestat['InstanceId']
	#print(instid)
        vmstate = (namestat['InstanceState'])
        print(vmstate['Name'])
	if vmstate['Name'] == 'running':
		print('VM {} running. No action to take'.format(instid))
	elif vmstate['Name'] == 'stopped':
		print('VM {} in stopped state. Starting VM'.format(instid))
		ec2client.start_instances(InstanceIds=[instid])
	else:
		print('VM {} not in a stable state. Check console'.format(instid))
