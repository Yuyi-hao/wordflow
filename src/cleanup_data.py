import re

data_file_name = 'data/corpus'
output_data_file_name = 'data/word_list.txt'

def openFileContent(inputFilePath, outputFilePath):
    word_set = ()
    with open(inputFilePath, 'r') as input_file:
        with open(outputFilePath, 'a') as output_file:
            for line in input_file:
                words = process_line(line)
                for word in words:
                    output_file.write(word+'\n')


def process_line(line):
    line_without_newline = line.replace('\n', ' ')
    # Replace punctuation characters and digits with spaces
    # [^\w\s]: Match any character that is not a word character (\w) or a whitespace character (\s)
    # |: OR
    # [\d]: Match any digit
    line_without_punctuation = re.sub(r'[^\w\s]|[\d]', ' ', line_without_newline)
    return [i.lower() for i in line_without_punctuation.split(' ') if i!=' ']

def main():
    openFileContent(data_file_name, output_data_file_name)

if __name__=="__main__":
    main()

