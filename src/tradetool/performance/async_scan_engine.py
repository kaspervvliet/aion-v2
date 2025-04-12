
import asyncio
import aiohttp

async def fetch_asset_data(session, asset):
    url = f"https://api.kraken.com/0/public/Ticker?pair={asset}"
    async with session.get(url) as response:
        return await response.json()

async def scan_all_assets(assets):
    results = {}
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_asset_data(session, asset) for asset in assets]
        data = await asyncio.gather(*tasks)
        for asset, result in zip(assets, data):
            results[asset] = result
    return results

def run_async_scan(assets):
    return asyncio.run(scan_all_assets(assets))
