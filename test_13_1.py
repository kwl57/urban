import asyncio
import time

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования!')
    for i in range(1, 6):
        print(f'Силач {name} поднял шар номер {i}')
        await asyncio.sleep(1/power)
    print(f'Силач {name} закончил соревнования!')

async def start_tournament():
    task_1 = asyncio.create_task(start_strongman('Ivanov', 1))
    task_2 = asyncio.create_task(start_strongman('Sidorov', 2))
    task_3 = asyncio.create_task(start_strongman('Petrov', 3))
    await task_1
    await task_2
    await task_3

st = time.time()
asyncio.run(start_tournament())
stop = time.time()

print(f'Соревнования длились {round(stop - st, 1)} секунд')

