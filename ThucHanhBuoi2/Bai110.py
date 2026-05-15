def decode(cipher: str) -> str:
    result = []
    i = 0
    while i < len(cipher):
        if cipher[i] == '#':
            i += 1
            count = int(cipher[i])  
            i += 1
            char = cipher[i]
            result.append(char * count)
            i += 1
        else:
            result.append(cipher[i])
            i += 1
    return ''.join(result)


print(decode("XY#6Z1#4023"))  
print(decode("#39+1=1#30"))