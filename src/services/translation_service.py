import tensorflow as tf
from tensorflow import keras
import pickle

# Tokenizers
input_tokenizer = None  # Load the input tokenizer used during training
target_tokenizer = None  # Load the target tokenizer used during training

# Load the tokenizers used during training
with open("tokens/input_tokenizer.pkl", "rb") as file:
    input_tokenizer = pickle.load(file)

with open("tokens/target_tokenizer.pkl", "rb") as file:
    target_tokenizer = pickle.load(file)
    
model_path = 'models/sukuma-translation' 
model =  keras.models.load_model(model_path)

class TranslationService:
    def translate(self, text):
        try:
            # Perform translation using the TensorFlow model
            input_data = text
            
            print(input_data)
        
            max_input_length = max(len(sequence) for sequence in input_data)
        
            # Tokenize and preprocess the input text
            new_input_data = input_tokenizer.texts_to_sequences([input_data])
            new_input_data = keras.preprocessing.sequence.pad_sequences(new_input_data, maxlen=model.input_shape[1], padding='post')
            # new_input_data = keras.preprocessing.sequence.pad_sequences(new_input_data, maxlen=max_input_length, padding='post')

            # Perform translation using the loaded model
            predictions = model.predict(new_input_data)
            predicted_indexes = tf.argmax(predictions, axis=-1)
            predicted_texts = target_tokenizer.sequences_to_texts(predicted_indexes.numpy())
            
            # print(predicted_texts)
            
            # Get the first translation
            result = predicted_texts[0]  
            
            # Return the translated text 
            return result
        except Exception as e:
            print("Error: " + str(e))
            raise e
        finally:
            print("Translation for " + input_data + " is complete")