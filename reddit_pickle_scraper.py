import praw
import pandas as pd
import pickle
# Define user agent details
r = praw.Reddit(user_agent=user_agent, client_id=reddit_client_id, client_secret=reddit_client_secret)
epressed_posts_titles = []
depressed_posts_content = []
depressed_comments = []
depressed_dict = {"title": [],
                 "id": [],
                 "num_comments": [],
                 "comments": [],
                 "content": []}
non_depressed_dict = {"title": [],
                     "id": [],
                     "num_comments": [],
                     "comments": [],
                     "content": []}
def depressed_data(subreddit):
    for post in r.subreddit(subreddit).top(limit=1000):
        post.comments.replace_more(limit=100)
        depressed_dict['title'].append(post.title)
        depressed_dict['id'].append(post.id)
        depressed_dict['num_comments'].append(post.num_comments)
        comments = post.comments.list()
        comments_new = []
        for comment in comments:
            comments_new.append(comment.body)
        depressed_dict['comments'].append(comments_new)
        depressed_dict['content'].append(post.selftext)
    depressed_df = pd.DataFrame(depressed_dict)
    depressed_df.drop_duplicates(subset=['id'], inplace=True)
    print("Total number of comments: ", sum(depressed_df['num_comments']))
    print(depressed_df)


def non_depressed_data(subreddit):
    for post in r.subreddit(subreddit).hot(limit=1000):
        post.comments.replace_more(limit=100)
        non_depressed_dict['title'].append(post.title)
        non_depressed_dict['id'].append(post.id)
        non_depressed_dict['num_comments'].append(post.num_comments)
        comments = post.comments.list()
        comments_new = []
        for comment in comments:
            comments_new.append(comment.body)
        non_depressed_dict['comments'].append(comments_new)
        non_depressed_dict['content'].append(post.selftext)
    non_depressed_df = pd.DataFrame(non_depressed_dict)
    non_depressed_df.drop_duplicates(subset=['id'], inplace=True)
    print("Total number of comments: ", sum(non_depressed_df['num_comments']))
    print(non_depressed_df)

depressed_data('depression')
non_depressed_data('askreddit')

depressed_pickle = open("depressed.pickle","wb")
pickle.dump(depressed_dict, depressed_pickle)
depressed_pickle.close()

test_depressed_pickle = open("depressed.pickle","rb")
test_depressed_pickle_dict = pickle.load(test_depressed_pickle)

depressed_df2 = pd.DataFrame(test_depressed_pickle_dict)
depressed_df2.drop_duplicates(subset=['id'], inplace=True)
print("test Total number of comments: ", sum(depressed_df2['num_comments']))


non_depressed_pickle = open("non_depressed.pickle","wb")
pickle.dump(non_depressed_dict, non_depressed_pickle)
non_depressed_pickle.close()

test_non_depressed_pickle = open("non_depressed.pickle","rb")
test_non_depressed_pickle_dict = pickle.load(test_non_depressed_pickle)
non_depressed_df2 = pd.DataFrame(test_non_depressed_pickle_dict)
non_depressed_df2.drop_duplicates(subset=['id'], inplace=True)
print("test Total number of comments: ", sum(non_depressed_df2['num_comments']))
