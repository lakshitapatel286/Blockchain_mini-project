import hashlib
import json
import time

class Block:
    def _init_(self, index, previous_hash, transaction, signature, public_key, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.transaction = transaction
        self.signature = signature
        self.public_key = public_key
        self.timestamp = timestamp or time.time()
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({
            "index": self.index,
            "previous_hash": self.previous_hash,
            "transaction": self.transaction,
            "signature": self.signature.hex(),
            "public_key": self.public_key.save_pkcs1().decode(),
            "timestamp": self.timestamp
        }, sort_keys=True).encode()

        return hashlib.sha256(block_string).hexdigest()