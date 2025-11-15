
</head>
<body>
  <main class="container">
    <header>
      <div class="logo"></div>
      <div>
        <h1>Mini Blockchain Project <small style="font-size:14px;color:var(--muted);">(Unit II)</small></h1>
        <p class="lead">A simple, educational Python implementation demonstrating block creation, SHA-256 hashing, block linking, and RSA digital signatures.</p>
        <div class="badges">
          <span class="badge">Python 3</span>
          <span class="badge">Educational</span>
          <span class="badge">MIT License</span>
        </div>
      </div>
    </header>

    <section>
      <h2>Project Overview</h2>
      <p>This mini-blockchain simulation includes the core ideas needed to understand how blockchains work internally. It's beginner-friendly and ideal for coursework demos:</p>
      <ul>
        <li>Creating new blocks</li>
        <li>Calculating SHA-256 hashes</li>
        <li>Linking blocks using previous hashes</li>
        <li>Adding and signing transactions</li>
        <li>Verifying transaction authenticity</li>
      </ul>
    </section>

    <section>
      <h2>Features</h2>
      <ul>
        <li><strong>Block Creation</strong> — Each block contains an index, timestamp, transaction data, previous hash, current hash, and a digital signature.</li>
        <li><strong>SHA-256 Hashing</strong> — Uses Python's <code>hashlib</code> to compute cryptographic hashes.</li>
        <li><strong>Block Linking</strong> — Each block stores the previous block's hash to form a tamper-evident chain.</li>
        <li><strong>Digital Signatures</strong> — RSA is used to sign transactions with a private key and verify with the public key; invalid signatures are rejected.</li>
      </ul>
    </section>

    <section>
      <h2>Technologies Used</h2>
      <p class="pill">Python 3</p>
      <p class="pill">hashlib — SHA-256</p>
      <p class="pill">json — data formatting</p>
      <p class="pill">rsa — digital signatures</p>
    </section>

    <section>
      <h2>How to Run</h2>
      <p>Run the main script from the repository root:</p>
      <pre><code>python blockchain.py</code></pre>
      <p>Typical script behavior:</p>
      <ul>
        <li>Generate RSA key pairs</li>
        <li>Create example transactions</li>
        <li>Sign transactions and verify authenticity</li>
        <li>Add validated blocks to the blockchain</li>
        <li>Display block details on the console</li>
      </ul>
    </section>

    <section>
      <h2>Project Structure</h2>
      <div class="file-structure">
        <pre><code>├── blockchain.py         # Contains Block and Blockchain classes
├── digital_signature.py  # Handles RSA key generation, signing, verification
├── import_hashlib.py     # Utility file for hashing functions (SHA-256)
├── main.py               # Runs the blockchain simulation
├── README.md             # Project documentation
</code></pre>
      </div>
    </section>

    <section>
      <h2>Blockchain Validation</h2>
      <p>The chain is validated by verifying:</p>
      <ul>
        <li>Hash integrity of each block</li>
        <li>That each block's <code>previous_hash</code> matches the previous block's hash</li>
        <li>Digital signature validity for each transaction</li>
      </ul>
    </section>

    <section>
      <h2>Digital Signature Workflow</h2>
      <ol>
        <li>Sign a transaction with a private RSA key.</li>
        <li>Include the signature inside the block.</li>
        <li>Use the sender's public RSA key to verify the signature.</li>
        <li>If verification fails, the block will be rejected as invalid.</li>
      </ol>
    </section>

    <section>
      <h2>Contributing</h2>
      <p>Contributions are welcome — open an issue or submit a pull request.</p>
    </section>

    <section>
      <h2>License</h2>
      <p>Released under the <strong>MIT License</strong>.</p>
    </section>

    <footer>
      <p>Generated README — Mini Blockchain Project • Unit II</p>
    </footer>
  </main>
</body>
</html>
