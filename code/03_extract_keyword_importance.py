import pandas as pd
from openai2 import *
import nltk
from nltk.tokenize import word_tokenize
import pickle

decoding_args = OpenAIDecodingArguments(
    max_tokens=4000
)

def tokenize_and_divide(text):
    # Tokenize the input text
    tokens = word_tokenize(text)

    # Check if the number of tokens is less than or equal to 4000
    if len(tokens) <= 3000:
        return [' '.join(tokens)]

    # Calculate the midpoint
    mid = len(tokens) // 2

    # Divide the tokens into two parts
    part1 = tokens[:mid]
    part2 = tokens[mid:]

    # Recursively apply divide_and_conquer on each part
    result = tokenize_and_divide(' '.join(part1)) + tokenize_and_divide(' '.join(part2))
    return result

TOPIC = "islamophobia"
filespath = '{}/filter_page_gpt4/'.format(TOPIC)
files=os.listdir(filespath)
# print(files)

article_text_list = []
for file in files:
    with open(os.path.join(filespath,file), 'r', encoding="utf-8") as file:
        text_content = file.read()
        article_text_list.append(text_content)

text_chunks_list = []
for article_text in article_text_list:
    text_chunks = tokenize_and_divide(article_text)
    text_chunks_list.append(text_chunks)

prompt_file_path = 'prompt_extract_keyword_importance.txt'

# Read the content of the text file into a string
with open(prompt_file_path, 'r', encoding="utf-8") as file:
    prompt = file.read()

sum_cost = 0
results_list = []
for text_chunks in text_chunks_list:
    num_chunks = len(text_chunks)
    prompt_lst = []
    for text_chunk in text_chunks:
        prompt_lst.append(prompt.format(TOPIC, text_chunk))
    # gpt-4-1106-preview gpt-3.5-turbo-1106
    results, finish_reason_lst, token_count, cost = openai_complete(prompt_lst, decoding_args, "gpt-4-1106-preview")
    sum_cost += cost
    results_list.append(results)
print("cost: {}".format(sum_cost))

article_results_dict = {}
for i in range(len(files)):
    article_results_dict[files[i]] = results_list[i]

# Save the dictionary to the pickle file
with open("{}/article_results_dict.pkl".format(TOPIC), 'wb') as pickle_file:
    pickle.dump(article_results_dict, pickle_file)


