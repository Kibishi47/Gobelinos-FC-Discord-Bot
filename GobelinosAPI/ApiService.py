import aiohttp
import config

class GobelinosAPI():
    def __init__(self, base_url, token=None):
        self.token = None
        self.base_url = base_url
        self.headers = self._build_default_headers()

    def _build_default_headers(self) -> dict:
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    def _set_token(self, token):
        self.token = token
        self.headers = self._build_default_headers()

    async def get_base_url(self):
        return self.base_url

    async def get(self, endpoint, params=None):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.base_url}/{endpoint}",headers=self.headers, params=params) as response:
                return await response.json()

    async def post(self, endpoint, data=None):
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.base_url}/{endpoint}",headers=self.headers, json=data) as response:
                return await response.json()

    async def put(self, endpoint, data=None):
        async with aiohttp.ClientSession() as session:
            async with session.put(f"{self.base_url}/{endpoint}",headers=self.headers, json=data) as response:
                return await response.json()
    
    async def delete(self, endpoint):
        async with aiohttp.ClientSession() as session:
            async with session.delete(f"{self.base_url}/{endpoint}",headers=self.headers) as response:
                return await response.json()

    async def patch(self, endpoint, data=None):
        async with aiohttp.ClientSession() as session:
            async with session.patch(f"{self.base_url}/{endpoint}",headers=self.headers, json=data) as response:
                return await response.json()

    async def login(self):
        endpoint = "login"
        data = {
            "email": config.Gobelinos_API_EMAIL, 
            "password": config.Gobelinos_API_PASSWORD
        }
        tokenJSON = await self.post(endpoint, data)
        if tokenJSON:
            self._set_token(tokenJSON['token'])
            return self.token
        else:
            raise Exception("Failed to login, check your credentials.")
        

    
if __name__ == "__main__":
    api = GobelinosAPI(config.Gobelinos_API_URL)
    # Example usage

    import asyncio

    async def main():
        response = await api.login()
        response = await api.get("games")
        print(response)

    asyncio.run(main())