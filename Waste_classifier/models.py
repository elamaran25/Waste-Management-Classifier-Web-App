import tensorflow as tf
import numpy as np
from PIL import Image
import io
import os
import base64

# Load your trained model once
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "waste_classifier.h5")

model = tf.keras.models.load_model(MODEL_PATH)

# Define your class labels in order
CLASS_NAMES = ['Organic','Recyclable']

def preprocess_image(image_bytes):
    # Load image, convert to grayscale or RGB as per your model, resize, normalize
    img = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    img = img.resize((224, 224))  # adjust size to your model input
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)  # batch dimension
    return img_array

def classify_image(image_bytes):
    img_array = preprocess_image(image_bytes)
    predictions = model.predict(img_array)
    class_idx = np.argmax(predictions[0])
    confidence = float(predictions[0][class_idx])
    return CLASS_NAMES[class_idx], confidence