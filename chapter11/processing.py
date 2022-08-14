import pandas as pd
import os

from pathlib import Path
from sklearn.model_selection import train_test_split
    

def load_input(input_target):
    input_dir = "/opt/ml/processing/input"
    
    df = pd.read_csv(f"{input_dir}/{input_target}",
                     engine='python')
    
    return df
    

def save_csv(df, filename):
    output_dir = "/opt/ml/processing/output"
    full_path = f"{output_dir}/{filename}"
    
    df.to_csv(full_path, 
              index=False, 
              header=False)
    
    
def ensure_dir(directory):
    output_dir = "/opt/ml/processing/output"
    full_path = f"{output_dir}/{directory}"
    
    Path(full_path).mkdir(parents=True, exist_ok=True)
        

def main():
    all_df = load_input("dataset.all.csv")
    
    train_val_df, test_df = train_test_split(
        all_df, test_size=0.1, random_state=0
    )
    train_df, val_df = train_test_split(
        train_val_df, test_size=0.1, random_state=0
    )
    
    ensure_dir("train")
    ensure_dir("validation")
    ensure_dir("test")
    
    save_csv(train_df, "train/data.csv")
    save_csv(val_df, "validation/data.csv")
    save_csv(test_df, "test/data.csv")
    

if __name__ == "__main__":
    main()