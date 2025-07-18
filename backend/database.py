from model import Todo

# MogoDB driver
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
database = client.ToDoList
collection = database.todo


async def fetch_one_todo(title):
    document = await collection.find_one({"title":title})
    return document

async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos

async def create_todo(todo: dict) -> dict:
    result = await collection.insert_one(todo)
    new_todo = await collection.find_one({"_id":result.inserted_id})
    return {
        "id":str(new_todo["_id"]),
        "title":new_todo["title"],
        "description":new_todo["description"],
    }

async def update_todo(title, desc):
    await collection.update_one({"title":title},{"$set":{
        "description":desc}})
    document = await collection.find_one({"title":title})
    return document

async def remove_todo(title):
    await collection.delete_one({"title":title})
    return True