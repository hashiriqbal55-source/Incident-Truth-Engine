from evidence.hashing import calculate_sha256

file_path = "evidence/sample_evidence.txt"

result = calculate_sha256(file_path)

print("Evidence File:", file_path)
print("SHA-256 Hash:", result)