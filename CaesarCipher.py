class CaesarCipher:
    def __init__(self, r):
        self.m_enc = ''.join([chr((i + r) % 26 + ord('A')) for i in range(26)])
        self.m_dec = ''.join([chr((i - r) % 26 + ord('A')) for i in range(26)])

    def encrypt(self, input_m):
        return self.transform(input_m, self.m_enc)

    def decrypt(self, secret):
        return self.transform(secret, self.m_dec)

    def transform(self, original, code):
        msg = list(original)
        for i in range(len(msg)):
            if msg[i].isupper():
                j = ord(msg[i]) - ord('A')
                msg[i] = code[j]
        return ''.join(msg)


cipher = CaesarCipher(3)
input_m = "THE EAGLE IS IN PLAY; MEET AT JOE'S"
coded = cipher.encrypt(input_m)
print("Secret: ", coded)
answer = cipher.decrypt(coded)
print("Message: ", answer)