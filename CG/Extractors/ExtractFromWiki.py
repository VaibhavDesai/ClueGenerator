from Utils import *

class ExtractFromWiki:

    def __init__(self):
        pass

    def extractFromWiki(self, word):

        source = "https://en.wikipedia.org/wiki/"
        searchString = source + word
        soup = getWebContent(searchString)

        body_content_bs = soup.find('div', id='bodyContent')
        if body_content_bs:
            mw_content_text_bs = body_content_bs.find('div', id='mw-content-text')

            if mw_content_text_bs:
                mw_parser_output_bs = mw_content_text_bs.find('div', class_='mw-parser-output')
                if mw_parser_output_bs:
                    first_para_bs = mw_parser_output_bs.p
                    return {'example_sentences':[first_para_bs.get_text().split('.')[0]]}

