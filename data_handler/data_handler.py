def prepare_all_words_list(filename):
    with open(filename, "r") as input_f:
        all_words = input_f.readlines()

    all_words = [word.strip() for word in all_words]
    return all_words