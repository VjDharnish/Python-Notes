binlogs = ['bin.log.1', 'bin.log.4', 'bin.log.5', 'bin.log.6' , 'bin.log.3', 'bin.log.7', 'bin.log.8','bin.log.2' 'bin.log.9', 'bin.log.10']

def extract_number(filename):
    return int(filename.split(".")[-1])

print(binlogs)
print("After sorting")
binlogs.sort(key=extract_number,reverse=True)
print(binlogs)
