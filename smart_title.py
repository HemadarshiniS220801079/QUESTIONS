def smart_title_case(sentence):
    abbreviations = {"AI", "ML", "NLP", "API", "SQL", "CPU", "GPU"}
    
    words = sentence.split()
    result = []
    
    for word in words:
        upper_word = word.upper()
        if upper_word in abbreviations:
            result.append(upper_word)
        else:
            result.append(word.capitalize())
    
    return " ".join(result)


if __name__ == "__main__":
    sentence = input().strip()
    print(smart_title_case(sentence))

