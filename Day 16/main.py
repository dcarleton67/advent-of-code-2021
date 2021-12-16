with open('Day 16/input.txt') as f:
    hexdata = f.readline().strip()

def process_literal_packet(literal_packet):
    result = ''
    for i in range(0, len(literal_packet), 5):
        if literal_packet[i] == '1':
            result += literal_packet[i+1:i+5]
            continue
        else:
            result += literal_packet[i+1:i+5]
            break

    return int(result, 2), literal_packet[i+5:]

def reduce_sub_results(results, type_id):
    if type_id == 0:
        return sum(results)
    elif type_id == 1:
        product = 1
        for result in results:
            product *= result
        return product
    elif type_id == 2:
        return min(results)
    elif type_id == 3:
        return max(results)
    elif type_id == 5:
        return int(results[0] > results[1])
    elif type_id == 6:
        return int(results[0] < results[1])
    elif type_id == 7:
        return int(results[0] == results[1])

def process_operator_packet(operator_packet, type_id):
    length_type_id = operator_packet[0]
    version_num = 0
    sub_results = []
    if length_type_id == '0':
        sub_packet_bits = int(operator_packet[1:16], 2)
        remaining_sub_packet = operator_packet[16:]
        while(len(operator_packet[16:]) - len(remaining_sub_packet) != sub_packet_bits):
            sub_packet_version_num, sub_result, remaining_sub_packet = process_packet(remaining_sub_packet)
            version_num += sub_packet_version_num
            sub_results.append(sub_result)
    else:
        sub_packet_count = int(operator_packet[1:12], 2)
        remaining_sub_packet = operator_packet[12:]
        for i in range(sub_packet_count):
            sub_packet_version_num, sub_result, remaining_sub_packet = process_packet(remaining_sub_packet)
            version_num += sub_packet_version_num
            sub_results.append(sub_result)

    result = reduce_sub_results(sub_results, type_id)
    return version_num, result, remaining_sub_packet
        

packets_processed = 0
def process_packet(packet):
    version_num = int(packet[0:3], 2)
    type_id = int(packet[3:6], 2)

    if type_id == 4:
        result, unprocessed_remainder = process_literal_packet(packet[6:])
    else:
        operator_version_num, result, unprocessed_remainder = process_operator_packet(packet[6:], type_id)
        version_num += operator_version_num

    return version_num, result, unprocessed_remainder

packet = bin(int(hexdata, 16))[2:].zfill(len(hexdata) * 4)

print(process_packet(packet))
