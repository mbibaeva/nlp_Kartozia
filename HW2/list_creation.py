#Language Detection, Kartozia
import wikipedia
import codecs
import collections
import sys
import re
from itertools import islice, tee

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
for lang in ('nl', 'bg', 'es', 'hu'): # испанский, венгерский, нидерландский и болгарский 
    wiki_texts[lang] = get_texts_for_lang(lang, 100)
    print(lang, len(wiki_texts[lang]))

##print(wiki_texts['nl'][0]) # распечатаем пару текстов
##print(wiki_texts['bg'][0])
#частотный список
def tokenize(text): 
    return text.split(' ')

def freq_list(corpus, arr):
    freqs = collections.defaultdict(lambda: 0)
    for article in corpus:
        for word in tokenize(article.replace('\n', '').lower()):
            word = word.strip('"!?«».,:;№[]&%=-)({}+"\\')
            word1 = word.replace('–', '')
            nword = re.sub('\d', '', word1)
            if nword != '':
                freqs[nword] += 1
    for word in sorted(freqs, key=lambda w: freqs[w], reverse=True):
        arr.append('{}\t{}'.format(freqs[word], word))
    return arr
        
#nl
nl_freq = open('nl_freq.txt', 'w', encoding='utf-8')
nl = wiki_texts['nl']
nl_list = []
freq_list(nl, nl_list)
    
#bg
bg_freq = open('bg_freq.txt', 'w', encoding='utf-8')
bg = wiki_texts['bg']
bg_list = []
freq_list(bg, bg_list)
for b in bg_list:
    bg_freq.write(b + '\n')

#es
es_freq = open('es_freq.txt', 'w', encoding='utf-8')
es = wiki_texts['es']
es_list = []
freq_list(es, es_list)

#hu
hu_freq = open('hu_freq.txt', 'w', encoding='utf-8')
hu = wiki_texts['hu']
hu_list = []
freq_list(hu, hu_list)

#повторения
for n in nl_list:
    if (n not in es_list) and (n not in hu_list):
        nl_freq.write(n + '\n')
        
for h in hu_list:
    if (h not in es_list) and (h not in nl_list):
        hu_freq.write(h + '\n')

for e in es_list:
    if (e not in nl_list) and (e not in hu_list):
        es_freq.write(e + '\n')
  
#частотные символьные n-граммы

def make_ngrams(text):
    N = 3 # задаем длину n-граммы
    ngrams = zip(*(islice(seq, index, None) for index, seq in enumerate(tee(text, N))))
    ngrams = [''.join(x) for x in ngrams]
    return ngrams

def ngram_freq(corpus, arr):
    freqs = collections.defaultdict(lambda: 0)
    for article in corpus:
        for ngram in make_ngrams(article.replace('\n', '').lower()):
            ngram = ngram.strip('"!?«».,:;№[]&%=-)({}+"\\/')
            word1 = ngram.replace('–', '')
            word2 = re.sub('\d', '', word1)
            word3 = re.sub(',', '', word2)
            nword = re.sub('\s', '', word3)
            if len(nword)>2:
                freqs[nword] += 1
    for ngram in sorted(freqs, key=lambda n: freqs[n], reverse=True):
        arr.append('{}\t{}'.format(freqs[ngram], ngram))
    return arr
#nl
nl_file = open('nl_ngram.txt', 'w', encoding='utf-8')
nl_ngram = []
ngram_freq(nl, nl_ngram)

#es
es_file = open('es_ngram.txt', 'w', encoding='utf-8')
es_ngram = []   
ngram_freq(es, es_ngram)

#bg
bg_file = open('bg_ngram.txt', 'w', encoding='utf-8')
bg_ngram = []
ngram_freq(bg, bg_ngram)
for b in bg_ngram:
    bg_file.write(b + '\n')
#hu
hu_file = open('hu_ngram.txt', 'w', encoding='utf-8')
hu_ngram = []
ngram_freq(hu, hu_ngram)

#повторения
for n in nl_ngram:
    if (n not in es_ngram) and (n not in hu_ngram):
        nl_file.write(n + '\n')
        
for h in hu_ngram:
    if (h not in es_ngram) and (h not in nl_ngram):
        hu_file.write(h + '\n')

for e in es_ngram:
    if (e not in nl_ngram) and (e not in hu_ngram):
        es_file.write(e + '\n')


nl_freq.close()
es_freq.close()
bg_freq.close()
hu_freq.close()
nl_file.close()
es_file.close()
bg_file.close()
hu_file.close()
