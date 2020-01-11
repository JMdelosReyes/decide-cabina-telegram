#Reference to code: https://github.com/RyanRiddle/elgamal=============

class PublicKey(object):
    def __init__(self, p=None, g=None, h=None, iNumBits=256):
        self.p = p
        self.g = g
        self.h = h
        self.iNumBits = iNumBits

def modexp( base, exp, modulus ):
        return pow(base, exp, modulus)

def encode(sPlaintext, iNumBits):
        byte_array = bytearray(sPlaintext, 'utf-16')
        
        z = []
        
        k = iNumBits//8
        j = -1 * k
        for i in range( len(byte_array) ):
                if i % k == 0:
                        j += k
                        z.append(0)
                z[j//k] += byte_array[i]*(2**(8*(i%k)))
        
        return z

def encrypt(key, sPlaintext):
        z = encode(sPlaintext, key.iNumBits)
        cipher_pairs = []
        for i in z:
                y = random.randint( 0, key.p )
                c = modexp( key.g, y, key.p )
                d = (i*modexp( key.h, y, key.p)) % key.p
                cipher_pairs.append( [c, d] )

        encryptedStr = ""
        for pair in cipher_pairs:
                encryptedStr += str(pair[0]) + ' ' + str(pair[1]) + ' '
    
        return encryptedStr

#==========================================================================================