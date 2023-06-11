from src.services.translation_service import TranslationService

class TranslationController:
    def __init__(self):
        self.translation_service = TranslationService()

    def translate_text(self, text):
        return self.translation_service.translate(text)
