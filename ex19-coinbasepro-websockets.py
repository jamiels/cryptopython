# Copyright Chainhaus
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# GDAX
#
# Docs: https://docs.gdax.com/#websocket-feed

import asyncio
import websockets
import json


def main():
    asyncio.get_event_loop().run_until_complete(start_gdax_websocket())

async def start_gdax_websocket():
    async with websockets.connect('wss://ws-feed.gdax.com') as websocket:
        await websocket.send(build_request())
        async for m in websocket:
            print(m)

def build_request():
    return "{ \"type\": \"subscribe\",    \"channels\": [{ \"name\": \"ticker\", \"product_ids\": [\"ETH-USD\"] }]}"

if __name__ == "__main__":
    main()
