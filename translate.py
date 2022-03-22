import googletrans

LANGS = {
    'English': 'en', 'French': 'fr', 'Spanish': 'es', 'Portuguese': 'pt', 
    'Italian': 'it', 'Russian': 'ru', 'Swedish': 'sv', 'Malayalam': 'ml', 
    'Dutch': 'nl', 'Arabic': 'ar', 'Turkish': 'tr', 'German': 'de', 
    'Tamil': 'ta', 'Danish': 'da', 'Kannada': 'kn', 'Greek': 'el', 'Hindi': 'hi'
}

class Translator:

    def __init__(self):
        self.translator = googletrans.Translator(service_urls=['translate.googleapis.com'])

    def toeng(self, text, src):
        res = self.translator.translate(text, src=LANGS[src], dest='en')
        return res.text

    def trnslt(self, text, src, dest):
        res = self.translator.translate(text, src=LANGS[src], dest=LANGS[dest])
        return res.text