import pandas as pd
from utils import block, debug
from sklearn.model_selection import train_test_split


with block('LOAD CSV'):
    generated_df = pd.read_csv('tmp/bookings.all.csv')


with block('TRAIN-TEST SPLIT'):
    train_df, test_df = train_test_split(
        generated_df, 
        test_size=0.3, 
        random_state=0
    )
    print(train_df)
    print(test_df)
    

with block('SAVE TO CSVs'):
    train_df.to_csv('tmp/bookings.train.csv', 
                    index=False)
    test_df.to_csv('tmp/bookings.test.csv', 
                   index=False)