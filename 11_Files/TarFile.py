import io
import sys
import tarfile

sInp = sys.stdin.read()
sInput = bytearray.fromhex(sInp)
tFile = tarfile.open(fileobj = io.BytesIO(sInput))
iSize = 0
iCount = 0

for cur in tFile.getmembers():
    if not cur.isdir():
        iSize += cur.size
        iCount += 1
print(iSize, iCount)


