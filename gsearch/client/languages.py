languages = ["am", "ar", "eu", "bn", "en-GB",
             "pt-BR", "bg", "ca", "chr", "hr", "cs", "da", "nl", "en", "et", "fil", "fi", "fr", "de", "el", "gu", "iw", "hi", "hu", "is", "id", "it", "ja", "kn", "ko", "lv", "lt", "ms", "ml", "mr", "no", "fa", "pl", "pt", "ro", "ru", "sr", "sk", "sl", "es", "sw", "sv", "ta", "te", "th", "tr", "uk", "ur", "vi", "zu"]
# languages taken from https://developers.google.com/admin-sdk/directory/v1/languages
# god I did not want to write this all down
# but here it is
# the fruits of my labor
# what a waste of time
# enjoy
def isLanguageSupported(language:str):
    return language in languages


if __name__ == "__main__":
    print("True: ")
    print(isLanguageSupported("en"))
    print("False: ")
    print(isLanguageSupported("cm"))
