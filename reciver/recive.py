from socket import socket

def recive_til_tag(tag: str, client: socket) -> bytes:
    tag_bytes = bytes(len(tag))
    