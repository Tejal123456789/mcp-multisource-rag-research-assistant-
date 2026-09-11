import os

repo_path = "data/github_repos/graphrag"

for root, dirs, files in os.walk(repo_path):

    for file in files:

        if file.endswith(".md"):

            print(
                os.path.join(root, file)
            )