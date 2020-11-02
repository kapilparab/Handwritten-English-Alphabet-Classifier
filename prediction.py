from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os
import numpy as np

os.environ['TF_FORCE_GPU_ALLOW_GROWTH'] = 'true'

alphabets_mapper = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M',
                    13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}

# Load Model
model = load_model('./model/model.h5')

# Get Prediction
def predictAlphabet(img_path):

    # Convert image into a numpy array
    img = image.load_img(img_path, target_size=(28, 28), color_mode="grayscale")
    img_arr = image.img_to_array(img)
    img_arr = np.array([img_arr])

    # Predict
    result = model.predict(img_arr)
    
    # Return alphabet
    return alphabets_mapper[np.argmax(result[0])]