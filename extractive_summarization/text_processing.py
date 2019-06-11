import nltk
from nltk.tokenize import word_tokenize
import re
import sqlite3


class ProcessText:
    
    def __init__(self, text):
        self.text = text
        

    def split_sentences(self):
        sentences = self.text.split(". ")
        res = [x for x in sentences if x.strip()]
        return res
    
    def tokenize(self):
        sentences = []
        pattern = re.compile('[\W_]+')
        article = self.split_sentences()
        for sentence in article:
            sentences.append(word_tokenize(pattern.sub(' ', sentence.lower())))
        return sentences
    
    def lemmatize(self, words):
        connection = sqlite3.connect('ua_database/mph_ua _dialekt.db')
        cursor = connection.cursor()
        done_array = []
        for word in words:
            current_word = word
            previous = ''

            regular_expression = re.fullmatch(r'[A-z]*|%|#|\.|\d+|\w\.|\(|\)|:|!|-|,|«|»|—|\?|(\d+,\d+)|(\d+.\d+)|\w{1}', current_word)
            normal_form = cursor.execute('SELECT reestr FROM nom WHERE reestr=?', (str(current_word).upper().lower(),)).fetchall()

            
            if normal_form:
                if current_word != previous:
                    previous = current_word
                    done_array.append(current_word)
            
            elif current_word == "їй":
                done_array.append("вона")
            elif current_word == "його":
                done_array.append('він (воно)')
            elif current_word == 'мене':
                done_array.append('я')
            elif cursor.execute('SELECT Col002 FROM abbreviatury WHERE Col002=?',(str(current_word).upper(),)).fetchall():
                done_array.append(current_word.upper())
            elif regular_expression:
                done_array.append(current_word)

            
            elif not normal_form:
                STOP = False
                word_Length = len(current_word)
                for bukva in range(word_Length):
                    word_END = current_word[bukva:]
                    
                    cursor.execute("SELECT type FROM flexes WHERE flex=?", (word_END,))

                    for type in cursor.fetchall():                                       

                        
                        for normal_ending in cursor.execute("SELECT flex FROM flexes WHERE type=? AND field2=1",
                                                            (type)).fetchall():
                            
                            word_FINAL = (current_word[:bukva] + ''.join(str(cursor) for cursor in normal_ending))
                            if cursor.execute('SELECT reestr FROM nom WHERE (reestr=? AND type<>0)',
                                              (word_FINAL,)).fetchall():
                                if not done_array:
                                    done_array.append(word_FINAL)
                                else:
                                    if word_FINAL[:2] == done_array[-1][:2] and len(word_FINAL) <= len(done_array[-1]):
                                        done_array[-1] = word_FINAL
                                    elif word_FINAL[:2] != done_array[-1][:2]:
                                        done_array.append(word_FINAL)
                            elif cursor.execute('SELECT reestr FROM nom WHERE (reestr=? AND type!=0)',
                                                (str(word_FINAL).lower(),)).fetchall():
                                if not done_array:
                                    done_array.append(word_FINAL)
                                else:
                                    if word_FINAL[:2] == done_array[-1][:2] and len(word_FINAL) <= len(done_array[-1]):
                                        done_array[-1] = word_FINAL
                                    elif word_FINAL[:2] != done_array[-1][:2]:
                                        done_array.append(word_FINAL)
                        if STOP:
                            break

        show_final = ' '.join(done_array)
        return done_array
    
    def lemmatize_sentences(self):
        lem_text = []
        raw_text = self.tokenize()
        for sen in raw_text:
            lem_text.append(self.lemmatize(sen))
        return lem_text