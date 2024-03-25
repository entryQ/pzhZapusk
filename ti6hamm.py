import heapq
from collections import defaultdict
class Hamming:
    def encode(self, data):
        data_length = len(data)
        for i in range(data_length):
            if 2 ** i >= data_length + i + 1:
                encoded_data = list(data.ljust(2 ** i, '-'))
                break

        for i in range(data_length):
            if encoded_data[i] == '-':
                parity = 0
                for j in range(i, len(encoded_data), 2 ** (i + 1)):
                    parity ^= int(encoded_data[j])
                encoded_data[i] = str(parity)

        return ''.join(encoded_data)

    def decode(self, encoded_data):
        decoded_data = ''
        parity_bits = []
        data_length = len(encoded_data)
        for i in range(data_length):
            if 2 ** i >= data_length + i + 1:
                for j in range(i, len(encoded_data), 2 ** (i + 1)):
                    parity = 0
                    for k in range(j, min(j + 2 ** i, data_length)):
                        parity ^= int(encoded_data[k])
                    if parity != 0:
                        parity_bits.append(j)
                break

        if not parity_bits:
            return encoded_data

        error_bit = sum(parity_bits)
        encoded_data = list(encoded_data)
        encoded_data[error_bit] = '1' if encoded_data[error_bit] == '0' else '0'
        return ''.join(encoded_data)
