import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')


    tag_key = 'AutoStartStop'
    tag_value = 'True'

    # Retrieve all EC2 instances
    instances = ec2.describe_instances(
            Filters=[{'Name': f'tag:{tag_key}', 'Values': [tag_value]}]
            )
    instance_ids = []
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            instance_id.append(instance_id)
            
    if not instance_ids:
        print("No instances found with the specified tag AutoStartStop=True.")
        return 

action = event.get('action', 'stop').lower()

if action == 'start':
    ec2.start_instances(InstanceIds=instance_ids)
    print(f'Started instances: {instance_ids}')

elif action == 'stop':
    ec2.stop_instances(InstanceIds=instance_ids)
    print(f'Stopped instances: {instance_ids}')

else:
    print("Invalid action specified. Use 'start' or 'stop'.")