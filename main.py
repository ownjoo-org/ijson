import logging
from asyncio import gather, run
from io import BytesIO
from json import dumps

from ijson import items, kvitems
from requests import get

stream_file: BytesIO = BytesIO()

logger = logging.getLogger(name=__name__)
logging.basicConfig(level=10)


async def stream_data():
    with get(
            url='http://localhost:3000',
            stream=True,
    ) as resp:
        resp.raise_for_status()
        for item in items(resp.raw, 'item'):
            print(item)


async def main():
    await gather(
        stream_data(),
    )


if __name__ == '__main__':
    run(main())
    # test: dict = {
    #     'key0': 'val0',
    #     'key1': {
    #         'key2': [
    #             {
    #                 'key3': [
    #                     {'2key0': '2val0'},
    #                     {'2key1': '2val1'},
    #                 ],
    #             },
    #         ],
    #     },
    # }
    # for each in items(dumps(test), 'key1.key2.item.key3.item'):
    #     print(f'main: {each}')
