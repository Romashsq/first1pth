
# UPDATED
import array
from collections import namedtuple

# Блок 1
text = "cOnNeCt:192.168.1.1:8080\n"
text = text.strip()
parts = text.split(":")
command = parts[0].lower()
ip = parts[1]
port = parts[2]
print(command, ip, port)
print(port.isdigit())

# Блок 2
ip_bytes = ip.encode("ascii")
print(ip_bytes)
# ip_bytes[0] = 50
# Ошибка TypeError: bytes нельзя изменять, это неизменяемый тип

# Блок 3
packet = bytearray(5)
packet[0] = 0xAA
packet[4] = 0xFF
packet.extend(ip_bytes)
print(len(packet))

# Блок 4
packet_queue = []
packet_queue.append(command)
packet_queue.append(ip_bytes)
packet_queue.append(packet)
packet_queue.insert(0, "PING")
processed_packet = packet_queue.pop()
print(packet_queue)
print(processed_packet)

# Блок 5
log_entry = (tuple(packet_queue), processed_packet)
print(log_entry)
# d = {log_entry: 1}
# Нельзя использовать как ключ словаря: внутри кортежа лежит bytearray,
# а он изменяемый, поэтому кортеж не хешируется (TypeError: unhashable type)

# Блок 6
ports = array.array("H", [80, 443, int(port)])
print(ports)
# ports.append("8080")
# Ошибка TypeError: массив с типом 'H' хранит только целые числа

# Блок 7
Session = namedtuple("Session", ["command", "ip", "port", "status"])
session = Session(command, ip, port, "Active")
print(session.ip)
print(session.status)