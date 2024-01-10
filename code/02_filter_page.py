from openaifilter import *
import nltk
from nltk.tokenize import word_tokenize
import os
import shutil

nltk.download('punkt')
TOPIC = "islamophobia"
filespath='{}/page'.format(TOPIC)
files=os.listdir(filespath)
articles = [file.split(".txt")[0] for file in files]
print("Number of articles after collection: {}".format(len(articles)))

decoding_args = OpenAIDecodingArguments(
    max_tokens=512
)

def truncate_sentence(sentence, max_tokens=512):
    tokens = word_tokenize(sentence)

    if len(tokens) <= max_tokens:
        return sentence  # No truncation needed

    truncated_tokens = tokens[:max_tokens]
    truncated_sentence = ' '.join(truncated_tokens)
    truncated_sentence = truncated_sentence + " ..."

    return truncated_sentence

prompt_file_path = 'prompt_filter_page.txt'

# Read the content of the text file into a string
with open(prompt_file_path, 'r', encoding="utf-8") as file:
    prompt = file.read()

prompt_lst = []
for article in articles:
    with open(filespath+"/"+article +".txt", "r", encoding="utf-8") as file:
        article_content = file.read()
    prefix_content = truncate_sentence(article_content, 512)
    prompt_lst.append(prompt.format(article, TOPIC, prefix_content))

# gpt-4-1106-preview gpt-3.5-turbo-1106
results, finish_reason_lst, token_count, cost = openai_complete(prompt_lst, decoding_args, "gpt-4-1106-preview")
print("cost: {}".format(cost))

relevant_articles = []
for i in range(len(results)):
    if results[i] == "YES":
        relevant_articles.append(articles[i])
print("Number of relevant articles after filtering: {}".format(len(relevant_articles)))

def copy_files(file_names, source_folder, destination_folder):
    for file_name in file_names:
        source_path = os.path.join(source_folder, file_name)
        destination_path = os.path.join(destination_folder, file_name)

        # Check if the source file exists
        if os.path.exists(source_path):
            # Create the destination folder if it doesn't exist
            os.makedirs(os.path.dirname(destination_path), exist_ok=True)

            # Copy the file
            shutil.copy(source_path, destination_path)
            print(f"File '{file_name}' copied to '{destination_folder}'.")
        else:
            print(f"File '{file_name}' not found in '{source_folder}'.")

file_names_to_copy = [page+".txt" for page in relevant_articles]
source_folder_path = filespath
destination_folder_path = "{}/filter_page_gpt4".format(TOPIC)
copy_files(file_names_to_copy, source_folder_path, destination_folder_path)

