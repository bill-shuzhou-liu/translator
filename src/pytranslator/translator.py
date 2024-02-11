import translators as ts
from cache3 import DiskCache

cache = DiskCache()
class Translator:
    def __init__(self, to_language = "en"):
        self.to_language = to_language

    # translate and cache it.
    def translate(self, input):
        try:
            input = input.strip()
            if cache.has_key(input):
                return cache.get(input)
            res = ts.translate_text(input, to_language=self.to_language)
            cache.set(input, res)
            return res
        except:
            return None
