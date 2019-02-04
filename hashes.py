import hashlib

# BUF_SIZE is totally arbitrary, change for your app!
BUF_SIZE = 1024  # lets read stuff in 64kb chunks!


dic = {'sha1':hashlib.sha1,
    'sha256':hashlib.sha256,
    'md5':hashlib.md5,
    'sha512':hashlib.sha512,
    'sha3_256':hashlib.sha3_256,
    'sha3_512':hashlib.sha3_512}

def calcFile(path, algorithm):
    alg = dic[algorithm]()
    with open(path, 'rb') as file:
        while True:
            data = file.read(BUF_SIZE)
            if not data:
                break
            alg.update(data)

    return alg.hexdigest()

def calcStr(algorithm, input):
    alg = dic[algorithm]()
    alg.update(input.encode())
    return alg.hexdigest()
