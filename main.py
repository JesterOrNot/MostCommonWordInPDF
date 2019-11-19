import textract


# Reads the text of a pdf into a string then returns said string
def read_pdf_to_string(file_name):
    return textract.process(file_name)

# Splits words into a list
def string_to_list(string: str):
    return string.split(" ")

# Fiters punctuation out of word list
def filter_list(the_list: list):
    final_list = []
    punctuation = [",", ";", "(", ")", "[", "]",
                   "{", "}", '"', "'", ".", "”", "\n", "“"]
    for i in the_list:
        if len(i) == 0:
            continue
        filtered_word = ""
        split_str = list(i)
        for l in split_str:
            if l in punctuation:
                continue
            else:
                filtered_word += l
        final_list.append(filtered_word)
    return final_list

# Counts num of times word occurs in list and adds them to a dict
def create_dict_from_list(the_list: list):
    my_dict = {}
    for i in the_list:
        if not i in my_dict.keys():
            my_dict[i] = 0
        else:
            my_dict[i] = my_dict.get(i)+1
    return my_dict

# Iterates through a dict and finds the largest value and returns it's key
def find_most_frequent_word(word_dict: dict):
    largest = word_dict[0]
    for key, value in word_dict.items():
        if value > word_dict.get(largest):
            largest = key
    return largest


if __name__ == "__main__":
    print(find_most_frequent_word(create_dict_from_list(filter_list(string_to_list(read_pdf_to_string("Salvage the Bones ( PDFDrive.com ).pdf"))))))
