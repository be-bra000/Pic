import re

def censor_checker():
    banned_list = ['hello', 'email', 'python', 'the', 'exam', 'wor', 'is']
    sentence = 'Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!'
    result = sentence
    for word_to_censor in banned_list:
        star_mask = '*' * len(word_to_censor)

        result = re.sub(
            re.escape(word_to_censor),
            star_mask,
            result,
            flags=re.IGNORECASE
        )

    print(result.replace('\n', ''))

if __name__ == "__main__":
    censor_checker()