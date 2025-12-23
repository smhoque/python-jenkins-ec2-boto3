import boto3

ec2_resource = boto3.resource('ec2')
instance_id = "i-00b0b3e9039428ee3"
instance = ec2_resource.Instance(instance_id)
instance.terminate()
print("Instance terminated successfully.")