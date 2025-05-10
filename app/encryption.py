import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def generate_key(salt = os.urandom(16), iterations = 3900000):

        password = b"password"
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=iterations,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        key_file = open('key.txt', 'a')
        key_file.write(key.decode('UTF-8'))
        key_file.close()


def encrypt_to_file(string, filename) -> None:
    """
    Encrypts a string and stores it in a txt file 
    """
    encrypt = Encryption()
    file = open('encryption/'+ filename+'.txt', 'a')
    encrypted_string = encrypt.encrypt(string)
    file.write(encrypted_string.decode('UTF-8'))
    file.close()

class Encryption:
    
    """
    Class for encrypting and decrypting strings
    """
    
    def __init__(self, salt = os.urandom(16), iterations = 3900000):
        
        """
        Constructor method for Encryption class
        """
        try:
             key_file = open('/run/secrets/key.txt', 'r')
        except:
            try:
                key_file = open('run/secrets/key.txt', 'r')
            except:
                try:
                    key_file = open('key.txt', 'r')
                except:
                    key_file = open('app/key.txt', 'r')
        key = (key_file.readlines())[0]

        self.key = bytes(key, 'UTF-8')
        self.fernet_instance = Fernet(self.key)

        
    def development(self):
        try:
            
            key_file = open('key.txt', 'r')
        except:
            raise ValueError("Finner ikke utviklingsnøkkel for utviklingsmiljø")
        key = (key_file.readlines())[0]

        self.key = bytes(key, 'UTF-8')
        self.fernet_instance = Fernet(self.key)


    def encrypt(self, string:str) -> str:
        """
        Encrypts an input string, and returns a bytes object
        """
        
        data = bytes(string, 'UTF-8')
        encrypted_string = self.fernet_instance.encrypt(data)
        return encrypted_string.decode('UTF-8')


    def decrypt(self,string:str) -> str:
        """
        Decrypts an input encrypted bytes object and returns it 
        as a string
        """

        bytes_object = bytes(string, 'UTF-8')
        if type(bytes_object) is not bytes:
            #print("> Decrypt: This is not a bytes object, rather a", type(bytes_object))
            return None
        decrypted_string = self.fernet_instance.decrypt(bytes_object)
        decoded_string = decrypted_string.decode('UTF-8') # Convert back from bytes  
        return decoded_string



if __name__ == "__main__":
    # Test of encryption class
    #generate_key()
    encrypt = Encryption()
    user_input = input("Input messsage: ")
    encrypted_message = encrypt.encrypt(user_input)
    print("Encrypted message:", encrypted_message)
    print("Decrypted message", encrypt.decrypt(encrypted_message))
