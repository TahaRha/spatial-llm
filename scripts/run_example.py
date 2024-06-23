import sys
import os

# Ensure the parent directory is in the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from src.space import Space, Path, Waypoint
from src.space_system import SpaceSystem

# Create a SpaceSystem instance
space_system = SpaceSystem()

# Load from JSON
space_system.from_json("data/example_spaces.json")

# Print loaded data
print("Loaded Spaces:")
for space_id, space in space_system.spaces.items():
    print(f"ID: {space_id}, Description: {space.description}, Type: {space.space_type}, Tags: {space.tags}")

print("\nLoaded Paths:")
for path_id, path in space_system.paths.items():
    print(f"ID: {path_id}, Description: {path.description}, Type: {path.path_type}, Capacity: {path.capacity}, Current Load: {path.current_load}")

# Example: Update path load
path_id = "path1"
load = 100
if space_system.update_path_load(path_id, load):
    print(f"\nUpdated load on path {path_id} by {load}. New load: {space_system.paths[path_id].current_load}")
else:
    print(f"\nFailed to update load on path {path_id}. Load exceeds capacity.")
