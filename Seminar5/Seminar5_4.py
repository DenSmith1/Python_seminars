# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def encode_text(textt: str):
    encoded_string = ""
    i = 0
    while (i < len(textt)-1):
        count = 1
        charr = textt[i]
        j = i
        while (j < len(textt)-1): 
            if (textt[j] == textt[j + 1]): 
                count += 1
                j += 1
            else: 
                break
        encoded_string += str(count) + charr
        i = j + 1
    return encoded_string

def decode_text(textt: str):
    decoded_text = ""
    i = 0
    j = 0
    while (i <= len(textt) - 1):
        char_count = int(textt[i])
        ischar = textt[i + 1]
        for j in range(char_count):
            decoded_text += ischar
            j += 1
        i += 2
    return decoded_text

my_text = 'AAAAddddddddggggfffffuuUUfffssggggerwerrr'
my_text2 = encode_text(my_text)
my_text3 = decode_text(my_text2)

print(my_text)
print(my_text2)
print(my_text3)