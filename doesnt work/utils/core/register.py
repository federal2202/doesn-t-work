# from loguru import logger
# from data import config
# import pyrogram
# from data.config import USE_PROXY
# import random
# from file_manager import save_to_json

# async def create_sessions():
#     while True:
#         session_name = input('\nInput the name of the session (press Enter to exit): ')
#         if not session_name: return

#         proxy = input("Input the proxy in the format login:password@ip:port (press Enter to use without proxy): ")
#         # if USE_PROXY:
#         #     proxy_dict = {}
#         #     with open('proxy.txt','r') as file:
#         #         proxy_list = [i.strip().split() for i in file.readlines() if len(i.strip().split()) == 2]
#         #         for prox,name in proxy_list:
#         #             proxy_dict[name] = prox
            
#         if proxy:
#             client_proxy = {
#                 "scheme": config.PROXY_TYPE,
#                 "hostname": proxy.split(":")[1].split("@")[1],
#                 "port": int(proxy.split(":")[2]),
#                 "username": proxy.split(":")[0],
#                 "password": proxy.split(":")[1].split("@")[0]
#             }
#         else:
#             client_proxy, proxy = None, None
                
#         session = pyrogram.Client(
#             api_id=config.API_ID,
#             api_hash=config.API_HASH,
#             name=session_name,
#             workdir=config.WORKDIR,
#             proxy=client_proxy
#         )

#         async with session:
#             user_data = await session.get_me()

#         logger.success(f'Добавлена сессия +{user_data.phone_number} @{user_data.username} PROXY {proxy.split(":")[0]}')
#     else:
            
#         session = pyrogram.Client(
#             api_id=config.API_ID,
#             api_hash=config.API_HASH,
#             name=session_name,
#             workdir=config.WORKDIR
#         )

#         async with session:
#             user_data = await session.get_me()
    
#     save_to_json(f'{config.WORKDIR}accounts.json', dict_={
#                 "session_name": session_name,
#                 "phone_number": phone_number,
#                 "proxy": proxy
#             })
    
#     logger.success(f'Добавлена сессия +{user_data.phone_number} @{user_data.username} PROXY : NONE')
