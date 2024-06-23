import os
import ast

def get_imports(file_path):
    with open(file_path, "r") as file:
        tree = ast.parse(file.read(), filename=file_path)
    imports = [node.names[0].name for node in ast.walk(tree) if isinstance(node, ast.Import)]
    imports.extend([node.module for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)])
    return imports

def get_requirements(directory):
    requirements = set()
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                imports = get_imports(file_path)
                requirements.update(imports)
    return requirements

directory_path = os.path.dirname(os.path.abspath(__file__))
requirements = get_requirements(directory_path)
requirements_path = os.path.join(directory_path, "requirements.txt")

with open(requirements_path, "w") as f:
    for requirement in sorted(requirements):
        f.write(f"{requirement}\n")

print(f"Requirements written to {requirements_path}")
