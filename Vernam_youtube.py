
def Vernam(Plain,key,Flag):
    result=""
    for i in range(len(Plain)):
        char=Plain[i]
        if(Flag):
            result += chr((ord(char)-97 + ord(key[i])-97)%26 +97)
        else:
            result += chr((ord(char) - ord(key[i]) + 26) % 26 + 97)



if __name__=="__main__":
    key=''.join(input('Enter key: ').lower().split())
    Plain=''.join(input("Enter Plain: ").lower().split())
    if len(key)!=len(Plain):
        print("Invalid key!")
        exit(None)
    CipherText=Vernam(Plain,key,True)
    print("CipherText: ",CipherText)
    print("Decripted Message: ",Vernam(CipherText,key,False))