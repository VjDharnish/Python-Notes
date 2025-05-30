import os
with open('file8kb.txt', 'w') as f:
    for _ in range(8*1024):
        f.write('a\n')

print(os.path.getsize('file8kb.txt')/1024)