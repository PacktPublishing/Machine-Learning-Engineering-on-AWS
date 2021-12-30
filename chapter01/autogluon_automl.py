from autogluon.tabular import TabularDataset, TabularPredictor
from utils import block, debug


with block('LOAD TRAIN AND TEST DATASETS'):
    train_loc = 'tmp/bookings.train.csv'
    test_loc = 'tmp/bookings.test.csv'
    
    train_data = TabularDataset(train_loc)
    test_data = TabularDataset(test_loc)
    
    print(train_data.head())
    print(test_data.head())


with block('TRAINING STEP'):
    label = 'is_cancelled'
    save_path = 'tmp'
    tp = TabularPredictor(label=label, path=save_path)
    predictor = tp.fit(train_data)
    
    
with block('LOAD MODEL'):
    predictor = TabularPredictor.load(save_path)
    
    
with block('PREPARE TEST DATA'):
    y_test = test_data[label]
    test_data_without_label = test_data.drop(columns=[label])
    print(test_data_without_label.head())
    y_pred = predictor.predict(test_data_without_label)
    
    
with block('EVALUATE PREDICTIONS'):
    predictor.evaluate_predictions(
        y_true=y_test, 
        y_pred=y_pred, 
        auxiliary_metrics=True
    )
    
    leaderboard = predictor.leaderboard(test_data, silent=True)
    print(leaderboard)
    
    
with block('GET BEST MODEL'):
    best_model = predictor.get_model_best()
    print(best_model)
    
    
with block('SINGLE PREDICTION'):
    datapoint = test_data_without_label.iloc[[0]]
    print(datapoint)

    result = predictor.predict(datapoint)
    print(result)
    
    result = predictor.predict_proba(datapoint)
    print(result)
    

with block('FEATURE IMPORTANCE'):
    fi = predictor.feature_importance(test_data)
    print(fi)
    
    
with block('SPECIFIC MODEL PREDICTION'):
    all_models = predictor.get_model_names()
    
    for model_name in all_models:
        with block(f'USING MODEL {model_name}'):
            target_model = predictor._trainer.load_model(model_name)
            y_pred = predictor.predict(test_data_without_label, 
                                       model=target_model)
            print(y_pred)


# with block('INSPECT AND DEBUG'):
#     debug()