"""
 - Reads data from the news_archive downloaded from Kaggle
 - Uses the keyword entered by user, the language selected and the source to query the datasource
 - Returns all news articles which match the options selected by the user.
 - Uses deep_translator library to translate user input in english to the language selected

"""

from deep_translator import GoogleTranslator


def search_archives_from_keyword(a):

    """
    Below in comments is the dictionary of languages supported by deep_translator
    We drop all the data where the languages in the CSV file do not match the languages in the below dictionary
    """
    # avail_lang = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy',
    # 'assamese': 'as', 'aymara': 'ay', 'azerbaijani': 'az', 'bambara': 'bm', 'basque': 'eu', 'belarusian': 'be',
    # 'bengali': 'bn', 'bhojpuri': 'bho', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb',
    # 'chichewa': 'ny', 'chinese (simplified)': 'zh-CN', 'chinese (traditional)': 'zh-TW', 'corsican': 'co',
    # 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dhivehi': 'dv', 'dogri': 'doi', 'dutch': 'nl', 'english':
    # 'en', 'esperanto': 'eo', 'estonian': 'et', 'ewe': 'ee', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr',
    # 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'guarani': 'gn',
    # 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'iw', 'hindi': 'hi',
    # 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'ilocano': 'ilo', 'indonesian': 'id',
    # 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk',
    # 'khmer': 'km', 'kinyarwanda': 'rw', 'konkani': 'gom', 'korean': 'ko', 'krio': 'kri', 'kurdish (kurmanji)':
    # 'ku', 'kurdish (sorani)': 'ckb', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lingala': 'ln',
    # 'lithuanian': 'lt', 'luganda': 'lg', 'luxembourgish': 'lb', 'macedonian': 'mk', 'maithili': 'mai', 'malagasy':
    # 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'meiteilon (
    # manipuri)': 'mni-Mtei', 'mizo': 'lus', 'mongolian': 'mn', 'myanmar': 'my', 'nepali': 'ne', 'norwegian': 'no',
    # 'odia (oriya)': 'or', 'oromo': 'om', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt',
    # 'punjabi': 'pa', 'quechua': 'qu', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'sanskrit': 'sa',
    # 'scots gaelic': 'gd', 'sepedi': 'nso', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd',
    # 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su',
    # 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'tatar': 'tt', 'telugu': 'te', 'thai': 'th',
    # 'tigrinya': 'ti', 'tsonga': 'ts', 'turkish': 'tr', 'turkmen': 'tk', 'twi': 'ak', 'ukrainian': 'uk',
    # 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi',
    # 'yoruba': 'yo', 'zulu': 'zu'}

    # avail_lang = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy',
    #              'assamese': 'as', 'aymara': 'ay', 'azerbaijani': 'az', 'bambara': 'bm', 'basque': 'eu',
    #              'belarusian': 'be', 'bengali': 'bn', 'bhojpuri': 'bho', 'bosnian': 'bs', 'bulgarian': 'bg',
    #              'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-CN',
    #              'chinese (traditional)': 'zh-TW', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da',
    #              'dhivehi': 'dv', 'dogri': 'doi', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et',
    #              'ewe': 'ee', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl',
    #              'georgian': 'ka', 'german': 'de', 'greek': 'el', 'guarani': 'gn', 'gujarati': 'gu',
    #             'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'iw', 'hindi': 'hi',
    #              'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'ilocano': 'ilo',
    #              'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw',
    #              'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'kinyarwanda': 'rw', 'konkani': 'gom', 'korean': 'ko',
    #              'krio': 'kri', 'kurdish (kurmanji)': 'ku', 'kurdish (sorani)': 'ckb', 'kyrgyz': 'ky', 'lao': 'lo',
    #              'latin': 'la', 'latvian': 'lv', 'lingala': 'ln', 'lithuanian': 'lt', 'luganda': 'lg',
    #              'luxembourgish': 'lb', 'macedonian': 'mk', 'maithili': 'mai', 'malagasy': 'mg', 'malay': 'ms',
    #              'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr',
    #              'meiteilon (manipuri)': 'mni-Mtei', 'mizo': 'lus', 'mongolian': 'mn', 'myanmar': 'my', 'nepali': 'ne',
    #              'norwegian': 'no', 'odia (oriya)': 'or', 'oromo': 'om', 'pashto': 'ps', 'persian': 'fa',
    #              'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'quechua': 'qu', 'romanian': 'ro',
    #              'russian': 'ru', 'samoan': 'sm', 'sanskrit': 'sa', 'scots gaelic': 'gd', 'sepedi': 'nso',
    #              'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk',
    #              'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw',
    #              'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'tatar': 'tt', 'telugu': 'te', 'thai': 'th',
    #              'tigrinya': 'ti', 'tsonga': 'ts', 'turkish': 'tr', 'turkmen': 'tk', 'twi': 'ak', 'ukrainian': 'uk',
    #              'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh',
    #              'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}
    #a = a[a['Language'].str.lower().isin(avail_lang.keys()) == True]

    """
    Create a dictionary of all languages where the keys are indexed starting from 1
    Ask user to choose the language of their choice
    Using user input to create a new dataframe which is specific to the language selected
    
    """

    a.dropna()
    languages = a['Language'].unique()
    lang_dict = {}
    i = 1

    for lang in languages:
        lang_dict[i] = lang
        i = i + 1

    print("\nChoose the language of archive")
    for i in lang_dict.keys():
        print(f"{i}. {lang_dict[i]}")

    choice = int(input("\nEnter a number: "))
    lang = lang_dict[choice]

    source = a.groupby('Language')['Source'].apply(list).reset_index(name='Source_List')

    """
    Create a list of web sources for the specific language
    Ask user to choose the source of their choice
    Using user input to create a new dataframe which is specific to the source selected

    """

    i = source[source['Language'] == lang].index.values[0]
    lang_source = list(set(source._get_value(i, 'Source_List')))
    i = 1

    print("\nChoose a source: ")
    for s in lang_source:
        print(f"{i}. {s}")
        i = i + 1

    src_choice = int(input("\nEnter a choice for source: "))
    src = lang_source[src_choice - 1]

    """
       Use language and source to query original dataframe and create a new dataframe
       Prompt the user for a keyword of choice
       Create a list of all articles which match the keyword
       Display the list

       """

    a_new = a.loc[a['Language'] == lang]
    a_new = a_new.loc[a_new['Source'] == src]

    keyword = str(input("\nEnter a keyword: "))
    translated = GoogleTranslator(source='auto', target=lang.lower()).translate(keyword)
    final = a_new[a_new['Text'].str.lower().str.contains(translated.lower())]
    final = final.drop(['Language', 'Source', 'Date'], axis=1)
    col_list = final.Text.values.tolist()

    i = 1
    print()

    for lang in col_list:
        print(f"{i}. {lang}")
        i += 1

