import wikipediaapi
import wikipedia
from tqdm import tqdm
import os

# zionism free Palestine antisemitism islamophobia

SEED_KEYWORD = "islamophobia"
CAT_DIR = "{}/page".format(SEED_KEYWORD)
os.makedirs(CAT_DIR)
LANGEUAGES = ["en"]

for LANGEUAGE in LANGEUAGES:
    print(LANGEUAGE)
    # get titles of top relevant articles
    wikipedia.set_lang(LANGEUAGE)
    top_relevant_articles = wikipedia.search(SEED_KEYWORD, results=30)
    # print(top_relevant_articles)
    print("num of top relevant articles: {}".format(len(top_relevant_articles)))

    # initiate api
    wiki_wiki = wikipediaapi.Wikipedia(
        user_agent='chenk7166@gmail.com',
        language=LANGEUAGE,
        extract_format=wikipediaapi.ExtractFormat.WIKI
    )

    # get full text based on title
    num_right_file = 0
    for article in tqdm(top_relevant_articles):
        p_wiki = wiki_wiki.page(article)  # Title of wikipedia page
        if p_wiki.exists():
            article = article.replace("/", "_")
            with open('{}/{}.txt'.format(CAT_DIR, article), 'w',
                      encoding='utf-8') as myfile:
                myfile.write(p_wiki.text)
            num_right_file += 1
        else:
            continue
    print("save {} files".format(num_right_file))