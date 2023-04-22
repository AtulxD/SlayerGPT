from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")

API_ID = int(getenv("API_ID", 7038415))
API_HASH = getenv("API_HASH", "1f914aa1da15ca6153bbcf09ec1414dc")
BOT_TOKEN = getenv("BOT_TOKEN", "6089831984:AAEAMXZaaRzd0NEb15gHtCudayZllAUxbwY")
OPENAI_API = getenv("OPENAI_API", "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") # get api key : https://platform.openai.com/account/api-keys
