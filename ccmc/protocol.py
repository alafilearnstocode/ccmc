
class StorageCommand:
    def __init__(self, command, key, flags, exptime, length, data):
        self.command = command
        self.key = key
        self.flags = flags
        self.exptime = exptime
        self.length = length
        self.data = data

    def serialize(self):
        header = f"{self.command} {self.key} {self.flags} {self.exptime} {self.length}\r\n"
        return header.encode() + self.data + b"\r\n"
    
def serialize_get(keys):
    return f"get {' '.join(keys)}\r\n".encode()

def parse_storage_response(response):
    return response.strip()

def parse_get_response(data):
    lines = data.decode().split("\r\n")
    result = {}
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("VALUE"):
            _, key, flags, length = line.split()
            flags, length = int(flags), int(length)
            value = lines[i + 1].encode()
            result[key] = (flags, value)
            i += 2
        elif line == "END":
            break
        else:
            i += 1
    return result