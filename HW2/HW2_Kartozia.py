#Language Detection, Kartozia
import wikipedia
import re

def get_texts_for_lang(lang, n=10): # функция для скачивания статей из википедии
    wikipedia.set_lang(lang)
    wiki_content = []
    pages = wikipedia.random(n)
    for page_name in pages:
        try:
            page = wikipedia.page(page_name)
        except wikipedia.exceptions.WikipediaException:
            print('Skipping page {}'.format(page_name))
            continue

        wiki_content.append('{}\n{}'.format(page.title, page.content.replace('==', '')))

    return wiki_content

wiki_texts = {}
for lang in ('nl', 'bg', 'es', 'hu', 'ru', 'de'): # испанский, венгерский, нидерландский и болгарский, русский и немецкий 
    wiki_texts[lang] = get_texts_for_lang(lang, 100)
    print(lang, len(wiki_texts[lang]))
    
def lang_check(text, language):
    lang = language.read()
    lang = lang.split()
    count = 0
    for l in lang:
        if l not in '0123456789':
            if l in text:
                count += 1
    percentage = (count/len(lang))*100
    return percentage

       
#ngram method
def ngram_detect(key, value):
    correct = 0
    nl_file = open('nl_ngram.txt', 'r', encoding='utf-8')
    bg_file = open('bg_ngram.txt', 'r', encoding='utf-8')
    es_file = open('es_ngram.txt', 'r', encoding='utf-8')
    hu_file = open('hu_ngram.txt', 'r', encoding='utf-8')
    for v in value:
        hu = lang_check(v, hu_file)
        es = lang_check(v, es_file)
        nl = lang_check(v, nl_file)
        bg = lang_check(v, bg_file)
        if nl == max(nl, bg, es, hu):
            if 'nl' == key:
                correct += 1
                return 'Ngram: Dutch: ' + str(nl) + '% Correct' 
            else:
                return 'Ngram: Dutch: ' + str(nl) + '% Wrong'       
        if es == max(nl, bg, es, hu):
            if 'es' == key:
                correct += 1
                return 'Ngram: Spanish: ' + str(es) + '% Correct'        
            else:
                return 'Ngram: Spanish: ' + str(es) + '% Wrong'
        if hu == max(nl, bg, es, hu):
            if 'hu' == key:
                correct += 1
                return 'Ngram: Hungarian: ' + str(hu) + '% Correct'    
            else:
                return 'Ngram: Hungarian: ' + str(hu) + '% Wrong'
        if bg == max(nl, bg, es, hu):
            if 'bg' == key:
               correct += 1
               return 'Ngram: Bulgarian: ' + str(bg) + '% Correct'
            else:
               return 'Ngram: Bulgarian ' + str(bg) + '% Wrong'
    nl_file.close()
    es_file.close()
    bg_file.close()
    hu_file.close()

#dic method
def freq_detect(key, value):
    correct = 0
    nl_freq = open('nl_freq.txt', 'r', encoding='utf-8')
    bg_freq = open('bg_freq.txt', 'r', encoding='utf-8')
    es_freq = open('es_freq.txt', 'r', encoding='utf-8')
    hu_freq = open('hu_freq.txt', 'r', encoding='utf-8')
    for v in value:
        hu = lang_check(v, hu_freq)
        es = lang_check(v, es_freq)
        nl = lang_check(v, nl_freq)
        bg = lang_check(v, bg_freq)
        if nl == max(nl, bg, es, hu):
            if 'nl' == key:
                correct += 1
                return 'Dic: Dutch: ' + str(nl) + '% Correct' 
            else:
                return 'Dic: Dutch: ' + str(nl) + '% Wrong'       
        if es == max(nl, bg, es, hu):
            if 'es' == key:
                correct += 1
                return 'Dic: Spanish: ' + str(es) + '% Correct'        
            else:
                return 'Dic: Spanish: ' + str(es) + '% Wrong'
        if hu == max(nl, bg, es, hu):
            if 'hu' == key:
                correct += 1
                return 'Dic: Hungarian: ' + str(hu) + '% Correct'    
            else:
                return 'Dic: Hungarian: ' + str(hu) + '% Wrong'
        if bg == max(nl, bg, es, hu):
            if 'bg' == key:
               correct += 1
               return 'Dic: Bulgarian: ' + str(bg) + '% Correct'
            else:
               return 'Dic: Bulgarian ' + str(bg) + '% Wrong'
    nl_freq.close()
    es_freq.close()
    bg_freq.close()
    hu_freq.close()

for key, value in wiki_texts.items():
    print(ngram_detect(key,value))
    print(freq_detect(key, value))
    

