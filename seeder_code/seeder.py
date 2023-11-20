import json
import asyncio

from app.main import client

with open("seeder_code/data.json", "r") as file:
    data = json.load(file)["entry"]


async def seed(data):
    for entry in data:
        await client.create_template(entry)

asyncio.run(seed(data))
