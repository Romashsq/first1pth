# 1
def format_text(text):
    command, ip, port = text.strip().split(':')
    command = command.lower()
    
    if not port.isdigit():
        print('Has to contain digits only')
    return command, ip, port


def encode(ip):
    return ip.encode('ascii')
print(format_text('cOnNeCt:192.168.1.1:8080\n      '))
print(encode())


# 2 

# city = "Oslo"
# data = city.encode("ascii")
# print(data)            # b'Oslo'
# print(type(data))      # <class 'bytes'>
# print(data.decode("ascii"))   # Oslo

# name = 'Romansdfsdnfadsnfasd'
# data_name = name.encode('ascii')
# print(data_name[0])
# print(type(data_name))
# print(name, data_name)


def return_bytes(text): 
    bytes_list = []
    bytes_text = text.encode('utf-8')
    bytes_list.extend(list(bytes_text))
    str_list = str(bytes_list)
    print(str_list)
    print(bytes_list)
return_bytes('ROMARIO228')