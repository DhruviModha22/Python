import sys
new_path = "/my/custom/modules"
sys.path.append(new_path)
print("Updated Python module search paths:")
print(sys.path)
