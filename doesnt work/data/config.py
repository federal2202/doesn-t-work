# api id, hash
API_ID = 21654633
API_HASH = 'f5372451107097616c4bc58f7106b03d'

USE_TG_BOT = False # True if you want use tg, else False
BOT_TOKEN = '283993:kdmioieiweikiokeocki4okew' # API TOKEN get in @BotFather
CHAT_ID = '22803822' # Your telegram id

# задержка между подключениями к аккаунтам
ACC_DELAY = [5, 15]

# тип прокси
PROXY_TYPE = "socks5" # http/socks5

# папка с сессиями (не менять)
WORKDIR = "sessions/"

# использование прокси
USE_PROXY = True # True/False

PROXY = {
    "USE_PROXY_FROM_FILE": False,  # True - if use proxy from file, False - if use proxy from accounts.json
    "PROXY_PATH": "data/proxy.txt",  # path to file proxy
    "TYPE": {
        "TG": "socks5",  # proxy type for tg client. "socks4", "socks5" and "http" are supported
        "REQUESTS": "socks5"  # proxy type for requests. "http" for https and http proxys, "socks5" for socks5 proxy.
        }
}

# до какого уровня прокачивать
UPGRADE_LEVEL = 20

hello ='''              _                               __  _        
 _ __    ___ | |_  _   _   __ _  ___   ___   / _|| |_  ___ 
| '_ \  / _ \| __|| | | | / _` |/ __| / _ \ | |_ | __|/ __|
| |_) ||  __/| |_ | |_| || (_| |\__ \| (_) ||  _|| |_ \__ \\
| .__/  \___| \__| \__, | \__,_||___/ \___/ |_|   \__||___/
|_|                |___/        

'''

TOOLS = {'Bombucks', 'coinflip', 'BrawlPirates', 'RocketQueen', 'RoyalMines', 'LuckyJet', 'Double', 'AnubisPlinko', 'Mines', 'LuckyLoot', 'RocketX', 'SpeednCash', 'Tower'}
REQUIRED = {'coinflip': None, 'Mines': None, 'Bombucks': None, 'Tower': None, 'Double': 'Mines8', 'RoyalMines': 'coinflip5', 'LuckyLoot': 'coinflip11', 'BrawlPirates': 'Bombucks3', 'AnubisPlinko': 'Tower7', 'RocketX': 'BrawlPirates7', 'SpeednCash': 'AnubisPlinko7', 'RocketQueen': 'LuckyLoot3', 'LuckyJet': 'SpeednCash5'}
PRICES = {'coinflip1': 150, 'coinflip2': 205, 'coinflip3': 275, 'coinflip4': 370, 'coinflip5': 500, 'coinflip6': 675, 'coinflip7': 910, 'coinflip8': 1230, 'coinflip9': 1650, 'coinflip10': 2230, 'coinflip11': 3020, 'coinflip12': 4100, 'coinflip13': 5500, 'coinflip14': 7400, 'coinflip15': 10000.0, 'coinflip16': 13500, 'coinflip17': 18300, 'coinflip18': 24600, 'coinflip19': 33300, 'coinflip20': 45000.0, 'Mines1': 340, 'Mines2': 440, 'Mines3': 570, 'Mines4': 750, 'Mines5': 950, 'Mines6': 1250, 'Mines7': 1650, 'Mines8': 2150, 'Mines9': 2750, 'Mines10': 3600, 'Mines11': 4700, 'Mines12': 6100, 'Mines13': 7900, 'Mines14': 10300, 'Mines15': 13400, 'Mines16': 17400, 'Mines17': 22600, 'Mines18': 29400, 'Mines19': 38200, 'Mines20': 50000.0, 'Bombucks1': 480, 'Bombucks2': 640, 'Bombucks3': 850, 'Bombucks4': 1150, 'Bombucks5': 1500, 'Bombucks6': 2000.0, 'Bombucks7': 3000.0, 'Bombucks8': 4000.0, 'Bombucks9': 5000.0, 'Bombucks10': 6000.0, 'Bombucks11': 8000.0, 'Bombucks12': 11000.0, 'Bombucks13': 15000.0, 'Bombucks14': 20000.0, 'Bombucks15': 26000.0, 'Bombucks16': 35000.0, 'Bombucks17': 46000.0, 'Bombucks18': 61000.0, 'Bombucks19': 81000.0, 'Bombucks20': 110000.0, 'Tower1': 555, 'Tower2': 745, 'Tower3': 995, 'Tower4': 1350, 'Tower5': 1790, 'Tower6': 2400, 'Tower7': 3000.0, 'Tower8': 4000.0, 'Tower9': 6000.0, 'Tower10': 8000.0, 'Tower11': 10000.0, 'Tower12': 14000.0, 'Tower13': 19000.0, 'Tower14': 25000.0, 'Tower15': 33000.0, 'Tower16': 45000.0, 'Tower17': 60000.0, 'Tower18': 80000.0, 'Tower19': 110000.0, 'Tower20': 145000.0, 'Double1': 1200, 'Double2': 1600, 'Double3': 2200, 'Double4': 3000.0, 'Double5': 4000.0, 'Double6': 5400, 'Double7': 7000.0, 'Double8': 10000.0, 'Double9': 13000.0, 'Double10': 18000.0, 'Double11': 24000.0, 'Double12': 33000.0, 'Double13': 44000.0, 'Double14': 59000.0, 'Double15': 80000.0, 'Double16': 110000.0, 'Double17': 150000.0, 'Double18': 200000.0, 'Double19': 270000.0, 'Double20': 360000.0, 'RoyalMines1': 1500, 'RoyalMines2': 2100, 'RoyalMines3': 2900, 'RoyalMines4': 4050, 'RoyalMines5': 5600, 'RoyalMines6': 7800, 'RoyalMines7': 11000.0, 'RoyalMines8': 15000.0, 'RoyalMines9': 21000.0, 'RoyalMines10': 29000.0, 'RoyalMines11': 40000.0, 'RoyalMines12': 56000.0, 'RoyalMines13': 78000.0, 'RoyalMines14': 108000.0, 'RoyalMines15': 151000.0, 'RoyalMines16': 210000.0, 'RoyalMines17': 290000.0, 'RoyalMines18': 400000.0, 'RoyalMines19': 560000.0, 'RoyalMines20': 800000.0, 'LuckyLoot1': 2200, 'LuckyLoot2': 3100, 'LuckyLoot3': 4300, 'LuckyLoot4': 6000.0, 'LuckyLoot5': 8500, 'LuckyLoot6': 11800, 'LuckyLoot7': 17000.0, 'LuckyLoot8': 23000.0, 'LuckyLoot9': 32000.0, 'LuckyLoot10': 45000.0, 'LuckyLoot11': 65000.0, 'LuckyLoot12': 90000.0, 'LuckyLoot13': 125000.0, 'LuckyLoot14': 175000.0, 'LuckyLoot15': 250000.0, 'LuckyLoot16': 350000.0, 'LuckyLoot17': 480000.0, 'LuckyLoot18': 670000.0, 'LuckyLoot19': 950000.0, 'LuckyLoot20': 1500000.0, 'BrawlPirates1': 4000.0, 'BrawlPirates2': 5550, 'BrawlPirates3': 7700, 'BrawlPirates4': 10600, 'BrawlPirates5': 14500, 'BrawlPirates6': 20500, 'BrawlPirates7': 28000.0, 'BrawlPirates8': 39000.0, 'BrawlPirates9': 54000.0, 'BrawlPirates10': 75000.0, 'BrawlPirates11': 105000.0, 'BrawlPirates12': 140000.0, 'BrawlPirates13': 199000.0, 'BrawlPirates14': 275000.0, 'BrawlPirates15': 400000.0, 'BrawlPirates16': 550000.0, 'BrawlPirates17': 750000.0, 'BrawlPirates18': 1000000.0, 'BrawlPirates19': 1400000.0, 'BrawlPirates20': 1950000.0, 'AnubisPlinko1': 5500, 'AnubisPlinko2': 7700, 'AnubisPlinko3': 11000.0, 'AnubisPlinko4': 15000.0, 'AnubisPlinko5': 21000.0, 'AnubisPlinko6': 30000.0, 'AnubisPlinko7': 41000.0, 'AnubisPlinko8': 60000.0, 'AnubisPlinko9': 82000.0, 'AnubisPlinko10': 115000.0, 'AnubisPlinko11': 160000.0, 'AnubisPlinko12': 225000.0, 'AnubisPlinko13': 310000.0, 'AnubisPlinko14': 440000.0, 'AnubisPlinko15': 610000.0, 'AnubisPlinko16': 850000.0, 'AnubisPlinko17': 1200000.0, 'AnubisPlinko18': 1700000.0, 'AnubisPlinko19': 2500000.0, 'AnubisPlinko20': 3300000.0, 'RocketX1': 20000.0, 'RocketX2': 30000.0, 'RocketX3': 45000.0, 'RocketX4': 70000.0, 'RocketX5': 100000.0, 'RocketX6': 150000.0, 'RocketX7': 250000.0, 'RocketX8': 350000.0, 'RocketX9': 500000.0, 'RocketX10': 770000.0, 'RocketX11': 1150000.0, 'RocketX12': 1750000.0, 'RocketX13': 2600000.0, 'RocketX14': 3900000.0, 'RocketX15': 5800000.0, 'RocketX16': 9000000.0, 'RocketX17': 13000000.0, 'RocketX18': 19500000.0, 'RocketX19': 29500000.0, 'RocketX20': 44500000.0, 'SpeednCash1': 33333, 'SpeednCash2': 50000.0, 'SpeednCash3': 75000.0, 'SpeednCash4': 110000.0, 'SpeednCash5': 170000.0, 'SpeednCash6': 255000.0, 'SpeednCash7': 400000.0, 'SpeednCash8': 550000.0, 'SpeednCash9': 850000.0, 'SpeednCash10': 1300000.0, 'SpeednCash11': 1900000.0, 'SpeednCash12': 3000000.0, 'SpeednCash13': 4300000.0, 'SpeednCash14': 6500000.0, 'SpeednCash15': 9700000.0, 'SpeednCash16': 14500000.0, 'SpeednCash17': 22000000.0, 'SpeednCash18': 33000000.0, 'посхалко': 666.000, 'SpeednCash19': 50000000.0, 'SpeednCash20': 75000000.0, 'RocketQueen1': 50000.0, 'RocketQueen2': 77500, 'RocketQueen3': 120000.0, 'RocketQueen4': 200000.0, 'RocketQueen5': 300000.0, 'RocketQueen6': 450000.0, 'RocketQueen7': 700000.0, 'RocketQueen8': 1100000.0, 'RocketQueen9': 1700000.0, 'RocketQueen10': 2600000.0, 'RocketQueen11': 4000000.0, 'RocketQueen12': 6000000.0, 'RocketQueen13': 9600000.0, 'RocketQueen14': 14900000.0, 'RocketQueen15': 23100000.0, 'RocketQueen16': 36000000.0, 'RocketQueen17': 55500000.0, 'RocketQueen18': 86000000.0, 'RocketQueen19': 130000000.0, 'RocketQueen20': 205000000.0, 'LuckyJet1': 100000.0, 'LuckyJet2': 165000.0, 'LuckyJet3': 300000.0, 'LuckyJet4': 450000.0, 'LuckyJet5': 700000.0, 'LuckyJet6': 1200000.0, 'LuckyJet7': 2000000.0, 'LuckyJet8': 3300000.0, 'LuckyJet9': 5500000.0, 'LuckyJet10': 9100000.0, 'LuckyJet11': 15000000.0, 'LuckyJet12': 25000000.0, 'LuckyJet13': 41000000.0, 'LuckyJet14': 65000000.0, 'LuckyJet15': 110000000.0, 'LuckyJet16': 185000000.0, 'LuckyJet17': 300000000.0, 'LuckyJet18': 500000000.0, 'LuckyJet19': 820000000.0, 'LuckyJet20': 1500000000.0}
