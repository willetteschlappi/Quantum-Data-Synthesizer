
#### **generate.py**
```python
import csv
import json
import random

fields = ["id", "name", "age", "country"]
countries = ["USA", "UK", "Germany", "France", "Japan"]

data = [{"id": i, "name": f"User_{i}", "age": random.randint(18, 65), "country": random.choice(countries)} for i in range(100)]

with open("data.json", "w") as f:
    json.dump(data, f, indent=4)

with open("data.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)

print("Datasets generated successfully.")
