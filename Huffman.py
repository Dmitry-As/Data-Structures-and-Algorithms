from collections import Counter


def count_freq(txt: str):
    freq = Counter(txt)
    return freq


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __str__(self):
        return f'({self.char}) *** ({self.freq})'

def build_huffman_tree(freq: dict):
    nodes = [Node(char, freq) for char, freq in freq.items()]
    print(*nodes, 'origin')
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.freq)
        print(*nodes, 'After sort')
        left = nodes.pop(0)
        right = nodes.pop(0)
        parent = Node(None, left.freq + right.freq)
        parent.left = left
        parent.right = right
        for i, node in enumerate(nodes):
            if parent.freq  > node.freq:
                continue
            else:
                nodes.insert(i, parent)
                break 
        else:
            nodes.append(parent)
    return nodes[0]


def gen_huffman_codes(root, code = '', codes = {}):
    if root is not None:
        if root.char is not None:
            codes[root.char] = code
        gen_huffman_codes(root.left, code + '0', codes)
        gen_huffman_codes(root.right, code + '1', codes)
    return codes


def huffman_encode(text, codes):
    encoded_text = ''
    for char in text:
        encoded_text += codes[char] + ' '
    return encoded_text


text = 'beep boop beer!'
# text = 'abracadabra'
freq = count_freq(text)
tree = build_huffman_tree(freq)
codes = gen_huffman_codes(tree)
encoded_text = huffman_encode(text, codes)

print(text)
print(codes)
print(encoded_text)