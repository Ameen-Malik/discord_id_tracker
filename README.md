# Discord ID Tracker Bot
This is a Discord bot that collects the user IDs of people who have posted messages in a specific channel of your Discord server within a given date range. It saves these IDs to a (`user_ids.txt`) text file, which can be used for tracking user engagement or any other purpose.
## Setup

Follow the steps below to set up the bot:

### Prerequisites

- Python 3.7+ is required.
- A Discord bot token.
- A `.env` file to store the bot token.

### Steps to Set Up

1. **Clone the repository:**

   If you haven't already, clone the repository to your local machine:
   ```bash
   git clone https://github.com/Ameen-Malik/discord_id_tracker.git
   cd discord_id_tracker
   ```
2. **Create a .env file:**

   Create a .env file in the root directory of the project. This file will store the Discord bot token:

   ```bash
   DISCORD_BOT_TOKEN=your_discord_bot_token
   ```   
3. **Install the required dependencies:**
   Install the Python dependencies by running:

   ```bash
   pip install -r requirements.txt
   ```
4. **Run the bot:**

   Start the bot by running the following command:

   ```bash
   python main.py
   ```
The bot will now be running and will log in to Discord using the provided bot token.
