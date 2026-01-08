import httpx

async def fetch_external_summary():
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://jsonplaceholder.typicode.com/posts/1"
        )
        data = response.json()
        return data.get("body")
