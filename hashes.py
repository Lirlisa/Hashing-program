import hashlib
from sys import argv

BUF_SIZE = 1024*64


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

if __name__=="__main__":
    if len(argv) != 4:
        print("Syntax: hashes.py <-f | -t> <algorith> <path | text>")
        print("-f:\thash a file\n-t:\thash plain text")
        print("algorithms: sha1, sha256, md5, sha512, sha3_256, sha3_512")
        quit()
    if argv[1] == "-f":
        try:
            print("\n"+calcFile(argv[3], argv[2])+"\n")
        except FileNotFoundError:
            print("File not found")
    elif argv[1] == "-t":
        print("\n"+calcStr(argv[2], argv[3])+"\n")
    else:
        print("Syntax: hashes.py <-f | -t> <algorith> <path | text>")
        print("-f:\thash a file\n-t:\thash plain text")
        print("algorithms: sha1, sha256, md5, sha512, sha3_256, sha3_512")
        quit()
