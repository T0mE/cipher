import codecs

class Rot13:

    @staticmethod
    def cipher(text: str) -> str:
        return codecs.encode(text, 'rot_13')

    @staticmethod
    def encrypt(text: str) -> str:
        return Rot13.cipher(text)

    @staticmethod
    def decrypt(text: str) -> str:
        return Rot13.cipher(text)


class Rot47:

    @staticmethod
    def cipher(text: str) -> str:
        chars = []
        for c in text:
            if 33 <= ord(c) <= 126:
                chars.append(chr(33 + (ord(c) - 33 + 47) % 94))
            else:
                chars.append(c)
        return ''.join(chars)

    @staticmethod
    def encrypt(text: str) -> str:
        return Rot47.cipher(text)

    @staticmethod
    def decrypt(text: str) -> str:
        return Rot47.cipher(text)

# x = Rot13()
#
# a = x.encrypt("Ala ma Kota")
# print(a)
#
# s = Rot47.encrypt("Ala ma Kota")
#
# print(s)