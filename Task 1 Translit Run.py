def get_lines_text(link_to_txt_doc):

    freading = open(link_to_txt_doc, 'rt', encoding='utf8')
    lines = freading.readlines()
    freading.close()

    return lines


# -------------------------------------------------
# Транслітеруємо укр. слово в англ. слово
def translit_line_text_ua_to_en(ua_text):
    dict_translit_ua_to_en = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'h', 'ґ': 'g', 'д': 'd', 'е': 'e', 'є': 'ie', 'ж': 'zh', 'з': 'z', 'и': 'y', 'і': 'i', 'ї': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ю': 'iu', 'я': 'ia', 'зг': 'zgh',
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'H', 'Ґ': 'G', 'Д': 'D', 'Е': 'E', 'Є': 'Ye', 'Ж': 'Zh', 'З': 'Z', 'И': 'Y', 'І': 'I', 'Ї': 'Yi', 'Й': 'Y', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Ts', 'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'Ю': 'Yu', 'Я': 'Ya', 'Зг': 'Zgh'
        # М'який знак і апостроф латиницею не відтворюються
        # Транслітерація  прізвищ  та  імен осіб і географічних назв здійснюється шляхом  відтворення  кожної  літери латиницею
    }

    list_translit_ua_to_en = list(dict_translit_ua_to_en.keys())
    en_word = ''
    list_words = []
    len_ua_text = len(ua_text) - 1 # for test:  len_ua_text == 100  >>> new len_ua_text == 99
    i = 0

    while i <= len_ua_text:  # for test:  i <= 99   >>>  i in [0, 99]
        if ua_text[i] == 'з' and ua_text[i + 1] == 'г' and i < len_ua_text:
            en_word += 'zgh'
            i += 1
        elif ua_text[i] == 'З' and ua_text[i + 1] == 'г' and i < len_ua_text:
            en_word += 'Zgh'
            i += 1
        elif ua_text[i] in list_translit_ua_to_en:
            en_word += dict_translit_ua_to_en[ua_text[i]]
        elif ua_text[i] == 'ь' or ua_text[i] == "'":
            pass
        elif len(en_word) > 0:
            list_words.append(en_word)
            en_word = ''
    
        i += 1

    return list_words


def get_sum_letters_in_word(en_word):
    
    dict_nums_en_letters = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,
        'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36, 'K': 37, 'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44, 'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52
    }

    sum = 0
    
    for char in en_word:
        sum += int(dict_nums_en_letters[char])

    return sum


# -------------------------------------------    
# Конвертуємо список українських слів, у список англійських слів

def get_list_words_ua_to_en(lines_out_text_file):

    # ua_text = lines_out_text_file
    list_words_en = []
    max_col = 0

    for phrase in lines_out_text_file:
        phrase += '.'
        en_phrase = translit_line_text_ua_to_en(phrase)
        list_words_en.append(en_phrase)
        
        if max_col < len(en_phrase):
            max_col = len(en_phrase)

    return list_words_en, max_col


# ----------------------------------------------------------
# Створюємо задану матрицю

def get_matrix(list_words_en, max_col):

    matrix = []

    for i, phrase in enumerate(list_words_en):
        matrix.append([])
        len_phrase = len(phrase)

        for j in range(max_col):
            if j < len_phrase:
                matrix[i].append(get_sum_letters_in_word(phrase[j]))
            else:
                matrix[i].append(0)

    return matrix
                

def vectorizer(link_to_txt_doc):
# ---------------------------------------------
    # Дістаємо текст з файлу
    lines_out_text_file = get_lines_text(link_to_txt_doc)[10:]

    # Конвертуємо список українських слів, у список англійських слів
    list_words_en, max_col = get_list_words_ua_to_en(lines_out_text_file)

    # Створюємо задану матрицю
    matrix = get_matrix(list_words_en, max_col)

    return matrix
 


def main():

    link_to_txt_doc = 'doc_txt_file.txt'
    matrix = vectorizer(link_to_txt_doc)

    print('matrix:')
    print(matrix)




if __name__ == '__main__':
    main()