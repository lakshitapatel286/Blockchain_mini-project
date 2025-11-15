from block import Block
from digital_signature import verify_signature


class Blockchain:
    def _init_(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(
            index=0,
            previous_hash="0",
            transaction="Genesis Block",
            signature=b"",
            public_key=None
        )

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, transaction, signature, public_key):
        # Verify transaction signature before adding
        if not verify_signature(public_key, transaction, signature):
            print("❌ Invalid digital signature. Block rejected.")
            return False

        prev_block = self.get_latest_block()
        new_block = Block(
            index=len(self.chain),
            previous_hash=prev_block.hash,
            transaction=transaction,
            signature=signature,
            public_key=public_key
        )
        self.chain.append(new_block)
        print("✔ Block added successfully!")
        return True

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            block = self.chain[i]
            prev_block = self.chain[i - 1]

            if block.hash != block.calculate_hash():
                return False

            if block.previous_hash != prev_block.hash:
                return False

        return True