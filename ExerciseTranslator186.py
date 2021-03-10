# 1 - Example 1 -Translate Online
# from googletrans import Translator
# translator = Translator()
# print(translator.translate("Como vai?Eu sempre tenho dinheiro.", dest='en').text)
# print(translator.translate("Como vai?", dest='en').text)

# 2 - Example 2 -Translate Off Line There is a limite to translate
from translatte import Translator
translator = Translator(to_lang="ja")


try:
    with open('TextCopy.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open('./TextJapa.txt', mode='w') as my_file2:
            my_file2.write(translation)
except FileNotFoundError as e:
    print(' Check the path.')
