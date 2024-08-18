## Charting the Top 10 "Most Forked" Github repositories

import requests

# Make the API call
url = "https://api.github.com/search/repositories"
url += "?q=language:python+forks:>100&sort=forks&order=desc&per_page=10"

headers = {"Accept": "application/vnd.github.v3+json"}
response = requests.get(url, headers=headers)

# Create dictionary with response, or provide error code.
if response.status_code == 200:
    response_dict = response.json()
    repo_dicts = response_dict['items']
else:
    print(f"Failed to retrieve data: Status code {response.status_code}")

print("\nSelected information about each repository:")
# Loop over each result to gather necessary information
for repo_dict in repo_dicts:
    print(f"\nName: {repo_dict['name']}")
    print(f"Description: {repo_dict['description']}")
    print(f"Fork Count: {repo_dict['forks_count']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Repository: {repo_dict['html_url']}")