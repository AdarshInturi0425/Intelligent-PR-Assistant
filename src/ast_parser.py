import ast

class PRAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.issues = []

    def analyze(self, source_code):
        """Parse Python code directly (no Git diff markers)."""
        try:
            tree = ast.parse(source_code)
            self.issues = []
            self.visit(tree)
            return self.issues
        except SyntaxError as e:
            return [{"type": "Syntax Error", "msg": f"{e.msg} at line {e.lineno}"}]

    def visit_FunctionDef(self, node):
        """Analyze nesting depth inside functions."""
        depth = 0
        for child in ast.walk(node):
            if isinstance(child, (ast.For, ast.While, ast.If)):
                depth += 1
        
        # Flag functions with 3 or more nested structures
        if depth >= 3:
            self.issues.append({
                "function": node.name,
                "line": node.lineno,
                "score": depth
            })
        self.generic_visit(node)