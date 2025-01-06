import unittest
from app.main import get_recipe

class TestMain(unittest.TestCase):
    def test_get_recipe_fount(self):
        self.assertEquals(
            get_recipe("pancakes"),
            {
                "ingredients": ["flour", "milk", "eggs"],
                "steps": ["Mix ingredients", "Cook on a pan"]
            }
        )

        def test_get_recipe_not_found(self):
            self.assertEqual(get_recipe("nonexistent"), "Recipe not found")

if __name__ == '__main__':
    unittest.main()