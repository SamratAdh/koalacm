from OpenSSL import crypto
import datetime

def generate_certificate(common_name, organization, valid_days, passphrase, bits, digest_algorithm):
    # Generate a new RSA key pair
    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA, int(bits))

    # Generate Certificate Signing Request (CSR)
    req = crypto.X509Req()
    subj = req.get_subject()
    subj.commonName = common_name
    subj.organizationName = organization

    req.set_pubkey(key)
    req.sign(key, digest_algorithm)
    
    # Dump CSR to PEM format
    csr = crypto.dump_certificate_request(crypto.FILETYPE_PEM, req).decode('utf-8')

    # Generate X.509 certificate
    cert = crypto.X509()
    cert.set_subject(subj)
    cert.set_pubkey(key)
    cert.gmtime_adj_notBefore(0)
    cert.gmtime_adj_notAfter(int(valid_days) * 24 * 60 * 60)
    cert.set_issuer(subj)
    cert.sign(key, digest_algorithm)

    # Dump X.509 certificate to PEM format
    x509_cert = crypto.dump_certificate(crypto.FILETYPE_PEM, cert).decode('utf-8')

    # Encrypt private key if passphrase is provided
    if passphrase:
        encrypted_key = crypto.dump_privatekey(crypto.FILETYPE_PEM, key, 'aes256', passphrase.encode()).decode('utf-8')
    else:
        encrypted_key = crypto.dump_privatekey(crypto.FILETYPE_PEM, key).decode('utf-8')

    return encrypted_key, x509_cert, csr

def validate_user(username, password):
    # Implement user validation logic
    # For simplicity, hardcoding a single user named koala
    return username == 'koala' and password == 'test'
