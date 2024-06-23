import sys
import os
from dotenv import load_dotenv
import openai

# Load environment variables from .env file
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
dotenv_path = os.path.join(parent_dir, '.env')
load_dotenv(dotenv_path)

# Retrieve the API key from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')

# Ensure the parent directory is in the Python path
sys.path.append(parent_dir)

from src.space import Space, Path, Waypoint
from src.space_system import SpaceSystem

# Create a SpaceSystem instance
space_system = SpaceSystem()

# Load existing data
json_path = os.path.join(parent_dir, 'data', 'example_spaces.json')
space_system.from_json(json_path)

# Define a prompt for the LLM
prompt = """
You are managing a spatial operating system. Here is the current state:
Spaces: [
    {"id": "storage1", "location": [5, 10], "size": [4, 4], "space_type": "r-space", "description": "Storage area for raw materials", "tags": ["storage", "raw_materials"]},
    {"id": "processing1", "location": [15, 20], "size": [6, 6], "space_type": "i-space", "description": "Processing unit for intermediate products", "tags": ["processing", "intermediate"]},
    {"id": "hub1", "location": [25, 30], "size": [3, 3], "space_type": "r-space", "description": "Communication hub for data transfer", "tags": ["communication", "data"]},
    {"id": "assembly1", "location": [35, 40], "size": [8, 8], "space_type": "r-space", "description": "Assembly line for final products", "tags": ["assembly", "final_products"]},
    {"id": "storage2", "location": [45, 50], "size": [5, 5], "space_type": "r-space", "description": "Secondary storage area", "tags": ["storage", "finished_goods"]}
]
Paths: [
    {"id": "path1", "start": "storage1", "end": "processing1", "waypoints": [{"location": [10, 15]}], "path_type": "linear", "description": "Path from raw materials storage to processing unit", "constraints": ["secure"], "capacity": 200},
    {"id": "path2", "start": "processing1", "end": "hub1", "waypoints": [{"location": [20, 25]}], "path_type": "linear", "description": "Path from processing unit to communication hub", "constraints": ["high_bandwidth"], "capacity": 150},
    {"id": "path3", "start": "hub1", "end": "assembly1", "waypoints": [{"location": [30, 35]}], "path_type": "linear", "description": "Path from communication hub to assembly line", "constraints": ["fast"], "capacity": 100},
    {"id": "path4", "start": "assembly1", "end": "storage2", "waypoints": [{"location": [40, 45]}], "path_type": "linear", "description": "Path from assembly line to secondary storage", "constraints": ["secure"], "capacity": 250}
]
Please provide updates to optimize the system.
"""

# Update the system using the LLM
if space_system.update_system_with_llm(prompt):
    print("System updated successfully with LLM.")
else:
    print("Failed to update system with LLM.")

# Save the updated system to JSON
updated_json_path = os.path.join(parent_dir, 'data', 'updated_spaces.json')
space_system.to_json(updated_json_path)
