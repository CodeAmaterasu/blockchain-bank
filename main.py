from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import json
import ecdsa

app = FastAPI()


class GetFundsContainer(BaseModel):
    wallet_address: str
    amount: str


app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/api/get_funds')
async def get_funds(get_funds_container: GetFundsContainer):
    sk = ecdsa.SigningKey.from_string(bytes.fromhex("a14b3cf0f4a8b9344a655565e3077505f3b64125c10b0ef3c2384e53f647aaa6"),
                                      curve=ecdsa.SECP256k1)
    signed_source = sk.sign(bytes(str(get_funds_container.amount), 'utf-8'))
    block = {
        "origin": '4w5wYUcjv1HXIboBK0B1Cczt6YBCCM1dMdBMjovWk068W+SuaQ3plenGsV9zAgGVmVtiAY10iDIlJlpMB3zuig==',
        "amount": get_funds_container.amount,
        "signature": str(signed_source.hex()),
        "destination": get_funds_container.wallet_address
    }
    print(block)
    requests.post(url='https://blockchain.danilojakob.ch/api/create_block', data=json.dumps(block))
