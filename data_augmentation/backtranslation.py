
import csv
import re
from mtranslate import translate


# stop words list
stop_words = ['i', 'me', 'my', 'myself', 'we', 'our',
              'ours', 'ourselves', 'you', 'your', 'yours',
              'yourself', 'yourselves', 'he', 'him', 'his',
              'himself', 'she', 'her', 'hers', 'herself',
              'it', 'its', 'itself', 'they', 'them', 'their',
              'theirs', 'themselves', 'what', 'which', 'who',
              'whom', 'this', 'that', 'these', 'those', 'am',
              'is', 'are', 'was', 'were', 'be', 'been', 'being',
              'have', 'has', 'had', 'having', 'do', 'does', 'did',
              'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or',
              'because', 'as', 'until', 'while', 'of', 'at',
              'by', 'for', 'with', 'about', 'against', 'between',
              'into', 'through', 'during', 'before', 'after',
              'above', 'below', 'to', 'from', 'up', 'down', 'in',
              'out', 'on', 'off', 'over', 'under', 'again',
              'further', 'then', 'once', 'here', 'there', 'when',
              'where', 'why', 'how', 'all', 'any', 'both', 'each',
              'few', 'more', 'most', 'other', 'some', 'such', 'no',
              'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too',
              'very', 's', 't', 'can', 'will', 'just', 'don',
              'should', 'now', '']

def remove_stop_words(string):
    words = string.split()      # Split the string into words
    filtered_words = [word for word in words if word.lower() not in stop_words]     # Remove stop words from the list of words
    filtered_string = ' '.join(filtered_words)    # Rebuild the string without stop wrds
    return filtered_string


def back_translate(text, target_lang, source_lang='auto'):
    # Translate the text to the target language
    translation = translate(text, target_lang, source_lang)
    # Translate the translated text back to the source language
    back_translation = translate(translation, source_lang, target_lang)

    return back_translation


def create_data(input_file, labels_file, output, output_clean, output_labels, target_lang):
    writer = open(output, 'a', encoding="utf-8")
    writer_clean = open(output_clean, 'a', encoding="utf-8")
    writer_labels = open(output_labels, 'a', encoding="utf-8")

    labels = []
    train_size = 0
    with open(labels_file, 'r', encoding="utf-8") as input_labels:
        for line in input_labels:
            train_size += 1
            columns = line.split('\t')  # Split the line by tabs assuming it's a TSV file
            labels.append(columns[2])  # Add the value to the list
    train_size -= 500
    print(train_size)
    print((labels))

    num = 0
    with open(input_file, 'r', encoding="utf-8") as file:
        count = 0
        for line in file:
            print(num)
            if (num <= train_size):
                print("translate")
                words = line.split()  # Split the string into a list of words
                line = ' '.join(words[1:])  # Join the words starting from the second word
                line = line.replace('\n', "")
                writer_labels.write(str(count) + "\t" + "train" + "\t" + labels[num])
                writer.write(line + "\n")
                print(line)
                writer_clean.write(line.replace("?", "\?") + "\n")
                count += 1

                back_translated_text = back_translate(line, target_lang)

                new_str = re.sub('[a-zA-Z\s]+$', '', back_translated_text)

                if "?" in new_str:
                    new_str = new_str.replace("?", " ?")

                line_remove = remove_stop_words(line)
                new_str_remove = remove_stop_words(new_str)
                if new_str_remove.lower() != line_remove.lower() and new_str != '\t' and new_str != '\n' and \
                        new_str != " " and new_str != "":
                    writer_labels.write(str(count) + "\t" + "train" + "\t" + labels[num])
                    writer.write(new_str+ "\n")
                    print(new_str)
                    writer_clean.write(new_str.replace("?", "\?")+ "\n")
                    count += 1
                    #print(new_str +'\t'+labels[count]+'\n')
            else:
                writer_labels.write(str(count) + "\t"+ "test" + "\t" + labels[num])
                writer.write(line)
                print(line)
                count += 1
                writer_clean.write(line.replace("?", "\?"))

            num += 1



if __name__ == "__main__":

    # file_path = r'C:\Users\DELL\Desktop\לימודים מחשב\שנה ד\DL\files\TREC-not_augmented.txt'
    # output = r'C:\Users\DELL\Desktop\לימודים מחשב\שנה ד\DL\files\TREC_backtranslation.txt'
    # output_clean = r'C:\Users\DELL\Desktop\לימודים מחשב\שנה ד\DL\files\TREC.clean_backtranslation.txt'
    # output_labels = r'C:\Users\DELL\Desktop\לימודים מחשב\שנה ד\DL\files\TREC_backtranslation.txt'

    #lables_file= r'C:\Users\DELL\Desktop\לימודים מחשב\שנה ד\DL\files\labels.txt'

    # arguments to be parsed from command line
    import argparse

    # Create the argument parser
    ap = argparse.ArgumentParser()
    arguments = {
        "input": r"..\data\corpus\TREC.txt",
        "input_labels": r"..\data\TREC\TREC.txt",
        "output_clean": r"TREC.clean_backtranslation.txt",
        "output": r"TREC_backtranslation.txt",
        "output_labels": r"TREC_labels_backtranslation.txt",
        "target_lang": "iw"
    }

    args = ap.parse_args([])
    args.input = arguments["input"]
    args.input_labels = arguments["input_labels"]
    args.output_clean = arguments["output_clean"]
    args.output_labels = arguments["output_labels"]
    args.output = arguments["output"]
    args.target_lang = arguments["target_lang"]

    # the output file
    output = None
    if args.output:
        output = args.output
    else:
        from os.path import dirname, basename, join

        output = join(dirname(args.input), 'eda_' + basename(args.input))

    #create_data(file_path, lables_file, target_lang, output)
    create_data(args.input, args.input_labels, args.output, args.output_clean, args.output_labels, args.target_lang)

# from googletrans import LANGUAGES
#
# # Get a dictionary of language codes and names
# languages = LANGUAGES
#
# # Print the language codes and names
# for code, name in languages.items():
#     print(code, "-", name)