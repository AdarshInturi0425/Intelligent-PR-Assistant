import hashlib
import json
import os

class ReviewCache:
    def __init__(self, cache_file=".pr_cache.json"):
        self.cache_file = cache_file
        self.data = self._load()

    def _load(self):
        if os.path.exists(self.cache_file):
            with open(self.cache_file, 'r') as f:
                try: return json.load(f)
                except: return {}
        return {}

    def get_cached_review(self, code_snippet):
        content_hash = hashlib.sha256(code_snippet.encode()).hexdigest()
        return self.data.get(content_hash)

    def set_cached_review(self, code_snippet, review_text):
        content_hash = hashlib.sha256(code_snippet.encode()).hexdigest()
        self.data[content_hash] = review_text
        with open(self.cache_file, 'w') as f:
            json.dump(self.data, f, indent=4)