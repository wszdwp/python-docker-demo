def decrypt(secret, offset):
    plain = ''
    for i in range(0, len(secret)):
        # print(ord(secret[i]))
        if ord(secret[i]) >= ord('A') and ord(secret[i]) <= ord('Z'):
            # print("ord(secret[i]) " + str(ord(secret[i])) + "+ 12 mod str(ord('A')) " + str(ord('A')) + " = " + str((ord(secret[i]) + offset) % 26 + ord('A')))
            plain += chr((ord(secret[i]) + offset) % 26 + ord('A'))
        else:
            plain += secret[i]
    return plain

def printUnicode():
    LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(0, len(LETTERS)):
        print(LETTERS[i] + ": " + str(ord(LETTERS[i])))        

if __name__ == '__main__':
    msgs = ['JG ZPV XBOU ZPVS DIJMESFO UP CF',
        'JOUFMMJHFOU SFBE UIFN GBJSZ UBMFT',
        'JG ZPV XBOU UIFN UP CF NPSF',
        'JOUFMMJHFOU SFBE UIFN NPSF GBJSZ UBMFT']
    for offset in range(12, 13):
        print("offset = " + str(offset))
        for msg in msgs:
            plain = decrypt(msg, offset)
            print(plain)
        print("\n")
        
    # printUnicode()