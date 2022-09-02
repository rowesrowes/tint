import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
    
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

API_ID = int(getenv("API_ID", "12022658"))
API_HASH = getenv("API_HASH", "c426067dd249a6017518179302b051b7")
BOT_TOKEN = getenv("BOT_TOKEN", "5671315275:AAH6Lu78r63l9h2Kv_U3Y8f-6Ga81sx63fE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "300"))
STRING_SESSION = getenv("STRING_SESSION", "BAC_yzag-KyRsPOPeXXE5unE872wZGK_rfbZvZQlGArx92HJbMKh5I_Xn422cGeY6NTkgmQ2qE_ObHYQLksTvUDx_MPGUFUwZHTEDIOwwjhHTAWhGGKj1DK8JMF6pSTgXDRc1OyKv2bQ7niP8qkm_m8lCe6Kdf1Tifh8xIHanCStNm8qBoN4Sr2_HIdmElV-mewXopgOIvZF1CZdzB5X0vh0Cl623VjYx9_ESdXzFVRsi0rd73CRtuXIQMdZmq_Xxo2yMTvvGgZH_7Aa4CJXQtWNE86bNKK2iRvp_E7T7E4o1GWMzUyIczL4ULjZ1aRRxl42YHgRE6uo5TvPYbeEbkEdAAAAATxCX1EA")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
