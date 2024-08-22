from socket import socket
from typing import Callable
from locale import getdefaultlocale

class Reciver:
    def __init__(self, client: socket) -> None:
        self.client = client

    def update_last_bytes(last_bytes: bytes, data: bytes) -> tuple[bytes, bytes]:
        tag_length = len(last_bytes)

        if len(data) >= tag_length:
            return data[-tag_length:], data[:-tag_length]

        else:
            return (last_bytes + data)[-tag_length:], bytes()                    

    def recive_and_write_til_tag(self, tag: bytes, file_name: str) -> None:
        last_bytes = bytes(len(tag))

        with open(f"reciver/recived_files/{file_name}", 'wb+') as file:
            while last_bytes != tag:
                data = last_bytes + self.client.recv(1024) if not b'\x00' in last_bytes else self.client.recv(1024)
                last_bytes, data = Reciver.update_last_bytes(last_bytes, data)

                file.write(data)

    def recive_til_tag(self, tag: bytes) -> bytes:
        last_bytes = bytes(len(tag))
        message_bytes = bytes()

        while last_bytes != tag:
            data = last_bytes + self.client.recv(1024) if not b'\x00' in last_bytes else self.client.recv(1024)
            last_bytes, data = Reciver.update_last_bytes(last_bytes, data)

            message_bytes += data

        return message_bytes
    
    def recive_file(self):
        pass



