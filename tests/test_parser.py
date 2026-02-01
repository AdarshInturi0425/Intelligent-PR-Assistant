import unittest
from src.ast_parser import PRAnalyzer

class TestPRAnalyzer(unittest.TestCase):
    def setUp(self):
        """Initialize the analyzer before each test."""
        self.analyzer = PRAnalyzer()

    def test_simple_function_passes(self):
        """Test that a basic function with low nesting has no issues."""
        code = "def hello_world():\n    print('Hello, World!')"
        issues = self.analyzer.analyze(code)
        self.assertEqual(len(issues), 0, "Simple code should not flag issues.")

    def test_nested_loops_flagged(self):
        """Test that deeply nested structures are correctly identified."""
        code = """
def complex_logic():
    if True:
        for i in range(10):
            if i % 2 == 0:
                for j in range(10):
                    print(i, j)
        """
        issues = self.analyzer.analyze(code)
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0]['function'], 'complex_logic')
        self.assertEqual(issues[0]['issue'], 'High Complexity Detected')
        self.assertEqual(issues[0]['score'], 4)

    def test_syntax_error_handling(self):
        """Test that the analyzer doesn't crash on invalid Python code."""
        invalid_code = "def broken_func(:"
        issues = self.analyzer.analyze(invalid_code)
        self.assertEqual(issues[0]['type'], 'Syntax Error')

if __name__ == '__main__':
    unittest.main()