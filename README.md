# Mini Blockchain with Digital Signatures 

A simple Python-based blockchain built for educational purposes.
This project  include functions for creating new blocks, calculating SHA-256 hashes, and linking blocks. Include a feature that uses digital signatures to verify the authenticity of a transaction within a block.

---

# Features

- Create new blocks

- SHA-256 hashing

- Linking blocks to form a chain

- RSA digital signatures

- Signature verification before adding a block

- Check blockchain validity

- Beginner-friendly Python code



---

# Project Structure

mini-blockchain
<br>
├── block.py                # Block structure with hashing
<br>
├── blockchain.py           # Blockchain logic and validation
<br>
├── digital_signature.py    # RSA key generation and signature handling
<br>
├── main.py                 # Runs the blockchain demo
<br>
└── README.md               # Project documentation


---

# How It Works

# 1. Digital Signatures

- Every transaction is signed using a private key

- The blockchain verifies the signature using the matching public key

- If signature is invalid → ❌ block is rejected

- Ensures authenticity & security


# 2. Blocks

Each block contains:

- Index

- Previous block’s hash

- Transaction

- RSA signature

- Timestamp

- Current block hash

# 3. Blockchain

- Starts with a Genesis Block

- New blocks are added only when signature is valid

- Chain integrity is checked by recalculating hashes

---
# Example Output

✔ Block added successfully!

Blockchain valid? True

---
----- BLOCKCHAIN DATA ----- 
<br>
{'index': 0, 'transaction': 'Genesis Block', ...} 
<br>
{'index': 1, 'transaction': 'Alice pays Bob 10 coins', ...}

---
# Files Explained

# 1. block.py
- Defines the block structure and SHA-256 hashing.
  
# 2. blockchain.py :
Handles:
- creating genesis block
- verifying signatures
- adding new blocks
-validating the chain

# 3. digital_signature.py

Creates RSA keys:
- Sign transaction with private key
- Verify using public key

# 4. main.py
Runs the whole blockchain:

- Generates keys
- Creates transaction
- Signs it
- Adds block
- Displays entire chain
---

# Purpose of This Project

This project is designed for learning:

- Blockchain basics

- Hashing and linking

- Digital signatures

- Python implementation of secure transactions

---
