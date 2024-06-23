import json
import os
import openai
from .space import Space, Path

class SpaceSystem:
    def __init__(self):
        self.spaces = {}
        self.paths = {}

    def add_space(self, space):
        self.spaces[space.id] = space

    def add_path(self, path):
        self.paths[path.id] = path

    def to_json(self, filename):
        data = {
            "spaces": [space.to_dict() for space in self.spaces.values()],
            "paths": [path.to_dict() for path in self.paths.values()]
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def from_json(self, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
            self.spaces = {s['id']: Space.from_dict(s) for s in data['spaces']}
            self.paths = {p['id']: Path.from_dict(p) for p in data['paths']}

    def update_path_load(self, path_id, load):
        if path_id in self.paths:
            path = self.paths[path_id]
            if path.can_handle_load(load):
                path.update_load(load)
                return True
        return False
    
    def interact_with_llm(self, prompt):
        client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        response = client.chat.completions.create(
            model="gpt-4o",
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": "You are managing a spatial operating system. return a JSON. Here is the current state:"},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000
        )
        print(response.choices[0].message.content)
        return response.choices[0].message.content
    
    def update_system_with_llm(self, prompt):
        response_text = self.interact_with_llm(prompt)
        
        try:
            updates = json.loads(response_text)
            
            if "spaces" in updates:
                for space_data in updates["spaces"]:
                    space = Space.from_dict(space_data)
                    self.add_space(space)
            
            if "paths" in updates:
                for path_data in updates["paths"]:
                    path = Path.from_dict(path_data)
                    self.add_path(path)
            
            return True
        except json.JSONDecodeError:
            print("Failed to decode LLM response.")
            return False
