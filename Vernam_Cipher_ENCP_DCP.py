import string
uppercase = list(string.ascii_uppercase)

def encryption() :
    plain_text = input('Enter the plain text : ').upper()
    key = input('Enter the key (length should be equal to the plain text  : ').upper()
    if len(plain_text)==len(key) :
        indexlist = [ ]
        index1list = [ ]
        cipher_text = ' '
        for eachletter in plain_text:
            if eachletter in uppercase:
                index = uppercase.index(eachletter)
                indexlist.append(index)
        for keyletter in key:
            if keyletter in uppercase:
                index1 = uppercase.index(keyletter)
                index1list.append(index1)
        for i in range(len(indexlist)):
            sum = indexlist[i] + index1list[i]
            if sum < 26:
                cipher_text += uppercase[sum]
            elif sum > 26:
                sum = sum - 26
                cipher_text += uppercase[sum]
        print('The encrypted message is : ',cipher_text)
    else :
        print('The length is not equal.')

def decryption() :
    cipher_text = input('Enter the cipher text (in uppercase) : ')
    key = input('Enter the key (length should be equal to the cipher text and in uppercase) : ')
    if len(cipher_text)==len(key) :
        indexlist = [ ]
        index1list = [ ]
        plain_text = ' '
        for eachletter in cipher_text:
            if eachletter in uppercase:
                index = uppercase.index(eachletter)
                indexlist.append(index)
        for keyletter in key:
            if keyletter in uppercase:
                index1 = uppercase.index(keyletter)
                index1list.append(index1)
        for i in range(len(indexlist)):
            sum = indexlist[i] - index1list[i]
            if sum < 0:
                sum = sum + 26
                plain_text += uppercase[sum]
            elif sum >= 0:
                plain_text += uppercase[sum]
        print('The decrypted message is : ',plain_text)
    else :
        print('The length is not equal.')

work = int(input('What do you want to do ? Choose 1 for encryption and 2 for decryption : '))
if work == 1 :
    encryption()
elif work == 2 :
    decryption()

