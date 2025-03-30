# Discord ID Tracker Bot

A Discord bot to collect user IDs from a specified channel within a date range and save them to a text file (`user_ids.txt`).

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
