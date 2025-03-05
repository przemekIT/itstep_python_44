text = 'hello'
byte_data = text.encode('utf-8')
print(byte_data)

decoded_text = byte_data.decode('utf-8')
print(decoded_text) 