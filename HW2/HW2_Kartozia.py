#Language Detection, Kartozia
import wikipedia
##nl_file = open('nl_ngram.txt', 'r', encoding='utf-8')
##bg_file = open('bg_ngram.txt', 'r', encoding='utf-8')
##es_file = open('es_ngram.txt', 'r', encoding='utf-8')
##hu_file = open('hu_ngram.txt', 'r', encoding='utf-8')
nl_freq = open('nl_freq.txt', 'r', encoding='utf-8')
bg_freq = open('bg_freq.txt', 'r', encoding='utf-8')
es_freq = open('es_freq.txt', 'r', encoding='utf-8')
hu_freq = open('hu_freq.txt', 'r', encoding='utf-8')

nl = nl_freq.readlines()
##nl1 = nl_file.readlines()

bg = bg_freq.readlines()
##bg1 = bg_file.readlines()

es = es_freq.readlines()
##es1 = es_file.readlines()

hu = hu_freq.readlines()
##hu1 = hu_file.readlines()

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
    wiki_texts[lang] = get_texts_for_lang(lang, 1)
    print(lang, len(wiki_texts[lang]))

for key,value in wiki_texts.items():
    ngram_detect(key, value)
    
def lang_check(text, language):
    lang = language.readlines()
    count = 0
    for line in lang:
        if l in text:
            count += 1
    percentage = (count/len(lang))*100
    return percentage

def whether_correct(lang, name, guess, answer):
    if (lang == guess) and (name == answer):
        return name +': ' + lang + 'Correct'
    elif (lang == guess) and (name != answer):
        return name +': ' + lang + 'Wrong'
        

def ngram_detect(key, value):
    correct = 0
    nl_file = open('nl_ngram.txt', 'r', encoding='utf-8')
    bg_file = open('bg_ngram.txt', 'r', encoding='utf-8')
    es_file = open('es_ngram.txt', 'r', encoding='utf-8')
    hu_file = open('hu_ngram.txt', 'r', encoding='utf-8')
    nl = lang_check(value, nl_file)
    bg = lang_check(value, bg_file)
    es = lang_check(value, es_file)
    hu = lang_check(value, hu_file)
    if nl == max(nl, bg, es, hu):
        if 'nl' == key:
            correct += 1
            return 'Dutch: ' + nl + '% Correct'
        else:
            return 'Dutch: ' + nl + '% Wrong'
    elif bg == max(nl, bg, es, hu):
        if 'bg' == key:
            correct += 1
            return 'Bulgarian: ' + bg + '% Correct'
        else:
            return 'Bulgarian ' + bg + '% Wrong'        
    elif es == max(nl, bg, es, hu):
        if 'es' == key:
            correct += 1
            return 'Spanish: ' + es + '% Correct'        
        else:
            return 'Spanish: ' + es + '% Wrong'
    elif hu == max(nl, bg, es, hu):
        if 'hu' == key:
            correct += 1
            return 'Hungarian: ' + hu + '% Correct'    
        else:
            return 'Hungarian: ' + hu + '% Wrong'
        
    

#def freq_detect(text):
nl_freq.close()
es_freq.close()
bg_freq.close()
hu_freq.close()
nl_file.close()
es_file.close()
bg_file.close()
hu_file.close()
