## Charting the Top 30 "Most Forked" Github repositories.

import requests
import plotly.express as px

# Make the API call.
url = "https://api.github.com/search/repositories"
url += "?q=language:python+forks:>100&sort=forks&order=desc&per_page=30"

headers = {"Accept": "application/vnd.github.v3+json"}
response = requests.get(url, headers=headers)

# Create dictionary with response, or provide error code.
if response.status_code == 200:
    response_dict = response.json()
    repo_dicts = response_dict['items']
else:
    print(f"Failed to retrieve data: Status code {response.status_code}")

# Process repositories.
repo_names, forks, descriptions = [], [], []
for repo in repo_dicts:
    repo_names.append(repo['name'])
    forks.append(repo['forks_count'])
    descriptions.append(repo['description'])

# Visualize results.
title = "30 Most-Forked Github Repositories"
labels = {'x': 'Repositories', 'y': 'Forks'}
fig = px.bar(x=repo_names, y=forks, title=title, labels=labels, hover_name=descriptions)

fig.update_layout(title_font_size=20, xaxis_title_font_size=15, yaxis_title_font_size=15)

fig.show()
