
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
# Multisig wallet
#
# Docs: https://github.com/vbuterin/pybitcointools
# pip install bitcoin 

from bitcoin import *

def main():

    # 4 PPKs
    private_key1 = random_key()
    public_key1 = privtopub(private_key1)

    private_key2 = random_key()
    public_key2 = privtopub(private_key2)
    
    private_key3 = random_key()
    public_key3 = privtopub(private_key3)
    
    private_key4 = random_key()
    public_key4 = privtopub(private_key4)

    # Multisig public key
    multisig = mk_multisig_script(public_key1, public_key2, public_key3, public_key4,4)
    print("Multisig: ", multisig)

    # Bitcoin address
    bitcoin_address = scriptaddr(multisig)
    print("Bitcoin address: ",bitcoin_address)
    

if __name__ == "__main__":
    main()