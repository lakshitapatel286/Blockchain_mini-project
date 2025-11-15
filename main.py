from blockchain import Blockchain
from digital_signature import generate_keys, sign_transaction


# Create blockchain
blockchain = Blockchain()

# Generate digital signature keys
public_key, private_key = generate_keys()

# Create some transactions
transaction1 = "Alice pays Bob 10 coins"
signature1 = sign_transaction(private_key, transaction1)

# Add block
blockchain.add_block(transaction1, signature1, public_key)

# Check validity
print("\nBlockchain valid?", blockchain.is_chain_valid())

# Print blockchain
print("\n----- BLOCKCHAIN DATA -----")
for block in blockchain.chain:
    print({
        "index": block.index,
        "transaction": block.transaction,
        "hash": block.hash,
        "previous_hash": block.previous_hash
    })