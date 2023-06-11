import string
from typing import Any, Text
from flask import Blueprint, jsonify, request
from src.controllers.translation_controller import TranslationController

translation_bp = Blueprint('translation', __name__)
controller = TranslationController()

@translation_bp.route('/translate', methods=['POST'])
def translate():
    try:
        input_text : Text  = request.json['text']
        translated_text = controller.translate_text(input_text)
        return jsonify({'translated_text': translated_text})
    except Exception as e:
        return jsonify({'error': 'Server Error'})
