import rsa


def generate_keys():
    """Generate a pair of RSA keys."""
    return rsa.newkeys(512)  # (public_key, private_key)


def sign_transaction(private_key, transaction):
    """Sign a transaction using private key."""
    return rsa.sign(transaction.encode(), private_key, 'SHA-256')


def verify_signature(public_key, transaction, signature):
    """Verify signature of a transaction."""
    try:
        rsa.verify(transaction.encode(), signature, public_key)
        return True
    except:
        return False