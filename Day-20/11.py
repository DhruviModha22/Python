import uuid

students = {f"Student_{i}": str(uuid.uuid4()) for i in range(1, 6)}
for student, uid in students.items():
    print(f"{student}: {uid}")
