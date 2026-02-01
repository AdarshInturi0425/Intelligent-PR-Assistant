"""
Test file with intentionally complex code patterns.
This demonstrates what the Intelligent PR-Assistant catches.
"""

def process_user_data(users):
    """Bad example: Too many nested levels (4 levels deep)."""
    for user in users:
        if user['active']:
            for permission in user['permissions']:
                if permission['level'] > 2:
                    for resource in permission['resources']:
                        print(f"Processing {user['name']} -> {resource}")


def validate_config(config):
    """Another bad example: 3+ levels of nesting."""
    for section in config.sections():
        if section != 'metadata':
            for key, value in config.items(section):
                if value and isinstance(value, str):
                    print(f"Validated {section}.{key}")


def simple_function(x):
    """Good example: Low complexity, no nested loops."""
    return x * 2


def calculate_total(items):
    """Good example: Single loop with a simple condition."""
    total = 0
    for item in items:
        if item.get('valid'):
            total += item['price']
    return total
