from fastapi import FastAPI

app = FastAPI()


@app.get('/api/get_funds')
async def get_funds(wallet_address: str = ''):
    return wallet_address
