import praw
###https://praw.readthedocs.io/en/latest/code_overview/reddit/user.html
###praw api docs

#### Initializes the credential to login into reddit
red_id = {};
with open("redscrapper.ini") as filein:
    for line in filein:
        (key,val) = line.strip().split('=')
        red_id[key] = val
    
# reddit authenticating process
reddit = praw.Reddit(client_id=red_id["client_id"], client_secret=red_id["client_secret"], user_agent=red_id["user_agent"], username=red_id["username"], password=red_id["password"])

# subreddit scanning
for submission in reddit.subreddit('pokemongo').hot(limit=20):
    print("==========================================================\n", submission.title, "\n", submission.selftext, "\n")
    ##print("Comments:\n", submission.comments.list())
    
# # users subreddits
# for sub in reddit.user.subreddits():
    # print(sub)

    

