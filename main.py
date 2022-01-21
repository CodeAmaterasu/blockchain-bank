from fastapi import FastAPI
import requests
import json
import ecdsa

app = FastAPI()


@app.get('/api/get_funds')
async def get_funds(wallet_address: str = '', amount: str = ''):
    sk = ecdsa.SigningKey.from_string(bytes.fromhex("a14b3cf0f4a8b9344a655565e3077505f3b64125c10b0ef3c2384e53f647aaa6"),
                                      curve=ecdsa.SECP256k1)
    signed_source = sk.sign(bytes(str(amount), 'utf-8'))
    block = {
        "origin": '4w5wYUcjv1HXIboBK0B1Cczt6YBCCM1dMdBMjovWk068W+SuaQ3plenGsV9zAgGVmVtiAY10iDIlJlpMB3zuig==',
        "amount": amount,
        "signature": str(signed_source.hex()),
        "destination": wallet_address
    }
    print(block)
    requests.post(url='https://blockchain.danilojakob.ch/api/create_block', data=json.dumps(block))
