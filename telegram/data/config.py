from environs import Env

# Using the .env file to store the sensitive data
env = Env()
env.read_env()

# Read the values from the .env file
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot Token
ADMINS = env.list("ADMINS")  # Admin LIst

