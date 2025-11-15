
</head>
<body>
  <div class="container">
    <h1>Mini Blockchain Project – Detailed Description</h1><p>
  This project is a simplified yet fully functional simulation of how a blockchain works at its core. It is designed for learning purposes, academic submissions, and anyone wanting to understand the internal mechanisms of blockchain technology without diving into complex real‑world implementations. Everything is built from scratch using clean and easy‑to‑understand Python code.
</p>

<div class="card">
  <h2>What This Project Demonstrates</h2>
  <p>
    The project showcases how a blockchain maintains secure, tamper‑proof data using cryptographic techniques. It includes the essential components that every blockchain—whether Bitcoin, Ethereum, or Hyperledger—uses at the fundamental level.
  </p>
  <ul>
    <li>How blocks store data and get linked together through hashes.</li>
    <li>How SHA‑256 hashing ensures integrity and immutability.</li>
    <li>How transactions are verified using digital signatures.</li>
    <li>How new blocks are added to the blockchain in sequence.</li>
  </ul>
</div>

<div class="card">
  <h2>What’s Inside the Project</h2>
  <p>This project is made of three major components:</p>
  <ol>
    <li>
      <strong>Block Class</strong> – Represents a single block containing:
      <ul>
        <li>Index (block number)</li>
        <li>Timestamp</li>
        <li>Transaction data</li>
        <li>Previous block’s hash</li>
        <li>Current block’s hash</li>
      </ul>
    </li>
    <li>
      <strong>Blockchain Class</strong> – Manages the entire chain by:
      <ul>
        <li>Creating the genesis (first) block</li>
        <li>Adding new blocks</li>
        <li>Verifying chain integrity</li>
      </ul>
    </li>
    <li>
      <strong>Digital Signature System</strong> – Ensures transactions are valid by:
      <ul>
        <li>Generating private and public keys for a user</li>
        <li>Signing a transaction using the private key</li>
        <li>Verifying the signature with the public key</li>
      </ul>
    </li>
  </ol>
  <p>
    Together, these components allow the blockchain to securely store transactions where each block is cryptographically tied to the previous one.
  </p>
</div>

<div class="card">
  <h2>How the System Works Internally</h2>
  <p>
    When a new transaction is created, the system signs it using the sender's private key. This ensures authenticity and prevents anyone else from forging the transaction. The transaction is then added to a new block, along with its metadata.
  </p>
  <p>
    The block is assigned a hash that is generated using the SHA‑256 hashing algorithm. This hash depends on the block's content, meaning even a tiny change will produce a completely different hash. Because each block stores the previous block’s hash, this creates a secure chain.
  </p>
  <p>
    If anyone tries to modify a block, its hash changes, making all following blocks invalid. This is what makes blockchain tamper‑proof.
  </p>
</div>

<div class="card">
  <h2>Purpose of This Project</h2>
  <p>
    The goal of this project is to give students and beginners a clear, practical understanding of blockchain fundamentals. It helps you learn:
  </p>
  <ul>
    <li>The internal functioning of blockchains</li>
    <li>Basics of cryptography (SHA‑256, digital signatures)</li>
    <li>Data security and integrity</li>
    <li>How linking blocks maintains tamper‑proof records</li>
  </ul>
</div>

<div class="card">

  </div>
</body>
</html>
