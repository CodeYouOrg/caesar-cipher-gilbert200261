
unencrypted_phrase = input("Enter the sentence? ")
encrypted_phrase = ""

for textchar in unencrypted_phrase:
    if 'a' <= textchar <= 'z':
        if ord(textchar) < 118:
            encrypted_phrase += str(chr(ord(textchar) + 5))
        else:
            encrypted_phrase += (chr(97 + 4 - (122 - ord(textchar))))
    elif 'A' <=  textchar <= 'Z':
        if ord(textchar) < 86:
            encrypted_phrase += str(chr(ord(textchar) + 5))
        else:
            encrypted_phrase += (chr(65 + 4 - (90-ord(textchar))))
    else:
        encrypted_phrase += textchar

print("The encrypted sentence is: " + encrypted_phrase)
