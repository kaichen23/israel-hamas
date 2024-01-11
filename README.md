# IsamasRed: Israel-Hamas Conflict Reddit Dataset
## Overview

- Time: August 1 to November 30, 2023
- Number of Submissions (posts): 412,258
- Number of Comments: 8,089,095

## Detail
### Attributes in Submissions
- Subreddit
- id
- author
- timestamp
- title
- text: supplemental text for title
- score: number of upvotes minus downvotes
- upvote_ratio: number of upvotes / (number of upvotes + downvotes)
- upvotes: number of upvotes

### Attributes in Comments
- Subreddit
- id
- text
- author
- timestamp
- submission_id
- controversial: whether is controversial, labeled by Reddit
- score
- ups: number of upvotes
- downs: number of downvotes
- parent_id: last level comment or submission

### Conversations
Each conversation includes one submission with comments.

**Attribute**
- comments_df: All comments information in the conversation
- freepalestine_islamophobia: 0 or 1. 1 means this conversation is related to Free palestine/islamophobia topic.
- zionism_antisemitism

## Data Download
All datasets are saved to JSON type files. This repository contains a sample of five hundred submissions, comments, and conversations data, along with an ID file extracted from the complete dataset.  Please contact the author (**kchen035@usc.edu**) to access the entire dataset.

## Keyword Extraction

<img src="framework.jpg" width="700">

The framework of keyword extraction. Initially, we conduct a keyword search on Wikipedia using seed keywords to identify pages related to a specific topic. Subsequently, we employ GPT 4 to filter out pages with weak relevance. Each page is then sequentially segmented into multiple text chunks, enabling keyword extraction via GPT 4. Finally, we concatenate these raw keywords and rank them to form a refined set of keywords for subsequent data collection.

The framework code and the Israel-Hamas Conflict keywords are uploaded to the repository.

## Analysis
emotion + moral foundation labeling dataset:
https://drive.google.com/drive/folders/10DJGKjfBe1i_QPrHn1rtByXYgeeBMp4y?usp=sharing
