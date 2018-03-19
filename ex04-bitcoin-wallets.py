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
# Public / Private Key wallet
#
# Docs: https://github.com/vbuterin/pybitcointools
# pip install bitcoin 

from bitcoin import *

def main():

    private_key = random_key()
    public_key = privtopub(private_key)
    bitcoin_address = pubtoaddr(public_key)

    print("Private key: ",private_key)
    print("Public key: ",public_key)
    print("Bitcoin address: ", bitcoin_address)
    

if __name__ == "__main__":
    main()