import os
import torch


def prepare_model():
    model = torch.nn.Sequential(
        torch.nn.Linear(1, 100),
        torch.nn.Dropout(0.01),
        torch.nn.ReLU(),
        torch.nn.Linear(100, 100),
        torch.nn.Dropout(0.01),
        torch.nn.ReLU(),
        torch.nn.Linear(100, 100),
        torch.nn.Dropout(0.01),
        torch.nn.ReLU(),
        torch.nn.Linear(100, 1),
    )
        
    return model


def load_model(model_dir):
    model = prepare_model()
    
    path = os.path.join(model_dir, 'model.pth')
    model.load_state_dict(torch.load(path))
    model.eval()
    
    return model


def predict(model, x):
    output = None

    with torch.no_grad():
        output = model(torch.Tensor([x]))

    return output.numpy()[0]


def handler(event, context):
    model = load_model("model")
    
    x = event.get('queryStringParameters',{}).get('x', 0)
    y = predict(model, float(x))
    
    return str(y)
    

"""    
if __name__ == "__main__":
    event = {
        'queryStringParameters': {
            'x': 42
        }
    }
    
    output = handler(event, context={})
    print(output)
"""