import boto3
import os
from time import sleep


ec2 = boto3.client('ec2')

volume_info = ec2.describe_volumes(
    Filters=[
        {
            'Name': 'attachment.instance-id',
            'Values': [
                os.getenv('EC2_INSTANCE_ID')
            ]
        }
    ]
)

volume_id = volume_info['Volumes'][0]['VolumeId']
ec2.modify_volume(VolumeId=volume_id, Size=120)
sleep(5)

os.system("sudo reboot")
