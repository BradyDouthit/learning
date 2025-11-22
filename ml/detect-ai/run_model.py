import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import sys

# Load the trained model
print("Loading model...")
model = tf.keras.models.load_model('ai_image_detector.keras')
print("Model loaded successfully!\n")

def predict_image(img_path):
    # Load and preprocess the image
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    
    # Make prediction
    prediction = model.predict(img_array, verbose=0)[0][0]
    
    # Interpret result
    # Check your training output - usually alphabetical order:
    # 0 = ai_generated, 1 = real
    return prediction

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python test_image.py <path_to_image>")
        print("\nExample:")
        print("  python test_image.py dataset/train/real/image_0.png")
    else:
        img_path = sys.argv[1]
        print(f"Testing image: {img_path}")
        result = predict_image(img_path)
        print(f"Prediction: {result}")
