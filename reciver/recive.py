from socket import socket

class Reciver:
    def update_last_bytes(last_bytes: bytes, data: bytes) -> tuple[bytes, bytes]:
        tag_length = len(last_bytes)

        if len(data) >= tag_length:
            return data[-tag_length:], data[:-tag_length]

        else:
            return (last_bytes + data)[-tag_length:], bytes()                    

    def recive_til_tag(client: socket, tag: bytes) -> bytes:
        last_bytes = bytes(len(tag))
        message_bytes = bytes()

        while last_bytes != tag:
            data = last_bytes + client.recv(1024) if not b'\x00' in last_bytes else client.recv(1024)
            last_bytes, data = Reciver.update_last_bytes(last_bytes, data)

            message_bytes += data

        return message_bytes
    
    def recive_file(self):
        pass



