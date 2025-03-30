import discord
from discord.ext import commands
from datetime import datetime, timedelta
import pytz
from dotenv import load_dotenv
import os

load_dotenv()

bot_token=os.getenv('DISCORD_BOT_TOKEN')


intents = discord.Intents.default()
intents.members = True  # Allow the bot to access the members list (optional, based on your use case)
intents.message_content = True  # Allow the bot to read message content
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def collectids(ctx):
    try:
        # Get the channel name, start date, and end date from the user input
        await ctx.send("Please enter the channel name (e.g., 'general'):")
        channel_name = await bot.wait_for('message', check=lambda m: m.author == ctx.author, timeout=60)
        channel_name = channel_name.content.strip()

        await ctx.send("Please enter the start date (YYYY-MM-DD):")
        start_date_msg = await bot.wait_for('message', check=lambda m: m.author == ctx.author, timeout=60)
        start_date = start_date_msg.content.strip()

        await ctx.send("Please enter the end date (YYYY-MM-DD):")
        end_date_msg = await bot.wait_for('message', check=lambda m: m.author == ctx.author, timeout=60)
        end_date = end_date_msg.content.strip()

        # Convert start and end date strings into datetime objects
        start_datetime = datetime.strptime(start_date, "%Y-%m-%d")
        end_datetime = datetime.strptime(end_date, "%Y-%m-%d") + timedelta(days=1)  # End date is inclusive

        # Set timezone to UTC
        timezone = pytz.timezone('UTC')
        start_datetime = timezone.localize(start_datetime)
        end_datetime = timezone.localize(end_datetime)

        # Fetch the guild (server) where the command was issued
        guild = ctx.guild

        # Fetch the channel by name
        channel = discord.utils.get(guild.text_channels, name=channel_name)
        if not channel:
            await ctx.send(f"Channel '{channel_name}' not found.")
            return
        
        await ctx.send(f"Collecting user IDs from {start_datetime} to {end_datetime} in channel '{channel_name}'.")

        # Collect user IDs from the specified channel and date range
        user_ids = []
        async for message in channel.history(after=start_datetime, before=end_datetime):
            if start_datetime <= message.created_at < end_datetime:
                user_ids.append(message.author.id)

        await ctx.send(f"Collected {len(user_ids)} unique user IDs.")
        
        # Save the IDs to a file
        with open("user_ids.txt", "w") as f:
            for user_id in user_ids:
                f.write(f"{user_id}\n")
        
        await ctx.send("User IDs have been saved to 'user_ids.txt'.")
    
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")

bot.run(bot_token)
