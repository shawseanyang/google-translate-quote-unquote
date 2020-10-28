# Author: Shaw-Sean Yang

# Google "Translate"

# Takes your perfectly good input and spices it up using multiple layers of Google Translate

import random
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

LANGUAGES = ['af', 'sq', 'am', 'ar', 'hy', 'az', 'eu', 'be', 'bn', 'bs', 'bg', 'ca', 'ceb', 'ny', 'zh-CN', 'co', 'hr', 'cs', 'da', 'nl', 'en', 'eo', 'et', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gu', 'ht', 'ha', 'haw', 'iw', 'hi', 'hmn', 'hu', 'is', 'ig', 'id', 'ga', 'it', 'ja', 'jw', 'kn', 'kk', 'km', 'rw', 'ko', 'ku', 'ky', 'lo', 'la', 'lv', 'lt', 'lb', 'mk', 'mg', 'ms', 'ml', 'mt', 'mi', 'mr', 'mn', 'my', 'ne', 'no', 'or', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'sm', 'gd', 'sr', 'st', 'sn', 'sd', 'si', 'sk', 'sl', 'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta', 'tt', 'te', 'th', 'tr', 'tk', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy', 'xh', 'yi', 'yo', 'zu']
LAYERS = 10
INPUT_LANG = 'en'
INPUT = 'Good evening'
URL_TEMPLATE_STR = 'https://translate.google.com/m?hl=en&sl={prev_lang}&tl={new_lang}&ie=UTF-8&prev=_m&q={query}'

def gtranslate(prev_lang_code, new_lang_code):
    url = URL_TEMPLATE_STR.format(prev_lang=prev_lang_code, new_lang=new_lang_code, query=buffer)
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    return soup.find(class_='t0')

assert(LAYERS <= len(LANGUAGES))

prev_lang_code = INPUT_LANG
buffer = INPUT

for i in range(1):#len(LANGUAGES)):
    new_lang_num = i+20 #random.randint(0, len(LANGUAGES) - 1 )
    new_lang_code = LANGUAGES[new_lang_num]
    
    print(new_lang_code)
    
    buffer = quote(buffer)
    
    #buffer = gtranslate(prev_lang_code, new_lang_code)
    
    url = URL_TEMPLATE_STR.format(prev_lang=prev_lang_code, new_lang=new_lang_code, query=buffer)
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    
    result_class = ''
    
    if (soup.find(class_='t0') == None):
        if(soup.find(class_='result-container') == None):
            print(url)
            print(page.status_code)
            print(page.headers)
            print(prev_lang_code + " -> " + new_lang_code)
            print(soup.prettify())
            print('b')
            break
        else:
            result_class = 'result-container'
            print(soup.find(class_=result_class).text)
    else:
        result_class = 't0'
            
    
    buffer = soup.find(class_=result_class).text
    
    prev_lang_code = new_lang_code;

buffer = gtranslate(prev_lang_code, INPUT_LANG)
print(buffer)