
import re
from Utils import *

class ExtractFromDictionaryDotCom:

    def __init__(self):
        pass

    def extractDefinitions(self, word):
        source = "http://www.dictionary.com/browse/"
        searchString = source + word + "?s=t"
        soup = getWebContent(searchString)

        types = {}

        content_container = soup.find('div', class_="center-well-container")

        if content_container:
            def_list = content_container.find('div', class_='def-list')
            if def_list:
                def_sections = def_list.find_all('section', class_="def-pbk ce-spot")

                if def_sections:

                    for section in def_sections:

                        def_set = section.find_all('div', class_='def-set')
                        section_header_bs = section.find('header', class_='luna-data-header')

                        if section_header_bs:

                            section_header_text = section_header_bs.find('span', class_='dbox-pg')
                            if section_header_text:

                                types[section_header_text.text] = []
                                if def_set:
                                    for defs in def_set:
                                        if defs:
                                            for definition in defs.find_all('div', class_='def-content'):
                                                if definition:
                                                    bold_text_bs = definition.find('span', class_='dbox-bold')
                                                    if bold_text_bs:
                                                        types[section_header_text.text].append(bold_text_bs.get_text())
                                                        break

                                                    types[section_header_text.text].append(re.sub(r"\s+", " ", definition.get_text(), flags=re.UNICODE))

            types['example_sentences'] = []
            source_example = content_container.find('section', id="source-example-sentences")

            if source_example:
                sent_wrap = source_example.find('div', class_="sent-wrap ce-spot")

                if sent_wrap:
                    source_box = sent_wrap.find('div', class_="source-box")
                    if source_box:
                        for example in source_box.find_all('p', class_="partner-example-text"):
                            types['example_sentences'].append(re.sub(r"\s+", " ", example.get_text(), flags=re.UNICODE))


        return types

    def extractSynonymsAndAntonyms(self, word):
        source = "http://www.thesaurus.com/browse/"
        searchString = source + word
        soup = getWebContent(searchString)
        types = {}
        types['synonyms'] = []
        types['antonyms'] = []
        relevency = soup.find('div', id='synonyms-0')

        if relevency:


            #######Synonyms
            relevency_list = relevency.find('div', class_='relevancy-list')

            if relevency_list:
                for span in relevency_list.find_all('span', class_='text'):
                    types['synonyms'].append(span.text)

            #######Antonyms

            relevency_list = relevency.find('section', class_='container-info antonyms')

            if relevency_list:

                list_holder = relevency_list.find('div', class_="list-holder")

                if list_holder:
                    for span in list_holder.find_all('span', class_="text"):
                        types['antonyms'].append(span.text)

        return types

    def extractFromDictionaryDotCom(self, word):
        print "here"
        return mergeTwoDicts(self.extractDefinitions(word), self.extractSynonymsAndAntonyms(word))
