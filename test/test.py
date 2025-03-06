with open("sklearn/tree/_classes.py", "r") as f:
    content = f.read()

assert "X_idx_sorted" not in content, "Test case failed: X_idx_sorted parameter still exists"

print("Test passed")