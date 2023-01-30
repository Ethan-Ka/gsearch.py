from gsearch import *
import gsearch.client.languages as languages
from gsearch.errors import ClientErrors as ClientErrors
class client:
    def __init__(self, language):
        if languages.isLanguageSupported(language):
            self.language = language
        else:
            raise ClientErrors.InvalidLanguage(f"{language} is not supported.")