from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")

API_ID = int(getenv("API_ID", 7038415))
API_HASH = getenv("API_HASH", "1f914aa1da15ca6153bbcf09ec1414dc")
BOT_TOKEN = getenv("BOT_TOKEN", "6089831984:AAEAMXZaaRzd0NEb15gHtCudayZllAUxbwY")
OPENAI_API = getenv("OPENAI_API", "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") # get api key : https://platform.openai.com/account/api-keys
