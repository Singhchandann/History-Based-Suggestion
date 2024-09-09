import pymongo
import time
from trie import Trie

client = pymongo.MongoClient("mongodb://sidd:siddhesh123@128.140.104.241")
db = client["MLS"]
collection = db["audittrails"]

def update_trie():
    global last_updated, cached_topics
    trie = Trie()
    while True:
        query = {}
        if last_updated:
            query["updatedAt"] = {"$gt": last_updated}
        cursor = collection.find(query, {"query.topic": 1, "updatedAt": 1})
        new_topics = []
        for document in cursor:
            if "query" in document and "topic" in document["query"]:
                topic = document["query"]["topic"]
                if topic not in cached_topics:
                    cached_topics.add(topic)
                    new_topics.append(topic)
                    trie.insert(topic)
                last_updated = document["updatedAt"]
        time.sleep(5)

def get_suggestions(query):
    query_words = query.split()
    suggestions = []
    for word in query_words:
        word_suggestions = trie.search(word)
        if word_suggestions:
            suggestions.extend(word_suggestions)
    suggestions = list(set(suggestions))
    if not suggestions:
        suggestions = correct_spelling(query, cached_topics)
    return suggestions[:4]
