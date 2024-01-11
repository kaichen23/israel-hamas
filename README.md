# Israel-Hamas Reddit Dataset
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

### Conversation
Each conversation includes one submission with comments. The attribute "comments_df" includes all comments information related to the conversation.

## Data Download



## Keyword Extraction Framework



## Analysis
emotion + moral foundation labeling dataset:
https://drive.google.com/drive/folders/10DJGKjfBe1i_QPrHn1rtByXYgeeBMp4y?usp=sharing
