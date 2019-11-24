import io
import json
import time
import torch.nn
import torchvision.transforms as transforms
from PIL import Image
from flask import Flask, jsonify, request
from torchvision import models

# Declare flask app
APP = Flask(__name__)

# Description
DESCRIPTION = {
    "service-name": "imagenet-mobilenet-predictor-service",
    "description": "Pass a URL containing an image to /api/v1/predict and let's go !",
    "usage-example": "curl -X POST -F \"file=@cat.jpg\" {my-service-url}/api/v1/predict"
}

with open('index_to_classes.json', 'r') as f:
    CLASS_INDEXES = json.load(f)

# We load the model using existing weights
MODEL = models.mobilenet_v2(pretrained=True)
# Setup as eval
MODEL.eval()


def transform_image(image: Image):
    my_transforms = transforms.Compose([
        transforms.Resize(255),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    return my_transforms(image).unsqueeze(0)


def get_prediction(image: Image):
    tensor = transform_image(image=image)
    outputs = MODEL.forward(tensor)
    outputs = torch.nn.functional.softmax(outputs)
    y_proba, y_hat = outputs.max(1)
    predicted_idx = str(y_hat.item())
    return CLASS_INDEXES[predicted_idx][0], CLASS_INDEXES[predicted_idx][1], round(float(y_proba.detach().numpy()), 3)


@APP.route('/api/v1/health', methods=['GET'])
def health():
    return "HEALTH OK\n"


@APP.route('/api/v1/describe', methods=['GET'])
def describe():
    return jsonify(DESCRIPTION)


@APP.route('/api/v1/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        img_bytes = file.read()
        image = Image.open(io.BytesIO(img_bytes))
        t1 = time.time()
        class_id, class_name, y_hat = get_prediction(image=image)
        t2 = time.time()
        t = round(t2 - t1, 3)
        return jsonify({
            'class_id': class_id,
            'class_name': class_name,
            'confidence': y_hat,
            'prediction_time': float(t)
        })


if __name__ == '__main__':
    APP.run()
