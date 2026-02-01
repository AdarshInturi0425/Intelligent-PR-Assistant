import sys
from src.git_client import GitClient
from src.ast_parser import PRAnalyzer
from src.cache_layer import ReviewCache
from src.ai_engine import AIEngine

def main():
    print("🚀 Starting Intelligent PR Assistant...")
    
    # 1. Initialize Components
    git = GitClient()
    analyzer = PRAnalyzer()
    cache = ReviewCache()
    ai = AIEngine()

    # 2. Get the code changes
    print("🔍 Fetching local git diff...")
    diff = git.get_unstaged_changes()
    
    if not diff:
        print("✅ No changes detected. Your code looks clean!")
        return

    # 3. Check Cache first (The 'Senior Engineer' move)
    cached_review = cache.get_cached_review(diff)
    if cached_review:
        print("📦 Found cached review. Skipping AI call...")
        print(f"\n--- Cached Review ---\n{cached_review}")
        return

    # 4. Perform Static Analysis (AST)
    print("📊 Performing AST Complexity Analysis...")
    issues = analyzer.analyze(diff)
    
    complexity_report = ""
    if issues:
        for issue in issues:
            complexity_report += f"- Function '{issue['function']}' at line {issue['line']}: {issue['issue']} (Score: {issue['score']})\n"
    else:
        complexity_report = "Low complexity detected."

    # 5. Get AI Review
    print("🤖 Requesting AI Review...")
    review = ai.generate_review(diff, complexity_report)
    
    # 6. Save to Cache and Print
    cache.set_cached_review(diff, review)
    print(f"\n--- Final Review ---\n{review}")

if __name__ == "__main__":
    main()
