import sys
import os
import unittest

# Ensure the parent directory is in the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from src.space import Space, Path, Waypoint
from src.space_system import SpaceSystem

class TestSpaceSystem(unittest.TestCase):
    def test_add_space(self):
        space_system = SpaceSystem()
        space = Space("space1", [10, 20], [5, 5], "r-space", "Main storage", ["storage"])
        space_system.add_space(space)
        self.assertIn("space1", space_system.spaces)

    def test_add_path(self):
        space_system = SpaceSystem()
        space1 = Space("space1", [10, 20], [5, 5], "r-space", "Main storage", ["storage"])
        space2 = Space("space2", [15, 25], [3, 3], "i-space", "Processing unit", ["processing"])
        waypoint1 = Waypoint([12, 22])
        waypoint2 = Waypoint([14, 24])
        path = Path("path1", space1.id, space2.id, [waypoint1, waypoint2], "linear", "Path from storage to processing", ["secure"], 100)
        space_system.add_path(path)
        self.assertIn("path1", space_system.paths)

    def test_json_serialization(self):
        space_system = SpaceSystem()
        space = Space("space1", [10, 20], [5, 5], "r-space", "Main storage", ["storage"])
        waypoint = Waypoint([12, 22])
        path = Path("path1", space.id, space.id, [waypoint], "linear", "Test path", ["secure"], 100)
        space_system.add_space(space)
        space_system.add_path(path)
        space_system.to_json("data/test_output.json")
        space_system.from_json("data/test_output.json")
        self.assertEqual(len(space_system.spaces), 1)
        self.assertEqual(len(space_system.paths), 1)

    def test_update_path_load(self):
        space_system = SpaceSystem()
        space1 = Space("space1", [10, 20], [5, 5], "r-space", "Main storage", ["storage"])
        waypoint = Waypoint([12, 22])
        path = Path("path1", space1.id, space1.id, [waypoint], "linear", "Test path", ["secure"], 100)
        space_system.add_space(space1)
        space_system.add_path(path)
        result = space_system.update_path_load("path1", 50)
        self.assertTrue(result)
        self.assertEqual(space_system.paths["path1"].current_load, 50)
        result = space_system.update_path_load("path1", 60)
        self.assertFalse(result)
        self.assertEqual(space_system.paths["path1"].current_load, 50)

if __name__ == '__main__':
    unittest.main()
