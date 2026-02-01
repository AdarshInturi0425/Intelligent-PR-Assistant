import os

class AIEngine:
    """
    Orchestrates the communication with the LLM (OpenAI/Anthropic).
    """
    def __init__(self, api_key=None):
        # In a real setup, you'd put your key in a .env file
        self.api_key = api_key or os.getenv("OPENAI_API_KEY", "mock_key_for_demo")

    def generate_review(self, code_snippet, complexity_issues):
        """
        Constructs a prompt and returns a simulated or real AI review.
        """
        if not code_snippet:
            return "No code changes detected to review."

        prompt = f"""
        System: Act as a Senior Software Engineer.
        Task: Review the following code diff.
        
        Complexity Context from AST: {complexity_issues}
        
        Code Diff:
        {code_snippet}
        
        Provide a concise review focusing on performance and logic.
        """
        
        # For the GitHub demo, we return a structured mock response
        # to show how the system handles the data flow.
        return f"[AI Review]: The code looks solid. I noticed {len(complexity_issues)} high-complexity areas. Suggest refactoring nested loops to improve Big-O performance."