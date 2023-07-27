# Easy data augmentation techniques for text classification
# Jason Wei and Kai Zou
import nltk
#nltk.download('omw-1.4')
try:
    nltk.data.find("corpora/wordnet")
except LookupError:
    nltk.download("wordnet")

from eda import *

#arguments to be parsed from command line
import argparse

# Create the argument parser
ap = argparse.ArgumentParser()
arguments = {
    "input": r"..\data\corpus\TREC.txt",
    "input_labels": r"..\data\TREC\TREC.txt",
    "output_clean": r"TREC.clean_eda8.txt",
    "output": r"C:TREC_eda8.txt",  # Specify the output file if needed
    "output_labels": r"TREC_labels_eda8.txt",
    "num_aug": 8,
    "alpha_sr": 0.1,
    "alpha_ri": 0.1,
    "alpha_rs": 0.1,
    "alpha_rd": 0.1
}

args = ap.parse_args([])
args.input = arguments["input"]
args.input_labels = arguments["input_labels"]
args.output_clean = arguments["output_clean"]
args.output_labels = arguments["output_labels"]
args.output = arguments["output"]
args.num_aug = arguments["num_aug"]
args.alpha_sr = arguments["alpha_sr"]
args.alpha_ri = arguments["alpha_ri"]
args.alpha_rs = arguments["alpha_rs"]
args.alpha_rd = arguments["alpha_rd"]

#the output file
output = None
if args.output:
    output = args.output
else:
    from os.path import dirname, basename, join
    output = join(dirname(args.input), 'eda_' + basename(args.input))

#number of augmented sentences to generate per original sentence
num_aug = 9 #default
if args.num_aug:
    num_aug = args.num_aug

#how much to replace each word by synonyms
alpha_sr = 0.1#default
if args.alpha_sr is not None:
    alpha_sr = args.alpha_sr

#how much to insert new words that are synonyms
alpha_ri = 0.1#default
if args.alpha_ri is not None:
    alpha_ri = args.alpha_ri

#how much to swap words
alpha_rs = 0.1#default
if args.alpha_rs is not None:
    alpha_rs = args.alpha_rs

#how much to delete words
alpha_rd = 0.1#default
if args.alpha_rd is not None:
    alpha_rd = args.alpha_rd

if alpha_sr == alpha_ri == alpha_rs == alpha_rd == 0:
     ap.error('At least one alpha should be greater than zero')


#generate more data with standard augmentation
def gen_eda(input, labels_file, output_file, output_clean, output_labels, alpha_sr, alpha_ri, alpha_rs, alpha_rd, num_aug=9):
    writer = open(output_file, 'a')
    writer_clean = open(output_clean, 'a')
    writer_labels = open(output_labels, 'a')

    labels = []
    train_size = 0
    with open(labels_file, 'r') as input_labels:
        for line in input_labels:
            train_size += 1
            columns = line.split('\t')  # Split the line by tabs assuming it's a TSV file
            labels.append(columns[2])  # Add the value to the list
    train_size -= 500

    count = -1
    num = 0
    input_data = open(input, 'r').readlines()

    for i, line in enumerate(input_data):
        num += 1
        words = line.split()  # Split the string into a list of words
        line = ' '.join(words[1:])  # Join the words starting from the second word
        if (num <= train_size):
            aug_sentences = eda(line, alpha_sr=alpha_sr, alpha_ri=alpha_ri, alpha_rs=alpha_rs, p_rd=alpha_rd,
                                num_aug=num_aug)
            for aug_sentence in aug_sentences:
                aug_sentence += "?" if aug_sentence[-1] == " " else " ?"
                count += 1
                writer_labels.write(str(count) + "\t" + "train" + "\t" + labels[i])
                writer.write(aug_sentence + '\n')
                aug_sentence = aug_sentence.replace('?', "\?")
                writer_clean.write(aug_sentence + '\n')
        else:
            count += 1
            writer_labels.write(str(count) + "\t" + "test" + "\t" + labels[i])
            writer.write(line+"\n")
            line = line.replace('?', "\?")
            writer_clean.write(line+"\n")



#main function
if __name__ == "__main__":

    #generate augmented sentences and output into a new file
    #gen_eda(args.input, output, args.output_clean, args.output_labels, args.test, alpha_sr=alpha_sr, alpha_ri=alpha_ri, alpha_rs=alpha_rs, alpha_rd=alpha_rd, num_aug=num_aug)
    gen_eda(args.input, args.input_labels, output, args.output_clean, args.output_labels, alpha_sr=alpha_sr, alpha_ri=alpha_ri, alpha_rs=alpha_rs, alpha_rd=alpha_rd, num_aug=num_aug)
