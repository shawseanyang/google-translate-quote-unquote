# Author: Shaw-Sean Yang

# Google "Translate"

# Takes your perfectly good input and spices it up using multiple layers of Google Translate

import random
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

INPUT = 'Today I dressed my unicorn in preparation for the race.'
INPUT_LANG_CODE = 'en'
LAYERS = 10

LANGUAGES = [{'code':'af','name':'Afrikaans'},{'code':'sq','name':'Albanian'},{'code':'am','name':'Amharic'},{'code':'ar','name':'Arabic'},{'code':'hy','name':'Armenian'},{'code':'az','name':'Azerbaijani'},{'code':'eu','name':'Basque'},{'code':'be','name':'Belarusian'},{'code':'bn','name':'Bengali'},{'code':'bs','name':'Bosnian'},{'code':'bg','name':'Bulgarian'},{'code':'ca','name':'Catalan'},{'code':'ceb','name':'Cebuano'},{'code':'ny','name':'Chichewa'},{'code':'zh-CN','name':'Chinese'},{'code':'co','name':'Corsican'},{'code':'hr','name':'Croatian'},{'code':'cs','name':'Czech'},{'code':'da','name':'Danish'},{'code':'nl','name':'Dutch'},{'code':'en','name':'English'},{'code':'eo','name':'Esperanto'},{'code':'et','name':'Estonian'},{'code':'tl','name':'Filipino'},{'code':'fi','name':'Finnish'},{'code':'fr','name':'French'},{'code':'fy','name':'Frisian'},{'code':'gl','name':'Galician'},{'code':'ka','name':'Georgian'},{'code':'de','name':'German'},{'code':'el','name':'Greek'},{'code':'gu','name':'Gujarati'},{'code':'ht','name':'Haitian Creole'},{'code':'ha','name':'Hausa'},{'code':'haw','name':'Hawaiian'},{'code':'iw','name':'Hebrew'},{'code':'hi','name':'Hindi'},{'code':'hmn','name':'Hmong'},{'code':'hu','name':'Hungarian'},{'code':'is','name':'Icelandic'},{'code':'ig','name':'Igbo'},{'code':'id','name':'Indonesian'},{'code':'ga','name':'Irish'},{'code':'it','name':'Italian'},{'code':'ja','name':'Japanese'},{'code':'jw','name':'Javanese'},{'code':'kn','name':'Kannada'},{'code':'kk','name':'Kazakh'},{'code':'km','name':'Khmer'},{'code':'rw','name':'Kinyarwanda'},{'code':'ko','name':'Korean'},{'code':'ku','name':'Kurdish (Kurmanji)'},{'code':'ky','name':'Kyrgyz'},{'code':'lo','name':'Lao'},{'code':'la','name':'Latin'},{'code':'lv','name':'Latvian'},{'code':'lt','name':'Lithuanian'},{'code':'lb','name':'Luxembourgish'},{'code':'mk','name':'Macedonian'},{'code':'mg','name':'Malagasy'},{'code':'ms','name':'Malay'},{'code':'ml','name':'Malayalam'},{'code':'mt','name':'Maltese'},{'code':'mi','name':'Maori'},{'code':'mr','name':'Marathi'},{'code':'mn','name':'Mongolian'},{'code':'my','name':'Myanmar (Burmese)'},{'code':'ne','name':'Nepali'},{'code':'no','name':'Norwegian'},{'code':'or','name':'Odia (Oriya)'},{'code':'ps','name':'Pashto'},{'code':'fa','name':'Persian'},{'code':'pl','name':'Polish'},{'code':'pt','name':'Portuguese'},{'code':'pa','name':'Punjabi'},{'code':'ro','name':'Romanian'},{'code':'ru','name':'Russian'},{'code':'sm','name':'Samoan'},{'code':'gd','name':'Scots Gaelic'},{'code':'sr','name':'Serbian'},{'code':'st','name':'Sesotho'},{'code':'sn','name':'Shona'},{'code':'sd','name':'Sindhi'},{'code':'si','name':'Sinhala'},{'code':'sk','name':'Slovak'},{'code':'sl','name':'Slovenian'},{'code':'so','name':'Somali'},{'code':'es','name':'Spanish'},{'code':'su','name':'Sundanese'},{'code':'sw','name':'Swahili'},{'code':'sv','name':'Swedish'},{'code':'tg','name':'Tajik'},{'code':'ta','name':'Tamil'},{'code':'tt','name':'Tatar'},{'code':'te','name':'Telugu'},{'code':'th','name':'Thai'},{'code':'tr','name':'Turkish'},{'code':'tk','name':'Turkmen'},{'code':'uk','name':'Ukrainian'},{'code':'ur','name':'Urdu'},{'code':'ug','name':'Uyghur'},{'code':'uz','name':'Uzbek'},{'code':'vi','name':'Vietnamese'},{'code':'cy','name':'Welsh'},{'code':'xh','name':'Xhosa'},{'code':'yi','name':'Yiddish'},{'code':'yo','name':'Yoruba'},{'code':'zu','name':'Zulu'}]

URL_TEMPLATE_STR = 'https://translate.google.com/m?hl=en&sl={prev_lang}&tl={new_lang}&ie=UTF-8&prev=_m&q={query}'

def gtranslate(prev_lang_code, new_lang_code, query):
    url = URL_TEMPLATE_STR.format(prev_lang=prev_lang_code, new_lang=new_lang_code, query=query)
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    result_class = ''

    if (soup.find(class_='t0') != None):
        result_class = 't0'
    elif (soup.find(class_='result-container') != None):
        result_class = 'result-container'
    else:
        print("Error: Failed translation from {} to {}".format(prev_lang_code, new_lang_code))
        return -1

    return soup.find(class_=result_class).text


def block_check(gtranslate_result):
    if (gtranslate_result == None or gtranslate_result == -1):
        raise RuntimeError("Error: Google Translate has detected that this is a script and prevented more translation requests, wait a few minutes and then try again.")


def main():

    prev_lang_code = INPUT_LANG_CODE
    buffer = INPUT

    for i in range(LAYERS):
        new_lang_num = random.randint(0, len(LANGUAGES) - 1 )
        new_lang_code = LANGUAGES[new_lang_num]['code']

        if (new_lang_code == INPUT_LANG_CODE):
            i = i - 1
            continue

        print("{}. {}".format(i+1, LANGUAGES[new_lang_num]['name']))

        buffer = quote(buffer)

        buffer = gtranslate(prev_lang_code, new_lang_code, buffer)
        block_check(buffer)

        prev_lang_code = new_lang_code;

        if (i%2 == 0):
            time.sleep(1)

    buffer = gtranslate(prev_lang_code, INPUT_LANG_CODE, buffer)
    block_check(buffer)

    print(buffer)


if __name__ == "__main__":
    # execute only if run as a script
    main()
