import hashlib

LIMIT = 100000000000 #limit pokusů
zero = 8 #počet 0 přes hashem

print("[INFO] Vyhledávání hashe bylo spuštěno!")

def tezba(block, transakce, predchozi_hash):
    for nonce in range(LIMIT):
        text = str(block) + transakce + predchozi_hash + str(nonce)
        hash_test = hashlib.sha256(text.encode()).hexdigest()
        if hash_test.startswith('0' * zero):
            print("[INFO] Nalezen hash s nulou: {nonce}")
            return hash_test
    return -1
block = 24
transakce = "3QqgeYKQF8qA2FeVVkt6mDkeqvbbZKzB4z"
predchozi_hash = "00000000839a8e6886ab5951d76f411475428afc90947ee320161bbf18eb6048" #aktuálně počítaný hash - https://www.blockchain.com/btc/block/1

tezba(block, transakce, predchozi_hash)
