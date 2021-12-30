pip3 install --user --upgrade boto3

TARGET_METADATA_URL=http://169.254.169.254/latest/meta-data/instance-id
export EC2_INSTANCE_ID=$(curl -s $TARGET_METADATA_URL)

python3 resize_and_reboot.py