import sys
from src.git_client import GitClient
from src.ast_parser import PRAnalyzer
from src.cache_layer import ReviewCache
from src.ai_engine import AIEngine

def main():
    print("🚀 Initializing Intelligent PR Assistant...")
    
    git = GitClient()
    analyzer = PRAnalyzer()
    cache = ReviewCache()
    ai = AIEngine()

    # 1. Get changes from Git
    diff = git.get_unstaged_changes()
    if not diff:
        print("✅ No unstaged changes found. Try editing a file!")
        return

    # 2. Check Cache
    cached_review = cache.get_cached_review(diff)
    if cached_review:
        print("📦 Found cached review for these changes:")
        print(cached_review)
        return

    # 3. Static Analysis
    issues = analyzer.analyze(diff)
    
    # 4. AI Review
    review = ai.generate_review(diff, issues)
    
    # 5. Store in Cache
    cache.set_cached_review(diff, review)
    
    print("\n--- 🤖 AI CODE REVIEW ---")
    print(review)
    if issues:
        print("\n--- 📊 COMPLEXITY ALERTS ---")
        for issue in issues:
            print(f"⚠️ Function '{issue['function']}' at line {issue['line']}: Score {issue['score']}")

if __name__ == "__main__":
    main()