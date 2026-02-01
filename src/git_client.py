import os

class GitClient:
    def get_unstaged_changes(self):
        """Read Python files directly from the workspace, avoiding Git diff formatting issues."""
        try:
            python_code = ""
            # Read all .py files in the current directory
            for filename in sorted(os.listdir('.')):
                if filename.endswith('.py') and not filename.startswith('.') and filename not in ['main.py']:
                    try:
                        with open(filename, 'r', encoding='utf-8') as f:
                            content = f.read()
                            if content.strip():
                                python_code += content + "\n"
                    except:
                        pass
            return python_code
        except Exception as e:
            return ""