from collections import defaultdict
import difflib

class TrieNode:
    def __init__(self):
        self.is_end_of_word = False
        self.children = defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, name):
        node = self.root
        for char in name.lower():
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, query):
        node = self.root
        for char in query.lower():
            if char not in node.children:
                return []
            node = node.children[char]
        return self._get_all_words_from_node(node, query)

    def _get_all_words_from_node(self, node, prefix):
        words = []
        if node.is_end_of_word:
            words.append(prefix)
        for child_char, child_node in node.children.items():
            words.extend(self._get_all_words_from_node(child_node, prefix + child_char))
        return words

def correct_spelling(query, words, max_suggestions=4):
    similar_matches = [word for word in words if query.lower() in word.lower()]
    similar_matches.sort(key=lambda x: (len(x), difflib.SequenceMatcher(None, query.lower(), x.lower()).ratio()), reverse=True)
    return similar_matches[:max_suggestions]
