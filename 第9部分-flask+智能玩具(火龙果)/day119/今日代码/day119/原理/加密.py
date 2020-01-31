import struct
msg_bytes = "hello".encode("utf8")
token = b"\x81"
length = len(msg_bytes)

if length < 126:
    token += struct.pack("B", length)
elif length == 126:
    token += struct.pack("!BH", 126, length)
else:
    token += struct.pack("!BQ", 127, length)

msg = token + msg_bytes

print(msg)
