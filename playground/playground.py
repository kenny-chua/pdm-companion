import marvin
from pydantic import BaseModel

class Location(BaseModel):
    city: str
    country: str

text = 'I live in New York, but I am visiting London next week.'

print(marvin.extract(text, Location))
# [Location(city="New York", country="US"), Location(city="London", country="UK")]

print(marvin.extract(text, Location, instructions='all locations in the United States'))
# [Location(city="New York", country="US")]