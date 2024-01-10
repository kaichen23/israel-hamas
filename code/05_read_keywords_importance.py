import pandas as pd
from openai2 import *
import json
from openai2 import *
from collections import Counter

pd.set_option('display.max_rows', None)

# decoding_args = OpenAIDecodingArguments(
#     max_tokens=2000
# )

# zionism free Palestine antisemitism islamophobia
TOPIC = "islamophobia"
results_dict = pd.read_pickle("{}/article_results_dict.pkl".format(TOPIC))
print(results_dict)
with open('{}/article_results_dict.json'.format(TOPIC), 'w') as json_file:
    json_file.write(json.dumps(results_dict, indent=4))

# prompt_file_path = 'prompt_reformate.txt'
#
# # Read the content of the text file into a string
# with open(prompt_file_path, 'r', encoding="utf-8") as file:
#     prompt = file.read()
#
# sum_cost = 0
# reform_results_list = []
# reform_article_results_dict = {}
# for article, results in results_dict.items():
#     prompt_lst = []
#     for result in results:
#         prompt_lst.append(prompt.format(result))
#
#     reform_results, finish_reason_lst, token_count, cost = openai_complete(prompt_lst, decoding_args, "gpt-3.5-turbo")
#     sum_cost += cost
#     reform_results_list.append(reform_results)
#     reform_article_results_dict[article] = reform_results
#
# print("cost: {}".format(sum_cost))
#
# with open('reform_article_results_dict.json', 'w') as json_file:
#     json_file.write(json.dumps(reform_article_results_dict, indent=4))



