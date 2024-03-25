import heapq
from collections import defaultdict

class Huffman:
    def encode(self, data):
        frequency = defaultdict(int)
        for symbol in data:
            frequency[symbol] += 1

        priority_queue = [[weight, [symbol, ""]] for symbol, weight in frequency.items()]
        heapq.heapify(priority_queue)

        while len(priority_queue) > 1:
            lo = heapq.heappop(priority_queue)
            hi = heapq.heappop(priority_queue)
            for pair in lo[1:]:
                pair[1] = '0' + pair[1]
            for pair in hi[1:]:
                pair[1] = '1' + pair[1]
            heapq.heappush(priority_queue, [lo[0] + hi[0]] + lo[1:] + hi[1:])

        huffman_codes = priority_queue[0][1:]
        huffman_encoded_data = ''.join([code for symbol, code in huffman_codes for char in data if char == symbol])

        return huffman_encoded_data

    def decode(self, encoded_data, huffman_codes):
        decoded_data = ""
        current_code = ""
        for bit in encoded_data:
            current_code += bit
            for symbol, code in huffman_codes.items():
                if code == current_code:
                    decoded_data += symbol
                    current_code = ""
                    break
        return decoded_data
