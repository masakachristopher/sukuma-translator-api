
# Translation API with Flask

## Overview

This is a Flask-based API that translates input text using a pre-trained TensorFlow model. The API accepts POST requests with input text and returns the translated output.

Translates english and swahili phrases to sukuma tribe language

## Installation

1. Clone the repository:
   ```shell
   git clone https://github.com/masakachristopher/translator-flask-server.git
   ```
2. Change directory to the root folder of your project:
   ```shell
   cd translator-flask-server
   ```
3. Create virtual environment
    ```shell
    python3 -m venv venv
    source venv/bin/activate
    ```
4. Install dependencies
    ```shell
    pip install -r requirements.txt
    ```
5. Download the model folder

    [Download `sukuma-translation` Folder](https://drive.google.com/drive/folders/14l-SYoR5Y2OyoS50nvo2lltoC3t5CCE6?usp=sharing)

5. Create folder with name `models` in the root folder and place the `sukuma-translation` folder inside it
    ```
    - Root
        - models
            - sukuma-translations
        - src
        - app
        // others root files or folders
    ```


## Usage

1. Run your app
    ```shell
    flask run
    ```
2. Make request
    - URL: http://localhost:5000/translate
    - Headers: `Content-Type: application/json`
    - Body (Json Payload)
        ```shell
        {
        "text": "water"
        }
        ```
        or

        ```shell
        {
        "text": "hapana"
        }
        ```
    - Response sample
        ```shell
        {
        "translated_text": "minze"
        }
        ```
3. Customize the model and translations:

    - If you want to use a different pre-trained TensorFlow model, replace the trans file with your own trained model. Update the file path in the Flask app accordingly.
    - If you want to modify the translations, update the target_texts_combined in the Flask app with your desired translations    
    
## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.