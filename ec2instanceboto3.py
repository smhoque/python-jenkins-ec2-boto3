import boto3

ec2_resource = boto3.resource('ec2')

# Following script installs Apache server and sets up a simple HTML page
user_data_script = """#!/bin/bash
apt update -y
apt install -y apache2
systemctl start apache2
systemctl enable apache2

echo "<html><body><h1>My First EC2 Instance</h1></body></html>" > /var/www/html/index.html

ufw allow 'Apache Full' || true
"""
# Launching an EC2 instance with the specified configurations
instances = ec2_resource.create_instances(
    ImageId='ami-00f46ccd1cbfb363e',  # Ubuntu AMI (verify region)
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',

    BlockDeviceMappings=[
        {
            'DeviceName': '/dev/sda1',
            'Ebs': {
                'VolumeSize': 20,
                'VolumeType': 'gp2',
                'DeleteOnTermination': True
            }
        }
    ],

    UserData=user_data_script,

    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {'Key': 'Name', 'Value': 'Ec2bootingtestinng'},
                {'Key': 'Department', 'Value': 'Technical'},
                {'Key': 'Environment', 'Value': 'Test'}
            ]
        }
    ]
)

for instance in instances:
    print(f"Instance ID: {instance.id} launched with a 20GB volume and Apache server.")
