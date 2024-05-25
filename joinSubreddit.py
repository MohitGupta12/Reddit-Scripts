import time
import praw
import os

# Load environment variables from .env file
from dotenv import load_dotenv
import os
load_dotenv()

# Authenticate using Reddit app credentials from environment variables
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

# Function to join a subreddit
def join_subreddit(subreddit_name):
    try:
        subreddit = reddit.subreddit(subreddit_name)
        subreddit.subscribe()
        print(f"Successfully joined r/{subreddit_name}")
    except Exception as e:
        print(f"Error joining r/{subreddit_name}: {e}")

# Read subreddit names from a text file
def read_subreddit_file(file_path):
    try:
        with open(file_path, 'r') as file:
            subreddit_names = file.read().splitlines()
        return subreddit_names
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

# Path to the text file containing subreddit names
file_path = input("Enter the path to the text file containing subreddit names (./List of subreddits/my.txt): ")

# Check if the file exists and is a valid text file
if os.path.isfile(file_path) and file_path.endswith('.txt'):
    # Read subreddit names from the file
    print("Path of the file valid.")
    subreddit_names = read_subreddit_file(file_path)

    # Join each subreddit
    for subreddit_name in subreddit_names:
        join_subreddit(subreddit_name)
else:
    print("Invalid file path or file format. Please provide a valid path to a text file.")
# Read subreddit names from the file
subreddit_names = read_subreddit_file(file_path)

# Join each subreddit
for subreddit_name in subreddit_names:
    print(f"Joining r/{subreddit_name}")
    join_subreddit(subreddit_name)

print("Subreddit subscribed successfully.")