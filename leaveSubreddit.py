from dotenv import load_dotenv
import os
import praw

load_dotenv()

# Authenticate using your Reddit app credentials
reddit = praw.Reddit(
    client_id=os.getenv('REDDIT_CLIENT_ID'),
    client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
    username=os.getenv('REDDIT_DEMANDPAST_USERNAME'),
    password=os.getenv('REDDIT_DEMANDPAST_PASSWORD'),
    user_agent=os.getenv('REDDIT_USER_AGENT')
)

# Access the authenticated user's account data
user = reddit.user.me()
print(f"Authenticated as u/{user}")

# Function to leave a subreddit
def leave_subreddit(subreddit_name):
    try:
        subreddit = reddit.subreddit(subreddit_name)
        subreddit.unsubscribe()
        print(f"You have left r/{subreddit_name}")
    except Exception as e:
        print(f"Error leaving r/{subreddit_name}: {e}")

# Get a list of subreddits the user has joined
subreddits = list(reddit.user.subreddits())
print(f"No. of subreddits you've joined:{len(subreddits)}")
if len(subreddits) > 0:
    if wantToSeeSubreddits := input("Do you want to see the subreddits you've joined? (y/n): ").lower() == "y":
        for subreddit in subreddits:
            print(subreddit.display_name)

    # Leave subreddits
    if wantToLeaveAllSubreddits := input("Do you want to leave all subreddits? (y/n): ").lower() == "y":
        for subreddit in subreddits:
            length = len(subreddits)
            if length < 5:
                leave = input(f"Do you want to leave r/{subreddit.display_name}? (y/n): ").lower()
                if leave == "y":
                    leave_subreddit(subreddit.display_name)
            else:
                leave_subreddit(subreddit.display_name)

print("Done leaving subreddits.")
