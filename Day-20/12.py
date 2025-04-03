import uuid

uuid1 = uuid.uuid4()
uuid2 = uuid.uuid4()

print(f"UUID 1: {uuid1}")
print(f"UUID 2: {uuid2}")
print("UUIDs are equal" if uuid1 == uuid2 else "UUIDs are not equal")
