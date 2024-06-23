class Space:
    def __init__(self, id, location, size, space_type, description, tags):
        self.id = id
        self.location = location
        self.size = size
        self.space_type = space_type
        self.description = description
        self.tags = tags

    def to_dict(self):
        return {
            "id": self.id,
            "location": self.location,
            "size": self.size,
            "space_type": self.space_type,
            "description": self.description,
            "tags": self.tags
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            location=data["location"],
            size=data["size"],
            space_type=data["space_type"],
            description=data["description"],
            tags=data["tags"]
        )
    
class Waypoint:
    def __init__(self, location):
        self.location = location

    def to_dict(self):
        return {
            "location": self.location
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data["location"])


class Path:
    def __init__(self, id, start, end, waypoints, path_type, description, constraints, capacity):
        self.id = id
        self.start = start
        self.end = end
        self.waypoints = waypoints
        self.path_type = path_type
        self.description = description
        self.constraints = constraints
        self.capacity = capacity
        self.current_load = 0
        self.load_history = []


    def to_dict(self):
        return {
            "id": self.id,
            "start": self.start,
            "end": self.end,
            "waypoints": [wp.to_dict() for wp in self.waypoints],
            "path_type": self.path_type,
            "description": self.description,
            "constraints": self.constraints,
            "capacity": self.capacity,
            "current_load": self.current_load,
            "load_history": self.load_history
        }
    
    @classmethod
    def from_dict(cls, data):
        path = cls(
            id=data["id"],
            start=data["start"],
            end=data["end"],
            waypoints=[Waypoint.from_dict(wp) for wp in data["waypoints"]],
            path_type=data["path_type"],
            description=data["description"],
            constraints=data["constraints"],
            capacity=data["capacity"]
        )
        path.current_load = data.get("current_load", 0)
        path.load_history = data.get("load_history", [])
        return path
    
    def update_load(self, load):
        self.current_load += load
        self.load_history.append((self.current_load, load))

    def can_handle_load(self, load):
        return self.current_load + load <= self.capacity