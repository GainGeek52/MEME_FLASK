
# Meme Gallery

This is a meme gallery web app that fetches memes from the Reddit API and displays them in a sleek and responsive design. The gallery is built using Flask for the backend and HTML/CSS for the frontend. Memes are fetched from the `/r/dankmemes` subreddit, and the app supports dynamic updates via a refresh button and auto-refresh every 45 seconds.

## Features

- Fetch memes from Reddit's `/r/dankmemes` subreddit (can be customized).
- Display meme images, titles, and subreddit names.
- Option to reload the memes via a button.
- Auto-refreshes the page every 45 seconds to show new memes.
- Responsive design for all screen sizes.
- Handles image loading errors gracefully, displaying a default image if needed.

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS
- **API**: Reddit API (using the `praw` Python library)
- **Styling**: Custom CSS for a modern and responsive layout

## Installation

### Prerequisites

- Python 3.8 or higher
- Flask
- praw (Python Reddit API Wrapper)

### Steps

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/meme-gallery.git
   cd meme-gallery
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your Reddit API credentials:
   - Create a Reddit account if you don't have one.
   - Go to [Reddit Apps](https://www.reddit.com/prefs/apps) and create a new application to get your `client_id`, `client_secret`, and `user_agent`.
   - Add these credentials to the `praw.Reddit` initialization in the `app.py` file.

4. Run the Flask app:

   ```bash
   python app.py
   ```

   The app should now be running at `http://localhost:5000`.

## Usage

Once the app is running, visit `http://localhost:5000` in your browser. You can customize the subreddit and the number of memes to display by changing the URL path like so:

- `http://localhost:5000/` - Default subreddit (`dankmemes`) with 6 memes.
- `http://localhost:5000/[subreddit_name]` - Specify a different subreddit.
- `http://localhost:5000/[subreddit_name]/[count]` - Specify a subreddit and the number of memes.

Click the "New Memes" button to reload the page with new memes.

## Contributing

Feel free to fork this repository and submit pull requests. If you find any bugs or issues, please open an issue, and I’ll get back to you.

## License

This project is open-source and available under the MIT License.

---

Make sure to replace `your-username` in the clone URL with your actual GitHub username and update any specific parts like the usage or features according to your actual project requirements.

