import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
import os

model = tf.keras.models.load_model('ai_image_detector.keras')

print("Testing a few training images...\n")

# Test a real image
real_imgs = os.listdir('dataset/train/real')[:3]
print("REAL images:")
for img_name in real_imgs:
    img_path = f'dataset/train/real/{img_name}'
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    
    prediction = model.predict(img_array, verbose=0)[0][0]
    print(f"  {img_name}: {prediction:.4f}")

print("\nAI-GENERATED images:")
ai_imgs = os.listdir('dataset/train/ai_generated')[:3]
for img_name in ai_imgs:
    img_path = f'dataset/train/ai_generated/{img_name}'
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    
    prediction = model.predict(img_array, verbose=0)[0][0]
    print(f"  {img_name}: {prediction:.4f}")
