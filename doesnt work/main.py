# from utils.core import create_sessions
# from utils.telegram import Accounts
from utils.onewin import OneWin
# from data.config import hello,USE_PROXY
# import asyncio
# import os
from utils.tel import Accounts
# from utils.starter import start, stats
import asyncio
from data import config
from itertools import zip_longest
from utils.core import get_all_lines
import os

# async def main():
#     print(hello)
#     action = int(input('Выберите действие:\n1. Начать сбор монет\n2. Сoздать сессию\n>'))
#     2
#     if not os.path.exists('sessions'):
#         os.mkdir('sessions')
    
#     if action == 2:
#         await Accounts().create_sessions()

#     if action == 1:
#         accounts = await Accounts().get_accounts()
                
#         tasks = []
#         if USE_PROXY:
#             proxy_dict = {}
#             with open('proxy.txt','r',encoding='utf-8') as file:
#                 proxy = [i.strip().split() for i in file.readlines() if len(i.strip().split()) == 2]
#                 for prox,name in proxy:
#                     proxy_dict[name] = prox
#             for thread, account in enumerate(accounts):
#                 if account in proxy_dict:
#                     tasks.append(asyncio.create_task(OneWin(account=account, thread=thread, proxy=proxy_dict[account]).main()))
#                 else:
#                     tasks.append(asyncio.create_task(OneWin(account=account, thread=thread,proxy = None).main()))
#         else:
            # for thread, account in enumerate(accounts):
            #     session_name, phone_number, proxy = account.values()
            #     tasks.append(asyncio.create_task(OneWin(account=account, thread=thread,proxy = None).main()))
#         await asyncio.gather(*tasks)

# if __name__ == '__main__':
#     asyncio.run(main())


async def main():
    action = int(input("Select action:\n0. About soft\n1. Start soft\n2. Get statistics\n3. Create sessions\n\n> "))

    if action == 0:
        print(config.SOFT_INFO)
        return

    if not os.path.exists('sessions'): os.mkdir('sessions')

    if config.PROXY['USE_PROXY_FROM_FILE']:
        if not os.path.exists(config.PROXY['PROXY_PATH']):
            with open(config.PROXY['PROXY_PATH'], 'w') as f:
                f.write("")
    else:
        if not os.path.exists('sessions/accounts.json'):
            with open("sessions/accounts.json", 'w') as f:
                f.write("[]")

    # if action == 3:
    #     await Accounts().create_sessions()

    if action == 1:
        accounts = await Accounts().get_accounts()

        tasks = []

        if config.PROXY['USE_PROXY_FROM_FILE']:
            # proxys = get_all_lines(config.PROXY['PROXY_PATH'])
            # for thread, (account, proxy) in enumerate(zip_longest(accounts, proxys)):
            #     if not account: break
            #     session_name, phone_number, proxy = account.values()
            #     tasks.append(asyncio.create_task(start(session_name=session_name, phone_number=phone_number, thread=thread, proxy=proxy)))
            pass
        else:
           for thread, account in enumerate(accounts):
                session_name, thread, proxy = account.values()
                tasks.append(asyncio.create_task(OneWin(session_name=session_name, thread=thread, proxy=proxy).main()))

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())