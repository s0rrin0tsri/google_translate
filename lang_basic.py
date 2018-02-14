#!/usr/bin/python

# To authenticate, download your json keyfile from your account.
# Once done, run the following command in a terminal, or set the
# export in your ~/.bashrc or ~/.profile
# export GOOGLE_APPLICATION_CREDENTIALS="/path/to/keyfile.json"

# Imports the Google Cloud client library
from google.cloud import translate

# Instantiates a client
translate_client = translate.Client()

# The text to translate
text = input('Text to translate?')
# The target language
target = input('Digraph for Language?')

# Translates some text into Arabic
translation = translate_client.translate(
    text,
    target_language=target)

print(u'Text: {}'.format(text))
print(u'Translation: {}'.format(translation['translatedText']))

