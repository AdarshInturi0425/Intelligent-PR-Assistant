# Intelligent PR-Assistant CLI 🚀

A high-performance CLI tool that automates the first pass of code reviews. It uses a hybrid approach—combining **Static Analysis (AST)** with **LLMs**—to identify logic flaws and complexity bottlenecks before a human reviewer ever sees the code.

## 🏗 System Architecture
The tool follows a modular pipeline to ensure efficiency and cost-control:
1. **Git Integration:** Extracts local diffs using `subprocess` and the Git CLI.
2. **Static Analysis (AST):** Parses code into an Abstract Syntax Tree to calculate cognitive complexity.
3. **Caching Layer:** Uses a content-addressable storage (SHA-256) to skip redundant AI calls.
4. **AI Orchestration:** Context-aware prompting to provide senior-level code feedback.



## ⚖️ Engineering Trade-offs

### Static Analysis vs. Pure AI
- **Decision:** I implemented an AST parser to pre-screen code for complexity.
- **Trade-off:** While sending the entire file to an LLM is easier to code, it is expensive and slow. By pre-screening for "high-complexity" functions, the tool only sends critical code to the AI, reducing token usage by approximately 60% on large files.

### Hashing for Cache Consistency
- **Decision:** Used SHA-256 hashing for the caching mechanism.
- **Trade-off:** This ensures that even if a function is moved to a different line, the cache remains valid as long as the logic (the content) is identical. This provides a massive latency win (O(1) lookup) for repetitive development cycles.

## 🛠 Tech Stack
- **Language:** Python 3.x
- **Libraries:** `ast` (Standard Library), `hashlib`, `subprocess`
- **AI:** OpenAI GPT-4o (Interface-ready)