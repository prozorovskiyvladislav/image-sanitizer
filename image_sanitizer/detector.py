import tensorflow as tf
import numpy as np
from PIL import Image
import requests
import io
import os

class ImageSanitizer:
    def __init__(self, model_path=None):
        """Ініціалізуємо класифікатор"""
        self.model = self.load_model(model_path)

    def load_model(self, model_path):
        """Завантажуємо модель класифікації"""
        if model_path and os.path.exists(model_path):
            return tf.keras.models.load_model(model_path)
        else:
            raise ValueError("Не знайдено модель для класифікації")

    def preprocess_image(self, image):
        """Обробляємо зображення перед передачею в модель"""
        image = image.resize((224, 224))  # Змінюємо розмір під модель
        image = np.array(image) / 255.0   # Масштабуємо
        image = np.expand_dims(image, axis=0)  # Додаємо batch dimension
        return image

    def classify(self, image_path):
        """Перевіряє зображення, повертає NSFW або Safe"""
        image = Image.open(image_path)
        image = self.preprocess_image(image)
        prediction = self.model.predict(image)

        return "NSFW" if prediction[0][0] > 0.5 else "Safe"

    def classify_url(self, image_url):
        """Перевіряє зображення за URL"""
        response = requests.get(image_url)
        image = Image.open(io.BytesIO(response.content))
        return self.classify(image)
