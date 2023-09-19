from argparse import ArgumentParser
from aiohttp import ClientSession
import requests
import asyncio
import time


URL = "https://6wrlmkp9u2.execute-api.us-east-1.amazonaws.com/"


async def perform_async_request(session, url, i):
    async with session.get(url) as response:
        response = await response.read()
        print(i)
        return response

async def asynchronous_requests():
    time_start = time.time()
    async with ClientSession() as session:
        tasks = [perform_async_request(session, URL, i) for i in range(10)]
        await asyncio.gather(*tasks)
    time_end = time.time()
    print(f"Time taken: {time_end - time_start}")

def synchronous_requests():
    time_start = time.time()
    for i in range(10):
        requests.get(URL)
        print(i)
    time_end = time.time()
    print(f"Time taken: {time_end - time_start}")



if __name__ == '__main__':
    parser = ArgumentParser()

    parser.add_argument('--use-async', action="store_true")
    args = parser.parse_args()
    if args.use_async:
        asyncio.run(asynchronous_requests())
    else:
        synchronous_requests()