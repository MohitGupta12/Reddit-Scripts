import praw
import os

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Function to prompt user for input
def prompt_user(prompt):
    return input(prompt)

# Function to authenticate with Reddit
def authenticate_with_reddit():
    profile = prompt_user("Enter your Reddit credentials or use Saved profiles (cred/pro): ").lower()
    if profile == "pro":
        print("Choose a profile:")
        print("1. DemandPast")
        print("2. Forsaken-Prince")
        profile_name = prompt_user("Select saved profiles (1/2): ").lower()
        if profile_name == "1":
            username = os.getenv('REDDIT_DEMANDPAST_USERNAME')
            password = os.getenv('REDDIT_DEMANDPAST_PASSWORD')
        elif profile_name == "2":
            username = os.getenv('REDDIT_FORSAKEN_PRINCE_USERNAME')
            password = os.getenv('REDDIT_FORSAKEN_PRINCE_PASSWORD')
        else:
            print("Invalid profile selected.")
            return None
    elif profile == "cred":
        username = prompt_user("Enter your Reddit username: ")
        password = prompt_user("Enter your Reddit password: ")

    reddit = praw.Reddit(
        client_id=os.getenv('REDDIT_CLIENT_ID'),
        client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
        username=username,
        password=password,
        user_agent=os.getenv('REDDIT_USER_AGENT')
    )
# Access the authenticated user's account data
    user = reddit.user.me()
    print(f"Authenticated as u/{user}")

    return reddit

# Function to get list of joined subreddits
def get_joined_subreddits(reddit):
    return list(reddit.user.subreddits())

# Function to create a text file containing subreddit list
def create_subreddit_file(subreddits, username):
    folder_name = "List of subreddits"
    os.makedirs(folder_name, exist_ok=True)
    file_name = f"{username}.txt"
    file_path = os.path.join(folder_name, file_name)

    with open(file_path, 'w') as file:
        for subreddit in subreddits:
            file.write(subreddit.display_name + '\n')

    print(f"Subreddit list saved to '{file_path}'")

def main():
    reddit = authenticate_with_reddit()
    subreddits = get_joined_subreddits(reddit)

    print("Joined subreddits:")

    if wantToSeeSubreddits := input("Do you want to see the subreddits you've joined? (y/n): ").lower() == "y":
        for subreddit in subreddits:
            print(subreddit.display_name)

    create_file = prompt_user("Do you want to create a text file containing the list of subreddits? (y/n): ").lower()
    if create_file == "y":
        create_subreddit_file(subreddits, reddit.user.me().name)
    print("Done.")

if __name__ == "__main__":
    main()
