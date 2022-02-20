```
mkdir -p data
mkdir -p logs
wget https://bit.ly/3h1KBx2 -O data/training_data.csv
wget https://bit.ly/3gXYM6v -O data/validation_data.csv
wget https://bit.ly/35aKWem -O data/test_data.csv

wget https://bit.ly/33D0iYC -O train.py

python3.8 train.py
tensorboard --logdir=logs --bind_all
jupyter notebook --allow-root --port 8888 --ip 0.0.0.0
```