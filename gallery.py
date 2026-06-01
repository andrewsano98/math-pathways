# ~~~ Part 1: Get all names for a given category

import json
import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "mathematicians_final.json")

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

entries = [entry for entry in data]

entries.sort(key=lambda entry: entry.get("sort_year", 0))

for entry in entries:
    print(entry["name"], "-", entry.get("date"))



# ~~~ Part 2: Get number of names filtered by category

# import json
# import os

# script_dir = os.path.dirname(__file__)
# file_path = os.path.join(script_dir, "mathematicians_final.json")

# with open(file_path, "r", encoding="utf-8") as f:
#     data = json.load(f)

# category_counts = {}

# for entry in data:
#     category = entry.get("category", "uncategorized")
#     category_counts[category] = category_counts.get(category, 0) + 1

# for category, count in category_counts.items():
#     print(f"{category}: {count}")