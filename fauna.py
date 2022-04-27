from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient 

client = FaunaClient(secret="fnAElM4ffIACS6UHUPvW-xKUoJ49ld7fRGbzlfjR")

indexes = client.query(q.paginate(q.indexes()))

print(indexes)