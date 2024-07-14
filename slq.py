from tinydb import TinyDB, Query

# 示例字典数据
data = {"name": "Alice", "age": 30, "city": "New York"}

# 连接到TinyDB数据库（如果数据库不存在，则会自动创建）
db = TinyDB("db.json")

# 插入数据
db.insert(data)

# 连接到TinyDB数据库
db = TinyDB("db.json")

# 查询所有数据
all_data = db.all()
print("All data:", all_data)

# 查询特定条件的数据
User = Query()
results = db.search(User.name == "Alice")
print("Search results:", results)

# 查询单个文档
result = db.get(User.name == "Alice")
print("Single result:", result)
