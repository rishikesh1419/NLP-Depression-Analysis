import praw
import csv
from datetime import datetime

#Create reddit object here using reddit=praw.Reddit(client_id=, client_secret=, username=, password=, user_agent=)

subreddit = reddit.subreddit("askreddit")

hot_ask = subreddit.new(limit=1000)
dict1 = {}

with open("non_dep_data.csv", "a", newline="") as file :
	fieldnames = ["id", "content", "date"]
	writer = csv.DictWriter(file, fieldnames=fieldnames)
	writer.writeheader()
	# i = 0
	for post in hot_ask :
		# print("==============================================================================================")
		# datetime.fromtimestamp(post.created_utc).strftime("%Y-%m-%d %H:%M:%S")
		# print(post.title)
		# print(post.selftext)
		writer.writerow({"id": str(post.id), "content": post.selftext, "date": datetime.fromtimestamp(post.created_utc).strftime("%Y-%m-%d %H:%M:%S")})
		post.comments.replace_more(limit=None)
		# i = i + 1
		# print(i)
		for comment in post.comments.list():
			# print(".................................................................................................")
			# print(datetime.fromtimestamp(comment.created_utc).strftime("%Y-%m-%d %H:%M:%S"))
			# print("C"+str(i),comment.body)
			writer.writerow({"id": str(comment.id), "content": comment.body, "date": datetime.fromtimestamp(comment.created_utc).strftime("%Y-%m-%d %H:%M:%S")})
			# i = i + 1
			# print(i)
			# if i == 5 : 
				# break
