import instaloader
from datetime import datetime
import os

def download_instagram_media(username, until_date):
    """
    Downloads Instagram images and videos from a given username until a specified date.
    
    :param username: Instagram username to download media from.
    :param until_date: Date in 'YYYY-MM-DD' format until which to download media.
    """
    # Convert until_date to a datetime object
    until_date = datetime.strptime(until_date, '%Y-%m-%d')

    # Initialize Instaloader
    loader = instaloader.Instaloader()

    # Log in to Instagram
    try:
        # Replace with your Instagram credentials or load them from a secure location
        loader.login('grace06795', 'Jesus@#99')
    except instaloader.exceptions.BadCredentialsException:
        print("Invalid username or password.")
        return

    # Download media from the given Instagram username
    try:
        # Load profile
        profile = instaloader.Profile.from_username(loader.context, username)

        # Create a directory for the account's media
        target_dir = f"{username}_media"
        os.makedirs(target_dir, exist_ok=True)

        # Loop through posts and download both images and videos
        for post in profile.get_posts():
            # Stop downloading if the post is older than until_date
            if post.date < until_date:
                break

            # Format the date for the filename
            media_date = post.date.strftime("%Y-%m-%d")
            extension = "mp4" if post.is_video else "jpg"
            filename = f"{target_dir}/{media_date}_{post.shortcode}.{extension}"
            
            # Download the media
            print(f"Downloading {'video' if post.is_video else 'image'} from post: {post.shortcode} ({post.date})")
            loader.download_post(post, target=target_dir)

            # Rename the downloaded media to use the date format
            downloaded_files = os.listdir(target_dir)
            for file in downloaded_files:
                if file.startswith(post.shortcode):
                    os.rename(os.path.join(target_dir, file), filename)
                    break

        print("Download complete!")
        
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Profile '{username}' does not exist.")
    except instaloader.exceptions.LoginRequiredException:
        print("Login is required. Please check your credentials or try again later.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
download_instagram_media('mla.krishnakhopde', '2024-01-01')