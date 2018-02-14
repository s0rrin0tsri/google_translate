#!/usr/bin/python

# To authenticate, to Google you will need to 
# download your json keyfile from your account.
# Once done, run the following command in a terminal:
# export GOOGLE_APPLICATION_CREDENTIALS="/path/to/keyfile.json"
#
# Alternatively, set the export in your ~/.bashrc or ~/.profile
################################################################

# Imports the Google Cloud client library
from google.cloud import translate

# Instantiates a client
translate_client = translate.Client()

# The text to translate provided by the user
text = raw_input(u'Text to translate? ')
# text = u'What do you mean?'

# The target language as a two letter language code
# (e.g., en, ar, ru, fr, etc.)
target = raw_input(u'Digraph for Language? ')
# target = 'ar'

# Translates text into chosen language
translation = translate_client.translate(
    text,
    target_language=target)

print(u'Text: {}'.format(text))
print(u'Translation: {}'.format(translation['translatedText']))

