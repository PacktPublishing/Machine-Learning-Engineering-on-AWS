aws ecr get-login-password --region us-west-2 | docker login --username AWS --password-stdin 763104351884.dkr.ecr.us-west-2.amazonaws.com
TRAINING_IMAGE=763104351884.dkr.ecr.us-west-2.amazonaws.com/pytorch-training:1.8.1-cpu-py36-ubuntu18.04
docker run -it -v `pwd`:/env -w /env $TRAINING_IMAGE python train.py