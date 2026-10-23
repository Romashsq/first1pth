import array
from collections import namedtuple

text = 'cOnNeCt:192.168.1.1:8080\n'


def dif_groups(text):
    # Блок 1. Строки
    text_list = text.strip().split(':')
    func, host, port = text_list
    func = func.lower()
    print(func, host, port)
    print(port.isdigit())

    # Блок 2. Байты
    host_bytes = host.encode('ascii')
    print(host_bytes)
    # host_bytes[0] = 50
    # TypeError: 'bytes' object does not support item assignment
    # bytes неизменяемый тип, его нельзя менять по индексу

    # Блок 3. bytearray
    bytearray_list = bytearray(5)
    bytearray_list[0] = 0xAA
    bytearray_list[-1] = 0xFF
    bytearray_list.extend(host_bytes)
    print(len(bytearray_list))

    # Блок 4. Список
    packet_queue = []
    packet_queue.append(func)
    packet_queue.append(host_bytes)
    packet_queue.append(bytearray_list)
    packet_queue.insert(0, 'PING')
    processed_packet = packet_queue.pop()
    print(packet_queue)
    print(processed_packet)

    # Блок 5. Кортеж
    log_entry = (tuple(packet_queue), processed_packet)
    print(log_entry)
    # archive = {log_entry: 'saved'}
    # TypeError: unhashable type: 'bytearray'
    # Нельзя использовать как ключ словаря. Ключ должен быть хешируемым,
    # то есть неизменяемым полностью. Сам кортеж неизменяемый, но внутри
    # лежит processed_packet, это bytearray, а он изменяемый.

    # Блок 6. array
    ports = array.array('H', [80, 443, int(port)])
    print(ports)
    # ports.append('8080')
    # TypeError: 'str' object cannot be interpreted as an integer
    # Массив с типом 'H' хранит только целые числа, строку не принимает

    # Блок 7. namedtuple
    Session = namedtuple('Session', ['command', 'ip', 'port', 'status'])
    session = Session(func, host, int(port), 'Active')
    print(session.ip)
    print(session.status)
    print(session.command)

    return {
        "func": func,
        "port": port,
        "host": host_bytes,
        "session": session
    }


print(dif_groups(text)['host'])