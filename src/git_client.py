import subprocess

class GitClient:
    """
    Interfaces with the local git repository to extract code changes.
    """
    def get_unstaged_changes(self):
        """
        Captures work-in-progress changes that haven't been committed yet.
        """
        try:
            # Runs 'git diff' to see what changed in your files
            result = subprocess.run(
                ['git', 'diff'],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout
        except subprocess.CalledProcessError:
            return ""

    def get_diff_against_main(self):
        """
        Captures changes between current branch and main.
        """
        try:
            result = subprocess.run(
                ['git', 'diff', 'main'],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout
        except subprocess.CalledProcessError:
            return ""