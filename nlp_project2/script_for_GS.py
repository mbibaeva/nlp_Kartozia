import re

def change_tags(tags, pos, wordform, lemma):
    tags_ch = str(wordform) + '\t' + str(lemma) + '\t'
    if pos == 'N':
        tags_ch += 'S\t'
        n_tags_1 = {'c': 'common', 'p': 'proper'}
        n_tags_2 = {'m': 'm', 'f': 'f', 'n': 'n', 'c': 'c'}#, '-':''}
        n_tags_3 = {'s': 'sg', 'p': 'pl'}
        n_tags_4 = {'n': 'nom', 'g': 'gen', 'd': 'dat', 'a': 'acc', 'v': 'voc',
                    'l': 'loc', 'i': 'ins'}
        n_tags_5 = {'n': 'non-animate', 'y': 'animate'}
        n_tags_6 = {'p': 'part', 'l': 'loc'}
        if tags[1] in n_tags_2:
            tags_ch += tags[1]
        if tags[3] in n_tags_4:
            tags_ch += ','
            tags_ch += str(n_tags_4[tags[3]])
            if len(tags) > 5:
                if tags[5] in n_tags_6:
                    tags_ch += '/'
                    tags_ch += str(n_tags_6[tags[5]])
        if tags[2] in n_tags_3:
            tags_ch += ','
            tags_ch += str(n_tags_3[tags[2]])
        #if tags[4] in n_tags_5:
        #    tags_ch += ','
        #    tags_ch += 'Animate='
        #    tags_ch += str(n_tags_5[tags[4]])
        return tags_ch
    elif pos == 'V':
        tags_ch += 'V\t'
        v_tags_1 = {'m':'main', 'a':'auxiliary'}
        v_tags_2 = {'i':'indicative', 'm':'imper', 'c':'cond', 'n':'inf',
                    'p':'partcp', 'g':'ger'}
        v_tags_3 = {'p':'pres', 'f':'fut', 's':'past'}
        v_tags_4 = {'1':'1p', '2':'2p', '3':'3p'}
        v_tags_5 = {'s':'sg', 'p':'pl'}
        v_tags_6 = {'m':'m', 'f': 'f', 'n': 'n'}
        v_tags_7 = {'a':'act', 'p':'pass'}
        v_tags_8 = {'s':'brev', 'f':'full-art'}
        v_tags_9 = {'p':'progressive', 'e':'perfective', 'b':'biaspectual'}
        v_tags_10 = {'n': 'nom', 'g': 'gen', 'd': 'dat', 'a': 'acc', 'v': 'voc',
                    'l': 'loc', 'i': 'ins'}
        if tags[1] in v_tags_2:
            if v_tags_2[tags[1]] == 'inf':
                tags_ch += 'inf'
                return tags_ch
            else:
                if tags[7] in v_tags_8 and v_tags_8[tags[7]] == 'brev':
                    tags_ch += v_tags_8[tags[7]]
                    tags_ch += ','
                if tags[3] in v_tags_4:
                    tags_ch += str(v_tags_4[tags[3]]) #лицо
                    tags_ch += ','
                if v_tags_2[tags[1]] == 'indicative':
                    if tags[2] in v_tags_3: #время
                        tags_ch += str(v_tags_3[tags[2]])
                        tags_ch += ','
                    if tags[5] in v_tags_6:
                        tags_ch += str(v_tags_6[tags[5]])
                        tags_ch += ','
                elif v_tags_2[tags[1]] == 'partcp':
                    if tags[6] in v_tags_7: #залог
                        tags_ch += str(v_tags_7[tags[6]])
                        tags_ch += ','
                    if len(tags) > 9:
                        if tags[9] in v_tags_10:
                            tags_ch += str(v_tags_10[tags[9]])
                            tags_ch += ','
                    tags_ch += v_tags_2[tags[1]]
                    tags_ch += ','
                    if tags[2] in v_tags_3: #время
                        tags_ch += str(v_tags_3[tags[2]])
                        tags_ch += ','
                elif v_tags_2[tags[1]] == 'ger':
                    tags_ch += v_tags_2[tags[1]]
                    tags_ch += ','
                    if tags[2] in v_tags_3: #время
                        tags_ch += str(v_tags_3[tags[2]])
                        tags_ch += ','
                else:
                    tags_ch += v_tags_2[tags[1]] #imperative
                    tags_ch += ','
        if tags[4] in v_tags_5: #число
            tags_ch += str(v_tags_5[tags[4]])
        return tags_ch
    elif pos == 'A':
        tags_ch += 'A\t'
        a_tags_1 = {'f':'qual', 's':'poss'}
        a_tags_2 = {'c':'comp', 's':'supr'}
        a_tags_3 = {'m':'ma', 'f': 'f', 'n': 'n'}
        a_tags_4 = {'s':'sg', 'p':'pl'}
        a_tags_5 = {'n': 'nom', 'g': 'gen', 'd': 'dat', 'a': 'acc', 'v': 'voc',
                    'l': 'loc', 'i': 'ins'}
        a_tags_6 = {'s':'short-art', 'f':'full-art', '-':'none'}
        if tags[1] in a_tags_2:
            tags_ch += str(a_tags_2[tags[1]])
            tags_ch += ','
        if tags[4] in a_tags_5: # падеж
            tags_ch += str(a_tags_5[tags[4]])
            tags_ch += ','
        if tags[3] in a_tags_4: # число
            if a_tags_4[tags[3]] == 'sg':
                if tags[2] in a_tags_3: # род
                    tags_ch += str(a_tags_3[tags[2]])
                    tags_ch += ','
            tags_ch += str(a_tags_4[tags[3]]) # число
        return tags_ch
    elif pos == 'P':
        p_tags_1 = {'p':'personal', 'd':'demonstrative', 'i':'indefinite', 's':'possessive',
                    'q':'interrogative', 'r':'relative', 'x':'reflexive', 'z':'negative',
                    'n':'nonspecific'}
        p_tags_2 = {'1':'1p', '2':'2p', '3':'3p'}
        p_tags_3 = {'m':'m', 'f': 'f', 'n': 'n'}
        p_tags_4 = {'s':'sg', 'p':'pl'}
        p_tags_5 = {'n': 'nom', 'g': 'gen', 'd': 'dat', 'a': 'acc', 'v': 'voc',
                    'l': 'loc', 'i': 'ins'}
        p_tags_6 = {'n':'SPRO', 'a':'APRO', 'r':'ADVPRO'}
        p_tags_7 = {'n':'animate', 'y':'non-animate'}
        if tags[5] in p_tags_6:
            tags_ch += p_tags_6[tags[5]]
            tags_ch += '\t'
            if p_tags_6[tags[5]] != 'ADVPRO':
                if tags[1] in p_tags_2: #лицо
                    tags_ch += str(p_tags_2[tags[1]])
                    tags_ch += ','
                if tags[4] in p_tags_5: #падеж
                    tags_ch += str(p_tags_5[tags[4]])
                    tags_ch += ','
                if tags[2] in p_tags_3: # род
                    tags_ch += str(p_tags_3[tags[2]])
                    tags_ch += ','
                if tags[3] in p_tags_4: #число
                    tags_ch += str(p_tags_4[tags[3]])
        #if tags[0] in p_tags_1:
        #    tags_ch += 'Type='
        #    tags_ch += str(p_tags_1[tags[0]])
        #if len(tags) > 6:
        #    if tags[6] in p_tags_7:
        #        tags_ch += ','
        #        tags_ch += 'Animate='
        #        tags_ch += str(p_tags_7[tags[6]])
        return tags_ch
    elif pos == 'R':
        tags_ch += 'ADV\t'
        r_tags_1 = {'c':'comp', 's':'supr'}
        if tag[0] in r_tags_1:
            tags_ch += str(r_tags_1[tags[0]])
        return tags_ch
    
    elif pos == 'S':
        tags_ch += 'PR\t'
        s_tags_1 = {'p':'preposition'}
        s_tags_2 = {'s':'simple', 'c':'compound'}
        s_tags_3 = {'n': 'nom', 'g': 'gen', 'd': 'dat', 'a': 'acc', 'v': 'voc',
                    'l': 'loc', 'i': 'ins'}
        #if tags[0] in s_tags_1:
        #    tags_ch += 'Type='
        #    tags_ch += str(s_tags_1[tags[0]])
        #if tags[1] in s_tags_2:
        #    tags_ch += ','
        #    tags_ch += 'Formation='
        #    tags_ch += str(s_tags_2[tags[1]])
        #if tags[2] in s_tags_3:
        #    tags_ch += ','
        #    tags_ch += 'Case='
        #    tags_ch += str(s_tags_3[tags[2]])
        return tags_ch
    elif pos == 'C':
        tags_ch += 'CONJ\t'
        c_tags_1 = {'c':'coordinating', 's':'subordinating'}
        c_tags_2 = {'s':'simple', 'c':'compound'}
        c_tags_3 = {'p':'sentence', 'w':'words'}
        c_tags_4 = {'z': 'negative', 'p':'positive'}
        #if len(tags) > 0:
        #    tags_ch += ':'
        #    if tags[0] in c_tags_1:
        #        tags_ch += 'Type='
        #        tags_ch += str(c_tags_1[tags[0]])
        #    if tags[1] in c_tags_2:
        #        tags_ch += ','
        #        tags_ch += 'Formation='
        #        tags_ch += str(c_tags_2[tags[1]])
        #    if tags[2] in c_tags_3:
        #        tags_ch += ','
        #        tags_ch += 'Coord_Type='
        #        tags_ch += str(c_tags_3[tags[2]])
        #    if tags[3] in c_tags_4:
        #        tags_ch += ','
        #        tags_ch += 'Sub_Type='
        #        tags_ch += str(c_tags_4[tags[3]])
        return tags_ch
    
    elif pos == 'M':
        tags_ch += 'ANUM\t'
        m_tags_1 = {'c':'cardinal', 'o':'ordinal', 'm':'multiple', 'l':'collect'}
        m_tags_2 = {'m':'m', 'f': 'f', 'n': 'n'}
        m_tags_3 = {'s':'sg', 'p':'pl'}
        m_tags_4 = {'n': 'nom', 'g': 'gen', 'd': 'dat', 'a': 'acc', 'v': 'voc',
                    'l': 'loc', 'i': 'ins'}
        m_tags_5 = {'d':'digit', 'r':'roman', 'l':'letter'}
        m_tags_6 = {'n':'non-animate', 'y':'animate'}
        if tags[3] in m_tags_4: # ПАДЕЖ
            tags_ch += str(m_tags_4[tags[3]])
            tags_ch += ','
        if tags[1] in m_tags_2: # РОД
            tags_ch += str(m_tags_2[tags[1]])
            tags_ch += ','
        #if tags[0] in m_tags_1:
        #    tags_ch += 'Type='
        #    tags_ch += str(m_tags_1[tags[0]])
        if tags[2] in m_tags_3: # ЧИСЛО
            tags_ch += str(m_tags_3[tags[2]])
        #if len(tags) > 4:
        #    if tags[4] in m_tags_5:
        #        tags_ch += ','
        #        tags_ch += 'Form='
        #        tags_ch += str(m_tags_5[tags[4]])
        #    if len(tags) > 5:
        #        if tags[5] in m_tags_6:
        #            tags_ch += ','
        #            tags_ch += 'Case='
        #           tags_ch += str(m_tags_6[tags[5]])
        return tags_ch
    elif pos == 'Q':
        tags_ch += 'PART\t'
        q_tags_1 = {'s':'simple', 'c':'compound'}
        #if len(tags) > 0:
        #    if tags[0] in q_tags_1:
        #        tags_ch += ':Formation='
        #        tags_ch += str(q_tags_1[tags[0]])
        return tags_ch
    elif pos == 'I':
        tags_ch = 'INTJ\t'
        #i_tags_1 = {'s':'simple', 'c':'compound'}
        #if len(tags) > 0:
        #    if tags[0] in i_tags_1:
        #        tags_ch += ':Formation='
        #        tags_ch += str(i_tags_1[tags[0]])
        return tags_ch
    elif pos == 'Y':
        tags_ch = 'Abbr\t'
        #y_tags_1 = {'n':'nominal', 'r':'adverbial'}
        #y_tags_2 = {'m':'masculine', 'f': 'feminine', 'n': 'neuter', '-':'none'}
        #y_tags_3 = {'s':'singular', 'p':'plural', '-':'none'}
        #y_tags_4 = {'n': 'Nom', 'g': 'Gen', 'd': 'Dat', 'a': 'Acc', 'l': 'Loc', 'i': 'Instr', '-':'none'}          
        #if len(tags) > 0:
        #    tags_ch += ':'
        #    if tags[0] in y_tags_1:
        #        tags_ch += 'Syntactic_Type='
        #        tags_ch += str(y_tags_1[tags[0]])
        #    if tags[1] in y_tags_2:
        #        tags_ch += ','
        #        tags_ch += 'Gender='
        #        tags_ch += str(y_tags_2[tags[1]])
        #    if tags[2] in y_tags_3:
        #        tags_ch += ','
        #        tags_ch += 'Number='
        #        tags_ch += str(y_tags_3[tags[2]])
        #    if tags[3] in y_tags_4:
        #       tags_ch += ','
        #        tags_ch += 'Case='
        #        tags_ch += str(y_tags_4[tags[3]])
        return tags_ch
    elif pos == 'X':
        tags_ch = '\t'
        return tags_ch
    else:
        return None
outfile = open('test_annotated_gold_500_words.txt', 'w', encoding = 'utf-8')
with open('test_parsed_gold_500_words.txt', encoding = 'utf-8') as f:
    text = f.readlines()
for line in text:
    tag = line.split()
    if len(tag) < 4:
        tag.append('')
    tags = change_tags(tag[3], tag[2], tag[0], tag[1])
    outfile.write(str(tags) + '\n')
outfile.close()
