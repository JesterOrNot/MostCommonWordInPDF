from tika import parser


# Reads the text of a pdf into a string then returns said string
def read_pdf_to_string(file_name):
    return parser.from_file(file_name)['content']

# Splits words into a list


def string_to_list(string: str):
    return string.split(" ")

# Fiters punctuation out of word list


def filter_list(the_list: list):
    final_list = []
    punctuation = [",", ";", "(", ")", "[", "]",
                   "{", "}", '"', "'", ".", "”", "\n", "“", "\t", "-"]
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
            my_dict[i] = 1
        else:
            my_dict[i] = my_dict.get(i)+1
    return my_dict

# Iterates through a dict and finds the largest value and returns it's key


def find_most_frequent_word(word_dict: dict):
    largest = list(word_dict)[0]
    for key, value in word_dict.items():
        if key == "the" or "and":
            continue
        if value > word_dict.get(largest):
            largest = key
    return largest


if __name__ == "__main__":
    print("Reading pdf...")
    # print(create_dict_from_list(filter_list(string_to_list(
    #     read_pdf_to_string("Salvage the Bones ( PDFDrive.com ).pdf"))))['Skeetah'])
    word_dict = create_dict_from_list(filter_list(
        string_to_list(read_pdf_to_string("Salvage the Bones ( PDFDrive.com ).pdf"))))
    most_common_word = find_most_frequent_word(create_dict_from_list(filter_list(
        string_to_list(read_pdf_to_string("Salvage the Bones ( PDFDrive.com ).pdf")))))
    print(f"The most common word is {most_common_word}")
    print(f"There are {len(word_dict)} unique words in salvage the bones")