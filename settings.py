__wifi_status__     = 0   #standard wifi status flag              1 > signals 0 > no signals   
__firmware_toggle__ = 0   #Standard firmware toggle flag          1 > f1.py   0 > f2.py 
__fimware_update__  = 0   # standard firmware update status flag  1 > new firmware  0 > no update

def encrypt(text, key):
    encrypted = ''
    for char in text:
        encrypted_char = chr(ord(char) ^ key)
        encrypted += encrypted_char
    return encrypted

def decrypt(ciphertext, key):
    decrypted = ''
    for char in ciphertext:
        decrypted_char = chr(ord(char) ^ key)
        decrypted += decrypted_char
    return decrypted

# Main program
#original_text = "Hi"
#encryption_key = 0xA5   

#encrypted_text = encrypt(original_text, encryption_key)
#rint("Encrypted:", encrypted_text)

###decrypted_text = decrypt(encrypted_text, encryption_key)
#print("Decrypted:", decrypted_text)
