# Clue Generator

This is the current project that I am actively involved in.

The aim of this project is to provide automated clues to target words. This is a word guessing game between a human and machine. I am using NLP tools to extract various features for the automated clues / the human clue and understand what makes a clue good.


Some of the features of the clue that are being used to better understand clues are:

1) Ratio of **Content words vs Function Words**

2) **Lexicon Count** :Not normalized.

3) **Syllable Count** : Not normalized.

4) **Avg Word Length**: Normalized.

5) **Stop word Count**: Not normalized.

6) **Bi Gram Fréquence**: This is bi gram frequency of the adjacent words in a sentence , source brown corpus. This is not normalized.

7) **Syntax tree height:

8) **Non terminal count of syntax tree**

9) **Avg branching factor**

10) **Adjective and Participle count**: Not normalized.

11) **Dependency complexity**: Average dependency distances (ADDs) of a sentence. Reference: https://www.researchgate.net/publication/266584664_Syntactic_Dependency_Distance_as_Sentence_Complexity_Measure

12) **Flesh reading ease**: Output a number from 0 to 100 - a higher score indicates easier reading. An average document has a Flesch Reading Ease score between 6 - 70. As a rule of thumb, scores of 90-100 can be understood by an average 5th grader. 8th and 9th grade students can understand documents with a score of 60-70; and college graduates can understand documents with a score of 0-30.

13) **Flesch Kincaid grade**: Outputs a U.S. school grade level; this indicates the average student in that grade level can read the text. For example, a score of 7.4 indicates that the text is understood by an average student in 7th grade.

14) **Coleman luau grade**: Relies on characters instead of syllables per word and sentence length. This formula will output a grade. For example, 10.6 means your text is appropriate for a 10-11th grade high school student.

15) **Automated Readability Score**: outputs a number which approximates the grade level needed to comprehend the text. For example, if the ARI outputs the number 3, it means students in 3rd grade (ages 8-9 yrs. old) should be able to comprehend the text.

16) **Dale Chall Readability Score**: It uses a list of 3000 words that groups of fourth-grade American students could reliably understand, considering any word not on that list to be difficult.

17) **Gunning Fog**: Is similar to the Flesch scale in that it compares syllables and sentence lengths. A Fog score of 5 is readable, 10 is hard, 15 is difficult, and 20 is very difficult. Based on its name, 'Foggy' words are words that contain 3 or more syllables.

More info about all the readability tests https://wordcounttools.com/dale_chall_readability_level.html

18) **Named Entity Recognition Count**: Using NLTK go get the Named Entities in a clue.


The machine clues were also classified based on the type of the clue ( definition, example, sys, wiki, idiomPhrase, wnNounHyper ect. )

Here are some of the observations:

Some of the screenshots of the App.
![architecture](https://github.com/VaibhavDesai/ClueGenerator/blob/master/CG/Output/humans/automated_readability_index.png?raw=true "Img1")

![webApp](https://github.com/VaibhavDesai/ClueGenerator/blob/master/CG/Output/humans/avg_word_length.png?raw=true "Img1")

![src1](https://github.com/VaibhavDesai/ClueGenerator/blob/master/CG/Output/humans/bi_gram_frequency.png?raw=true "Img1")

![architecture](https://github.com/VaibhavDesai/ClueGenerator/blob/master/CG/Output/humans/coleman_liau_index.png?raw=true "Img1")

![webApp](https://github.com/VaibhavDesai/ClueGenerator/blob/master/CG/Output/humans/syntax_tree.png?raw=true "Img1")

![src1](https://github.com/VaibhavDesai/ClueGenerator/blob/master/CG/Output/humans/stopword_count.png?raw=true "Img1")
