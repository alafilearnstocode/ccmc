import socket
from .protocol import StorageCommand, serialize_get, parse_storage_response, parse_get_response

class MemcachedClient:
    def __init__(self, host = "127.0.0.1", port = 11211):
        self.host = host
        self.port = port
        self.sock = None
    
    def connect(self):
        if self.sock is None:
            self.sock = socket.create_connection((self.host, self.port))
    
    def close(self):
        if self.sock:
            self.sock.close()
            self.sock = None
    
    def send(self, data):
        self.connect()
        self.sock.sendall(data)

    def recv_line(self):
        buffer = b""
        while not buffer.endswith(b"\r\n"):
            chunk = self.sock.recv(1)
            if not chunk:
                raise ConnectionError("Connection closed by the server")
            buffer += chunk
        return buffer.decode().strip()
    
    def recv_until_end(self):
        buffer = b""
        while b"END\r\n" not in buffer:
            chunk = self.sock.recv(4096)
            if not chunk:
                raise ConnectionError("Connection closed by the server")
            buffer += chunk
        return buffer
    
    def set(self, key, value, flags=0, exptime=0):
        value_bytes = value.encode()
        cmd = StorageCommand("set", key, flags, exptime, len(value_bytes), value_bytes)
        self.send(cmd.serialize())
        return parse_storage_response(self.recv_line())
    
    def get(self, key):
        self.send(serialize_get([key]))
        data = self.recv_until_end()
        return parse_get_response(data)
    
    def add(self, key, value, flags=0, exptime=0):
        value_bytes = value.encode()
        cmd = StorageCommand("add", key, flags, exptime, len(value_bytes), value_bytes)
        self.send(cmd.serialize())
        return parse_storage_response(self.recv_line())
    
    def replace(self, key, value, flags=0, exptime=0):
        value_bytes = value.encode()
        cmd = StorageCommand("replace", key, flags, exptime, len(value_bytes), value_bytes)
        self.send(cmd.serialize())
        return parse_storage_response(self.recv_line())

    def append(self, key, value, flags=0, exptime=0):
        value_bytes = value.encode()
        cmd = StorageCommand("append", key, flags, exptime, len(value_bytes), value_bytes)
        self.send(cmd.serialize())
        return parse_storage_response(self.recv_line())

    def prepend(self, key, value, flags=0, exptime=0):
        value_bytes = value.encode()
        cmd = StorageCommand("prepend", key, flags, exptime, len(value_bytes), value_bytes)
        self.send(cmd.serialize())
        return parse_storage_response(self.recv_line())
    