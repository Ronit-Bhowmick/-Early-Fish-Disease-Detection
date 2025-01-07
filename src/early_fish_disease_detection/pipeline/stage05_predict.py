import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image 


class PredictionPipeline:
    def __init__(self, filename):
        self.filename=filename


    def predict(self):
        
        model = load_model(os.path.join("artifacts", "training", "model.keras"))

        img_name = self.filename
        test_image = image.load_img(img_name, target_size=(224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        
        result = np.argmax(model.predict(test_image), axis=1)
        print(f"Prediction Result: {result[0]}")

        if result[0] == 0:
            prediction = "Bacterial diseases - Aeromoniasis"
        
        elif result[0] == 1:
            prediction = "Bacterial gill disease"
        
        elif result[0] == 2:
            prediction = "Bacterial Red disease"
        
        elif result[0] == 3:
            prediction = "Fungal disease Saprolegniasis"
        
        elif result[0] == 4:
            prediction = "Healthy Fish"
        
        elif result[0] == 5:
            prediction = "Parasitic Fish"
        
        elif result[0] == 6:
            prediction = "Viral diseases White tail disease"
        

        # Return prediction as a dictionary
        return [{"image": prediction}]
    
