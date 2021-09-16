def decode(trame):

    payload = bytearray()

    if len(data) < 7:
        raise Exception("Trame trop petite")
    if hex(trame[0])!= '0x69':
        raise Exception("Protocol inconnu")
    if trame[1] == trame[2]:
        raise Exception("Source == DEST")
    parite = 0
    for i in range(trame[3]+trame[4]):
        payload.append(trame[i+5])
        parite+=trame[i+5]

    checksum = trame[-1]

    if not checksum and parite % 2 != 0:
        raise Exception("CheckSum incorrect", parite)
    elif checksum and parite % 2 == 0:
        raise Exception("CheckSum incorrect", parite)

    return payload

def encode(source: bytes, dest: bytes, data: bytes):

    trame = b'\x69'
    trame+= source
    trame+= dest
    if len(data)<16:
        trame+= b'\x00'
        trame+= bytes(len(data))
    else:
        trame+= bytes(len(data))
    parite = 0
    trame += data

    for i in range(len(data)):
        parite += data[i]
    
    trame+=bytes(parite % 2)

    return trame
    


data: bytes = b'\x69\x01\x02\x00\x02\x11\x22\x01'


trame = encode(b'\x01', b'\x02', b'\x11\x22\x33')
print(decode(trame))