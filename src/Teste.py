import requests
import sys
import json
headers = {"Authorization":  'Bearer {0}'.format(sys.argv[1])}
print(headers)


def run_query(query):
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers)
    if request.status_code == 200:
        return json.loads(request.content.decode('utf-8'))
    else:
        return None


# The GraphQL query (with a few aditional bits included) itself defined as a multi-line string.
query = """
{
  viewer {
    login
  }
  rateLimit {
    limit
    cost
    remaining
    resetAt
  }
}
"""

result = run_query(query)  # Execute the query
print(result)