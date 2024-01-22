#Łukasz Kwaśniowski - LAB02, Ćw 1

import base64

def encrypt_base64(text):
    # Zmiana tekstu na bajty (base64)
    text_encode = text.encode('utf-8')
    
    # Szyfrowanie
    text_encrypted = base64.b64encode(text_encode).decode('utf-8')
    
    return text_encrypted

def deszyfruj_base64(text_encrypted):

    # Dekodowanie do bajtów
    text_decode = base64.b64decode(text_encrypted.encode('utf-8'))
    
    # Zmiana bajtów na tekst (base64)
    text_decrypted = text_decode.decode('utf-8')
    
    return text_decrypted

def main():

    # Tekst do zaszyfrowania
    main_text = "Hello, World!"

    # Zakodowanie tekstu
    encrypted_text = encrypt_base64(main_text)
    print("Zaszyfrowany tekst:", encrypted_text)

    # Dekodowanie tekstu
    decrypted_text = deszyfruj_base64(encrypted_text)
    print("Odszyfrowany tekst:", decrypted_text)

main()
