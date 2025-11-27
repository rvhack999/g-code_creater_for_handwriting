import os
from PIL import Image

class SymbolLoader:
    def __init__(self, letter_dir='letters'):
        self.BASE_SYMBOL_SIZE = (50, 50)
        self.NUM_VARIANTS = 5
        self.LETTER_DIR = letter_dir
        self.symbols = self.load_symbols()

    def load_symbols(self):
        """Загрузка всех образов символов"""
        symbols = {}
        supported_symbols = [
            'абвгдежзиклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ',
            'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
            '0123456789',
            '.,:;?!()[]{}<>+-*/%=~^@#$&\'\" '
        ]
        all_symbols = ''.join(supported_symbols)
        
        for sym in all_symbols:
            variants = []
            for i in range(self.NUM_VARIANTS):
                filename = f"{sym}_{i+1}.png"
                path = os.path.join(self.LETTER_DIR, filename)
                if os.path.exists(path):
                    variant = Image.open(path).resize(self.BASE_SYMBOL_SIZE)
                    variants.append(variant)
            symbols[sym] = variants
        return symbols