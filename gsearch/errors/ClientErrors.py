import gsearch.client.languages as client_languages

class InvalidLanguage(Exception):
    def __init__(self, message, language):
        self.message = message
        # little language check
        if client_languages.isLanguageSupported(language):
            self.message = self.message + \
                f"\n{language} is supported, this is an error. Please raise an issue in the GitHub at: https://github.com/DankBoi293/gsearch.py."
        

    def __str__(self):
        
        return self.message
