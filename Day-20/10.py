import uuid

random_uuid = uuid.uuid4()
print("Random UUID:", random_uuid)
namespace = uuid.NAMESPACE_DNS
name = "example.com"
generated_uuid = uuid.uuid5(namespace, name)
print("UUID from Namespace and Name:", generated_uuid)
