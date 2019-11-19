def read_pdf_to_string(file_name):
    pass


def string_to_list(string: str):
    word_list = string.split(" ")
    return word_list

def filter_list(the_list: list):
    final_list = []
    punctuation = [",", ";", "(", ")", "[", "]", "{", "}", '"', "'", ".", "”"]
    for i in the_list:
        filtered_word = ""
        split_str = i.split()
        for l in split_str:
            if l in punctuation:
                pass
            else:
                filtered_word += l
        final_list += filtered_word


def create_dict_from_list(the_list: list):
    pass


def find_most_frequent_word(word_dict: dict):
    pass


if __name__ == "__main__":
    pass