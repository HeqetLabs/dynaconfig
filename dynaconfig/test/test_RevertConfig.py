import unittest
from dynaconfig.endpoints import RevertConfig

class TestRevertConfig(unittest.TestCase):

  def setUp(self):
    self.revert = RevertConfig()

  def test_RevertEmptyResultsInEmpty(self):
    config = self.revert._revert_config({}, [], 0)
    self.assertEquals({}, config)

  def test_RevertAddToEmpty(self):
    config = self.revert._revert_config({"hello": "world"}, [{"created_at": 0, "version": 1, "changes": [{"key": "hello", "value": "world", "action": "added"}]}], 0)
    self.assertEquals({}, config)

  def test_RevertDeleteToSingleValue(self):
    config = self.revert._revert_config({}, [{"created_at": 0, "version": 1, "changes": [{"key": "hello", "value": "world", "action": "removed"}]}], 0)
    self.assertEquals({"hello": "world"}, config)

