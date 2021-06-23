
import asyncio
import base64
import functools
import os

import colorific


def to_png(location, img_data):
    with open(location, "wb") as file:
        file.write(base64.b64decode(img_data))


def delete_image(path):
    if os.path.exists(path):
        os.remove(path)


def generate_pallet(image_path, max_colors, rgb):
    pallet = colorific.extract_colors(
        image_path, min_prominence=0.1, max_colors=max_colors
    )
    if rgb:
        colors = [c.value for c in pallet.colors]
    else:
        colors = [colorific.rgb_to_hex(c.value) for c in pallet.colors]

    return colors


def to_async(f):
    """
    Can be applied as a decorator to a function to make it async.
    Example:

    @to_async
    def foo(arg):  # Your wrapper for async use
        asyncio.sleep(2)
        return arg

    async def test():
        await foo("Hello")
    """
    @functools.wraps(f)
    def inner(*args, **kwargs):
        loop = asyncio.get_running_loop()
        return loop.run_in_executor(None, lambda: f(*args, **kwargs))

    return inner
