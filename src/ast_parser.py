import ast

class PRAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.issues = []

    def analyze(self, source_code):
        try:
            tree = ast.parse(source_code)
            self.visit(tree)
            return self.issues
        except SyntaxError as e:
            return [{"type": "Syntax Error", "msg": str(e)}]

    def visit_FunctionDef(self, node):
        # Calculate 'Cognitive Complexity' based on nesting
        depth = 0
        for child in ast.walk(node):
            if isinstance(child, (ast.For, ast.While, ast.If, ast.Try)):
                depth += 1
        
        if depth > 3:
            self.issues.append({
                "function": node.name,
                "line": node.lineno,
                "issue": "High Complexity Detected",
                "score": depth
            })
        self.generic_visit(node)