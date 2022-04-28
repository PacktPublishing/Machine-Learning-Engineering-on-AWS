import json

from transformers import AutoModelForSequenceClassification
from transformers import Trainer
from transformers import TrainingArguments
from torch.nn import functional as F
from transformers import AutoTokenizer
from time import sleep


TOKENIZER = "distilbert-base-uncased-finetuned-sst-2-english"


def model_fn(model_dir):
    model = AutoModelForSequenceClassification.from_pretrained(model_dir)
    
    return model


def humanize_prediction(output):
    class_a, class_b = F.softmax(output[0][0], dim = 0).tolist()
    
    prediction = "-"
    
    if class_a > class_b:
        prediction = "NEGATIVE"

    else:
        prediction = "POSITIVE"
        
    
    return prediction


def predict_fn(input_data, model):
    # sleep(30)
    
    sentence = input_data['text']
    
    tokenizer = AutoTokenizer.from_pretrained(TOKENIZER)
    
    batch = tokenizer(
        [sentence],
        padding=True,
        truncation=True,
        max_length=512,
        return_tensors="pt"
    )

    output = model(**batch)

    prediction = humanize_prediction(output)
    
    return prediction


def input_fn(serialized_input_data, content_type='application/json'):  
    if content_type == 'application/json':
        input_data = json.loads(serialized_input_data)
        
        return input_data
    else:
        raise Exception('Unsupported Content Type')

    
def output_fn(prediction_output, accept='application/json'):
    if accept == 'application/json':
        return json.dumps(prediction_output), accept
    
    raise Exception('Unsupported Content Type')