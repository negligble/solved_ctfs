from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import requests
from secrets import randbelow
from hashlib import sha256
from base64 import b64encode, b64decode
from os import urandom

class encryptionHandler:
    def __init__(self):
        self.bits = 384
        self.g = None
        self.p = None
        self.a = None
        self.serverPublicKey = None
        self.clientPublicKey = None
        self.sessionKey = None
        
    def computeClientPublicKey(self):
        self.a = randbelow(self.p)
        self.clientPublicKey = pow(self.g, self.a, self.p)

    def computeSessionKey(self):
        key = pow(self.serverPublicKey, self.a, self.p)
        self.sessionKey = sha256(str(key).encode()).digest()

    def encrypt(self, data):
        iv = urandom(16)
        cipher = AES.new(self.sessionKey, AES.MODE_CBC, iv)
        encryptedPacket = iv + cipher.encrypt(pad(data.encode(), 16))
        return b64encode(encryptedPacket).decode()
    
    def decrypt(self, packet):
        decoded_packet = b64decode(packet.encode())
        iv = decoded_packet[:16]
        encrypted_packet = decoded_packet[16:]
        cipher = AES.new(self.sessionKey, AES.MODE_CBC, iv)
        try:
            decrypted_packet = unpad(cipher.decrypt(encrypted_packet), 16)
            packet_data = decrypted_packet
        except Exception as e:
            return f'Error: {e}'
        
        return packet_data
        
flagGetter = encryptionHandler()

port = 49200
ip = '94.237.59.119'
url = f'http://{ip}:{port}'

parameters = requests.post(url + '/api/request-session-parameters').json()

flagGetter.g = int(parameters['g'], 16)
flagGetter.p = int(parameters['p'], 16)

flagGetter.computeClientPublicKey()


publicKey = requests.post(url + '/api/init-session', json={'client_public_key': flagGetter.clientPublicKey}).json()

flagGetter.serverPublicKey = int(publicKey['server_public_key'], 16)
flagGetter.computeSessionKey()

encryptedChallenge = requests.post(url + '/api/request-challenge').json()['encrypted_challenge']

decryptedChallenge = flagGetter.decrypt(encryptedChallenge)

decryptedChallenge = sha256(decryptedChallenge).hexdigest()


encryptedRequest = flagGetter.encrypt('flag')

encryptedFlag = requests.post(url + '/api/dashboard', json={'challenge': decryptedChallenge, 'packet_data': encryptedRequest}).json()

encryptedFlag = encryptedFlag['packet_data']

flag = flagGetter.decrypt(encryptedFlag)
print(flag.decode())


