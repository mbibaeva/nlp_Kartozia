import re

def change_tags(tags, pos):
    if pos == 'N':
        tags_ch = 'Noun:'
        n_tags_1 = {'c': 'common', 'p': 'proper'}
        n_tags_2 = {'m': 'masculine', 'f': 'feminine', 'n': 'neuter', 'c': 'common'}
        n_tags_3 = {'s': 'singular', 'p': 'plural'}
        n_tags_4 = {'n': 'Nom', 'g': 'Gen', 'd': 'Dat', 'a': 'Acc', 'v': 'Voc',
                    'l': 'Loc', 'i': 'Instr'}
        n_tags_5 = {'n': 'non-animate', 'y': 'animate'}
        n_tags_6 = {'p': 'partitive', 'l': 'locative'}
        if tags[0] in n_tags_1:
            tags_ch += 'Type='
            tags_ch += str(n_tags_1[tags[0]])
        if tags[1] in n_tags_2:
            tags_ch += ','
            tags_ch += 'Gender='
            tags_ch += str(n_tags_2[tags[1]])
        if tags[2] in n_tags_3:
            tags_ch += ','
            tags_ch += 'Number='
            tags_ch += str(n_tags_3[tags[2]])
        if tags[3] in n_tags_4:
            tags_ch += ','
            tags_ch += 'Case='
            tags_ch += str(n_tags_4[tags[3]])
        if tags[4] in n_tags_5:
            tags_ch += ','
            tags_ch += 'Animate='
            tags_ch += str(n_tags_5[tags[4]])
        if len(tags) > 5:
            if tags[5] in n_tags_6:
                tags_ch += ','
                tags_ch += 'Case2='
                tags_ch += str(n_tags_6[tags[5]])
        return tags_ch
    elif pos == 'V':
        tags_ch = 'Verb:'
        v_tags_1 = {'m':'main', 'a':'auxiliary'}
        v_tags_2 = {'i':'indicative', 'm':'imperative', 'c':'conditional', 'n':'infinitive',
                    'p':'participle', 'g':'gerund'}
        v_tags_3 = {'p':'present', 'f':'future', 's':'past'}
        v_tags_4 = {'1':'first', '2':'second', '3':'third', '-':'none'}
        v_tags_5 = {'s':'singular', 'p':'plural', '-':'none'}
        v_tags_6 = {'m':'masculine', 'f': 'feminine', 'n': 'neuter', '-':'none'}
        v_tags_7 = {'a':'active', 'p':'passive', 'm':'medial', '-':'none'}
        v_tags_8 = {'s':'short-art', 'f':'full-art', '-':'none'}
        v_tags_9 = {'p':'progressive', 'e':'perfective', 'b':'biaspectual'}
        v_tags_10 = {'n': 'Nom', 'g': 'Gen', 'd': 'Dat', 'a': 'Acc', 'l': 'Loc', 'i': 'Instr'}
        if tags[0] in v_tags_1:
            tags_ch += 'Type='
            tags_ch += str(v_tags_1[tags[0]])
        if tags[1] in v_tags_2:
            tags_ch += ','
            tags_ch += 'VForm='
            tags_ch += str(v_tags_2[tags[1]])
        if tags[2] in v_tags_3:
            tags_ch += ','
            tags_ch += 'Tense='
            tags_ch += str(v_tags_3[tags[2]])
        if tags[3] in v_tags_4:
            tags_ch += ','
            tags_ch += 'Person='
            tags_ch += str(v_tags_4[tags[3]])
        if tags[4] in v_tags_5:
            tags_ch += ','
            tags_ch += 'Number='
            tags_ch += str(v_tags_5[tags[4]])
        if tags[5] in v_tags_6:
            tags_ch += ','
            tags_ch += 'Gender='
            tags_ch += str(v_tags_6[tags[5]])
        if tags[6] in v_tags_7:
            tags_ch += ','
            tags_ch += 'Voice='
            tags_ch += str(v_tags_7[tags[6]])
        if tags[7] in v_tags_8:
            tags_ch += ','
            tags_ch += 'Definiteness='
            tags_ch += str(v_tags_8[tags[7]])
        if tags[8] in v_tags_9:
            tags_ch += ','
            tags_ch += 'Aspect='
            tags_ch += str(v_tags_9[tags[8]])
        if len(tags) > 9:
            if tags[9] in v_tags_10:
                tags_ch += ','
                tags_ch += 'Case='
                tags_ch += str(v_tags_10[tags[9]])
        return tags_ch
    elif pos == 'A':
        tags_ch = 'Adjective:'
        a_tags_1 = {'f':'qualificative', 's':'posseissive'}
        a_tags_2 = {'p':'positive', 'c':'comparative', 's':'superlative'}
        a_tags_3 = {'m':'masculine', 'f': 'feminine', 'n': 'neuter', '-':'none'}
        a_tags_4 = {'s':'singular', 'p':'plural', '-':'none'}
        a_tags_5 = {'n': 'Nom', 'g': 'Gen', 'd': 'Dat', 'a': 'Acc', 'l': 'Loc', 'i': 'Instr', '-':'none'}
        a_tags_6 = {'s':'short-art', 'f':'full-art', '-':'none'}
        if tags[0] in a_tags_1:
            tags_ch += 'Type='
            tags_ch += str(a_tags_1[tags[0]])
        if tags[1] in a_tags_2:
            tags_ch += ','
            tags_ch += 'Degree='
            tags_ch += str(a_tags_2[tags[1]])
        if tags[2] in a_tags_3:
            tags_ch += ','
            tags_ch += 'Gender='
            tags_ch += str(a_tags_3[tags[2]])
        if tags[3] in a_tags_4:
            tags_ch += ','
            tags_ch += 'Number='
            tags_ch += str(a_tags_4[tags[3]])
        if tags[4] in a_tags_5:
            tags_ch += ','
            tags_ch += 'Case='
            tags_ch += str(a_tags_5[tags[4]])
        if tags[5] in a_tags_6:
            tags_ch += ','
            tags_ch += 'Definiteness='
            tags_ch += str(a_tags_6[tags[5]])
        return tags_ch
    elif pos == 'P':
        tags_ch = 'Pronoun:'
        p_tags_1 = {'p':'personal', 'd':'demonstrative', 'i':'indefinite', 's':'possessive',
                    'q':'interrogative', 'r':'relative', 'x':'reflexive', 'z':'negative',
                    'n':'nonspecific'}
        p_tags_2 = {'1':'first', '2':'second', '3':'third', '-':'none'}
        p_tags_3 = {'m':'masculine', 'f': 'feminine', 'n': 'neuter', '-':'none'}
        p_tags_4 = {'s':'singular', 'p':'plural', '-':'none'}
        p_tags_5 = {'n': 'Nom', 'g': 'Gen', 'd': 'Dat', 'a': 'Acc', 'l': 'Loc', 'i': 'Instr', '-':'none'}
        p_tags_6 = {'n':'nominal', 'a':'adjectival', 'r':'adverbial'}
        p_tags_7 = {'n':'animate', 'y':'non-animate'}
        if tags[0] in p_tags_1:
            tags_ch += 'Type='
            tags_ch += str(p_tags_1[tags[0]])
        if tags[1] in p_tags_2:
            tags_ch += ','
            tags_ch += 'Person='
            tags_ch += str(p_tags_2[tags[1]])
        if tags[2] in p_tags_3:
            tags_ch += ','
            tags_ch += 'Gender='
            tags_ch += str(p_tags_3[tags[2]])
        if tags[3] in p_tags_4:
            tags_ch += ','
            tags_ch += 'Number='
            tags_ch += str(p_tags_4[tags[3]])
        if tags[4] in p_tags_5:
            tags_ch += ','
            tags_ch += 'Case='
            tags_ch += str(p_tags_5[tags[4]])
        if tags[5] in p_tags_6:
            tags_ch += ','
            tags_ch += 'Syntactic_Type='
            tags_ch += str(p_tags_6[tags[5]])
        if len(tags) > 6:
            if tags[6] in p_tags_7:
                tags_ch += ','
                tags_ch += 'Animate='
                tags_ch += str(p_tags_7[tags[6]])
        return tags_ch
    elif pos == 'R':
        tags_ch = 'Adverb'
        r_tags_1 = {'p':'positive', 'c':'comparative', 's':'superlative'}
        if tag[0] in r_tags_1:
            tags_ch += ':Degree'
            tags_ch += str(r_tags_1[tags[0]])
        return tags_ch
    elif pos == 'S':
        tags_ch = 'Adposition:'
        s_tags_1 = {'p':'preposition'}
        s_tags_2 = {'s':'simple', 'c':'compound'}
        s_tags_3 = {'g': 'Gen', 'd': 'Dat', 'a': 'Acc', 'l': 'Loc', 'i': 'Instr', '-':'none'}
        if tags[0] in s_tags_1:
            tags_ch += 'Type='
            tags_ch += str(s_tags_1[tags[0]])
        if tags[1] in s_tags_2:
            tags_ch += ','
            tags_ch += 'Formation='
            tags_ch += str(s_tags_2[tags[1]])
        if tags[2] in s_tags_3:
            tags_ch += ','
            tags_ch += 'Case='
            tags_ch += str(s_tags_3[tags[2]])
        return tags_ch
    elif pos == 'C':
        tags_ch = 'Conjunction'
        c_tags_1 = {'c':'coordinating', 's':'subordinating'}
        c_tags_2 = {'s':'simple', 'c':'compound'}
        c_tags_3 = {'p':'sentence', 'w':'words'}
        c_tags_4 = {'z': 'negative', 'p':'positive'}
        if len(tags) > 0:
            tags_ch += ':'
            if tags[0] in c_tags_1:
                tags_ch += 'Type='
                tags_ch += str(c_tags_1[tags[0]])
            if tags[1] in c_tags_2:
                tags_ch += ','
                tags_ch += 'Formation='
                tags_ch += str(c_tags_2[tags[1]])
            if tags[2] in c_tags_3:
                tags_ch += ','
                tags_ch += 'Coord_Type='
                tags_ch += str(c_tags_3[tags[2]])
            if tags[3] in c_tags_4:
                tags_ch += ','
                tags_ch += 'Sub_Type='
                tags_ch += str(c_tags_4[tags[3]])
        return tags_ch
    elif pos == 'M':
        tags_ch = 'Numeral'
        m_tags_1 = {'c':'cardinal', 'o':'ordinal', 'm':'multiple', 'l':'collect'}
        m_tags_2 = {'m':'masculine', 'f': 'feminine', 'n': 'neuter', '-':'none'}
        m_tags_3 = {'s':'singular', 'p':'plural', '-':'none'}
        m_tags_4 = {'n': 'Nom', 'g': 'Gen', 'd': 'Dat', 'a': 'Acc', 'l': 'Loc', 'i': 'Instr', '-':'none'}
        m_tags_5 = {'d':'digit', 'r':'roman', 'l':'letter'}
        m_tags_6 = {'n':'non-animate', 'y':'animate'}
        if tags[0] in m_tags_1:
            tags_ch += 'Type='
            tags_ch += str(m_tags_1[tags[0]])
        if tags[1] in m_tags_2:
            tags_ch += ','
            tags_ch += 'Gender='
            tags_ch += str(m_tags_2[tags[1]])
        if tags[2] in m_tags_3:
            tags_ch += ','
            tags_ch += 'Number='
            tags_ch += str(m_tags_3[tags[2]])
        if tags[3] in m_tags_4:
            tags_ch += ','
            tags_ch += 'Case='
            tags_ch += str(m_tags_4[tags[3]])
        if len(tags) > 4:
            if tags[4] in m_tags_5:
                tags_ch += ','
                tags_ch += 'Form='
                tags_ch += str(m_tags_5[tags[4]])
            if len(tags) > 5:
                if tags[5] in m_tags_6:
                    tags_ch += ','
                    tags_ch += 'Case='
                    tags_ch += str(m_tags_6[tags[5]])
        return tags_ch
    elif pos == 'Q':
        tags_ch = 'Particle'
        q_tags_1 = {'s':'simple', 'c':'compound'}
        if len(tags) > 0:
            if tags[0] in q_tags_1:
                tags_ch += ':Formation='
                tags_ch += str(q_tags_1[tags[0]])
        return tags_ch
    elif pos == 'I':
        tags_ch = 'Interjection'
        i_tags_1 = {'s':'simple', 'c':'compound'}
        if len(tags) > 0:
            if tags[0] in i_tags_1:
                tags_ch += ':Formation='
                tags_ch += str(i_tags_1[tags[0]])
        return tags_ch
    elif pos == 'Y':
        tags_ch = 'Abbreviation'
        y_tags_1 = {'n':'nominal', 'r':'adverbial'}
        y_tags_2 = {'m':'masculine', 'f': 'feminine', 'n': 'neuter', '-':'none'}
        y_tags_3 = {'s':'singular', 'p':'plural', '-':'none'}
        y_tags_4 = {'n': 'Nom', 'g': 'Gen', 'd': 'Dat', 'a': 'Acc', 'l': 'Loc', 'i': 'Instr', '-':'none'}          
        if len(tags) > 0:
            tags_ch += ':'
            if tags[0] in y_tags_1:
                tags_ch += 'Syntactic_Type='
                tags_ch += str(y_tags_1[tags[0]])
            if tags[1] in y_tags_2:
                tags_ch += ','
                tags_ch += 'Gender='
                tags_ch += str(y_tags_2[tags[1]])
            if tags[2] in y_tags_3:
                tags_ch += ','
                tags_ch += 'Number='
                tags_ch += str(y_tags_3[tags[2]])
            if tags[3] in y_tags_4:
                tags_ch += ','
                tags_ch += 'Case='
                tags_ch += str(y_tags_4[tags[3]])
        return tags_ch
    elif pos == 'X':
        tags_ch = 'Residual'
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
    tags = change_tags(tag[3], tag[2])
    outfile.write(str(tag[0]) + '\t' + str(tag[1]) + '\t' + str(tags) + '\n')
outfile.close()

