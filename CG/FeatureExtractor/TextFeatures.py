from textstat.textstat import textstat
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import time



class TextFeatures:

    text = ""
    annotator = None
    bigrams_freq = []
    trigrams_freq = []
    word_tokens = []
    syntax_tree = ""
    annotation = None
    stop_words = set(stopwords.words('english'))

    def __init__(self, text,annotator, bigrams_freq):
        self.text = text
        self.bigrams_freq = bigrams_freq
        #times=[]
        #times.append(time.time())
        self.annotation = annotator.getAnnotations(self.text, dep_parse=True)
        #times.append(time.time())
        self.syntax_tree = self.annotation['syntax_tree']
        #times.append(time.time())
        self.word_tokens = word_tokenize(self.text)
        #times.append(time.time())
        for i in range(len(self.word_tokens)):
            if "." in self.word_tokens[i]:
                self.word_tokens[i] = self.word_tokens[i][:-1]

        #times.append(time.time())

        '''
        tracker=0
        for tim in times:
            if tracker>0:
                print "count_2 "+str(tracker)+":"+str(tim-last)
            tracker=tracker+1
            last=tim
        '''
        
    def lexicon_count(self):

        try:
            return textstat.lexicon_count(self.text)
        except:
            return 0

    def syllable_count(self):
        try:
            return textstat.syllable_count(self.text)
        except:
            return 0

    def word_count(self):
        return len(self.word_tokens)

    #normalized
    def avg_letters_per_word_count(self):
        try:
            number_of_letters = 0
            for words in self.word_tokens:
                number_of_letters += len(words)
            return number_of_letters / len(self.word_tokens)
        except:
            return 0

    def stopword_count(self):
        try:
            count = 0
            for w in self.word_tokens:
                if w in self.stop_words:
                    count +=1

            return count
        except:
            return 0

    #normalized
    def frame_count(self):
        try:
            return float(len(self.annotation['srl']))/len(self.word_tokens)
        except:
            return 0

    def nGram(self, n):

        try:
            n_gram_score = {}
            if n == 2:
                for i in range(len(self.word_tokens)-1):
                    n_gram_score[self.word_tokens[i]+" "+self.word_tokens[i+1]] = self.bigrams_freq[(self.word_tokens[i], self.word_tokens[i+1])]

            '''if n == 3:
                for i in range(len(self.word_tokens)-2):
                    n_gram_score += self.bigrams_freq[(self.word_tokens[i], self.word_tokens[i+1], self.word_tokens[i+2])]
            '''
            return n_gram_score
        except:
            return 0

    def syntax_tree_height(self):

        try:
            counter = 0
            level = 0
            for ch in self.syntax_tree:
                if ch == '(':
                    counter += 1
                elif ch == ')':
                    counter -= 1

                if counter > level:
                    level = counter

            return level
        except:
            return 0

    def syntax_tree_non_terminal_node_count(self):

        try:
            count = 0
            for ch in self.syntax_tree:
                if ch == '(':
                    count += 1

            return count
        except:
            return 0

    def filler_word_count(self):

        try:
            count = 0
            for word in self.word_tokens:
                if word in ['uh', 'ah', 'like', 'you know', 'I mean', 'okay', 'so', 'actually', 'basically', 'right']:
                    count += 1

            return count
        except:
            return 0

    #ADD formula
    def dependency_complexity(self):

        try:

            list_of_dep = self.annotation['dep_parse'].split("\n")
            sum = 0
            for dep in list_of_dep:
                dependent_words = dep[dep.find("(")+1:dep.find(")")].split(",")
                sum += abs(int(dependent_words[0].split("-")[-1]) - int(dependent_words[1].split("-")[-1]))
            return sum/len(list_of_dep)
        except:
            return 0

    # Total number of nodes expanded/ total number of nodes generated
    def avg_branching_factor_syntax_tree(self):
        try:

            pos = self.annotation['pos']
            non_terminal_nodes_count = self.syntax_tree_non_terminal_node_count()
            total_number_of_nodes_expanded = non_terminal_nodes_count+len(pos)
            res = total_number_of_nodes_expanded/non_terminal_nodes_count
            return res
        except:
            return 0

    def adjective_and_participle_count(self):
        try:
            count = 0
            for ele in self.annotation['pos']:
                if ele[1] == 'JJ' or ele[1] == 'VBN':
                    count += 1
            return count
        except:
            return 0

    def preposition_count(self):

        try:
            count = 0
            for ele in self.annotation['pos']:
                if ele[1] == 'IN' or ele[1] == 'ON' or ele[1] == 'AT':
                    count += 1
            return count
        except:
            return 0

    def NER(self, type):

        entity_dic = {}
        for sent in nltk.sent_tokenize(self.text.title()):
            for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
                if hasattr(chunk, 'label'):
                    if chunk.label() not in entity_dic:
                        entity_dic[chunk.label()] = []
                    entity_dic[chunk.label()].append(' '.join(c[0] for c in chunk))

        if type == 'ALL':
            count = 0
            for k,v in enumerate(entity_dic):
                count += len(entity_dic[v])
            return count
        if type == 'ORGANIZATION':
            if 'ORGANIZATION' in entity_dic:
                return len(entity_dic['ORGANIZATION'])
            else:
                return 0
        if type == 'PERSON':
            if 'PERSON' in entity_dic:
                return len(entity_dic['PERSON'])
            else:
                return 0
        if type == 'LOCATION':
            if 'LOCATION' in entity_dic:
                return len(entity_dic['LOCATION'])
            else:
                return 0
        if type == 'DATE':
            if 'DATE' in entity_dic:
                return len(entity_dic['DATE'])
            else:
                return 0
        if type == 'TIME':
            if 'TIME' in entity_dic:
                return len(entity_dic['TIME'])
            else:
                return 0
        if type == 'MONEY':
            if 'MONEY' in entity_dic:
                return len(entity_dic['MONEY'])
            else:
                return 0
        if type == 'FACILITY':
            if 'FACILITY' in entity_dic:
                return len(entity_dic['FACILITY'])
            else:
                return 0
        if type == 'GPE':
            if 'GPE' in entity_dic:
                return len(entity_dic['GPE'])
            else:
                return 0