import meilisearch
client = meilisearch.Client('http://127.0.0.1:7700', 'sD0yrINzAJz0GszDWMHHY1srVqak3sHXLx4KvdVkKPI') 

def stock_search(query):
  return client.index('nasdaq').search(query)