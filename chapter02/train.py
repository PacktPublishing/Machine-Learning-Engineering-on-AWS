import tensorflow as tf
import os
import numpy as np
from numpy.random import seed

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import TensorBoard

def set_seed():
    seed(42)
    tf.random.set_seed(42)


def load_data(location):
    result = np.loadtxt(open(location, "rb"), delimiter=",")
    
    y = result[:, 0]
    x = result[:, 1]
    
    return (x, y)


def prepare_model():
    model = Sequential([
        Dense(100, activation=tf.nn.leaky_relu, 
                   input_shape=[1]),
        Dense(100, activation=tf.nn.leaky_relu),
        Dense(100, activation=tf.nn.leaky_relu),
        Dense(100, activation=tf.nn.leaky_relu),
        Dense(1)
      ])
    
    model.compile(loss='mean_squared_error', 
                  optimizer='adam')
    
    return model


def main(model_dir, train_path, val_path, 
         batch_size=200, epochs=500):
    set_seed()
    
    model = prepare_model()
    model.summary()
        
    x, y = load_data(train_path)
    x_val, y_val = load_data(val_path)

    log_folder = 'logs'
    
    callbacks = [TensorBoard(log_dir=log_folder,
        histogram_freq=1,
        write_graph=True,
        write_images=True,
        update_freq='epoch',
        profile_batch=2,
        embeddings_freq=1)]

    model.fit(x=x, 
              y=y, 
              batch_size=batch_size, 
              epochs=epochs, 
              validation_data=(x_val, y_val),
              callbacks=callbacks)    
    
    model.save(model_dir)


if __name__ == "__main__":
    data_path = "data"
    model_dir = "model"
    train_path = f"{data_path}/training_data.csv"
    val_path = f"{data_path}/validation_data.csv"
    
    main(model_dir=model_dir,
         train_path=train_path,
         val_path=val_path,
         batch_size=200,
         epochs=500)