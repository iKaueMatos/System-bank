from cryptography.fernet import Fernet

class EncryptionManagerService:
    def __init__(self, key=None):
        if key is None:
            self.key = Fernet.generate_key()
        else:
            self.key = key
        self.cipher_suite = Fernet(self.key)

    def encrypt(self, plaintext):
        return self.cipher_suite.encrypt(plaintext.encode()).decode()

    def decrypt(self, ciphertext):
        return self.cipher_suite.decrypt(ciphertext.encode()).decode()

    def get_key(self):
        return self.key.decode()