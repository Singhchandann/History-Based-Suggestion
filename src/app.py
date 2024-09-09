import gradio as gr
from trie import Trie
from db import update_trie, get_suggestions
import threading

trie = Trie()
cached_topics = set()
last_updated = None

# Start background thread to update the Trie from MongoDB
threading.Thread(target=update_trie, daemon=True).start()

# Gradio interface
def autocomplete(query):
    suggestions = get_suggestions(query)
    return "\n".join(suggestions)

iface = gr.Interface(fn=autocomplete, inputs="text", outputs="text", title="Autocomplete Suggestions")
iface.launch()
