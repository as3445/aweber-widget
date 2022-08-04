import asyncio

from prisma import Prisma
from prisma.models import Widget

widgets_seed_data = [
    {"name": "w1", "parts": 5},
    {"name": "w2", "parts": 2},
    {"name": "w3", "parts": 3},
]


async def seed():
    prisma = Prisma(auto_register=True)
    await prisma.connect()
    await Widget.prisma().delete_many()
    for widget in widgets_seed_data:
        await Widget.prisma().create(widget)
    await prisma.disconnect()


if __name__ == "__main__":
    asyncio.run(seed())
