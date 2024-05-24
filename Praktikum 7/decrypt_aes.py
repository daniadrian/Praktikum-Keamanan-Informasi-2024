from hashlib import sha1  # Import library kriptografi sha1
from Crypto.Cipher import AES  # Import library kriptografi AES
import string  # Bantuan lib string untuk loop lowercase text

# Mengakses/membuka file yang terenkripsi
encryptedfile = open('Very Important Document.pdf.dokb', 'rb').read()

for i in string.ascii_lowercase:
    # Generate kunci dari tiap karakter a-z
    key = i * 16  # Pasti tiap karakter akan digandakan sebanyak 16 misal 'aaaaaaaaaaaaaaaa'
    key = sha1(key.encode()).digest()[:16]  # Mengambil 16 bytes pertama dari hasil SHA-1 digest bytes 0 sampai 15

    aes = AES.new(key, AES.MODE_ECB)  # Membuat AES cipher dari key yang didapat dari SHA-1 digest sebelumnya menggunakan mode ECB
    result = aes.decrypt(encryptedfile)  # Melakukan dekripsi file dengan algoritma kriptografi AES yang telah didefinisikan sebelumnya

    # Pastikan terdapat direktori result
    # Write file baru hasil proses dekripsi, seharusnya ada 26 file baru dan hanya ada 1 file yang dapat diakses.
    open(f'result/Very Important Document_Char_{i}.pdf', 'wb').write(result)
