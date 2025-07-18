import aiohttp
import config

class GobelinosAPI():
    def __init__(self, base_url, token=None):
        self.token = None
        self.base_url = base_url

    def _build_default_headers(self) -> dict:
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    async def get_base_url(self):
        return self.base_url

    async def get(self, endpoint, params=None):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.base_url}/{endpoint}", params=params) as response:
                return await response.json()

    async def post(self, endpoint, data=None):
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.base_url}/{endpoint}", json=data) as response:
                return await response.json()

    async def put(self, endpoint, data=None):
        async with aiohttp.ClientSession() as session:
            async with session.put(f"{self.base_url}/{endpoint}", json=data) as response:
                return await response.json()
    
    async def delete(self, endpoint):
        async with aiohttp.ClientSession() as session:
            async with session.delete(f"{self.base_url}/{endpoint}") as response:
                return await response.json()

    async def patch(self, endpoint, data=None):
        async with aiohttp.ClientSession() as session:
            async with session.patch(f"{self.base_url}/{endpoint}", json=data) as response:
                return await response.json()

    async def login(self, data=None):
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.base_url}/login", headers=self._build_default_headers(), json=data) as response:
                return await response.json()

    
if __name__ == "__main__":
    api = GobelinosAPI(config.Gobelinos_API_URL)
    # Example usage

    import asyncio

    async def main():
        await api.login({"email": config.Gobelinos_API_EMAIL, "password": config.Gobelinos_API_PASSWORD})
        # response = await api.post("endpoint")
        print(response)

    asyncio.run(main())