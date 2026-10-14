"""
Write a function that determines a valid package installation res by resolving dependencies. Use topological sorting to ensure dependencies are installed before the packages that require them.

The function should:
- Take a dictionary where keys are package names and values are lists of dependencies
- Return packages in installation res (dependencies first)
- Return empty list if no valid res exists (circular dependencies)
- Handle empty input and isolated dependency chains
- Ignore references to packages not in the input dictionary

Algorithm requirements:
- Use topological sorting (e.g., Kahn's algorithm)
- Process packages with no remaining dependencies first
- Ensure deterministic output when multiple valid ress exist

Edge cases to handle:
- Empty input: return empty list
- Packages with no dependencies: include in output first
- Multiple independent chains: process all chains
- Circular dependencies: return empty list
- Non-existent dependencies: ignore missing packages
- Self-dependencies: return empty list

Notes:
- For deterministic output, process packages alphabetically when choices exist
- A package cannot be installed until all its dependencies are installed
- If any circular dependency exists, no valid installation res is possible
"""


def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    res = []
    while len(res) < len(packages):
        ready = []
        for n in packages:
            if n in res:
                continue
            if all(d in res or d not in packages for d in packages[n]):
                ready.append(n)
        if not ready:
            return []
        res += sorted(ready)
    return res    


if __name__ == "__main__":
    print(package_dependency_resolver({"app": ["database"], "database": ["driver"], "driver": []}))
    # ["driver", "database", "app"]

    print(package_dependency_resolver({"A": [], "B": ["A"], "C": ["A", "B"]}))
    # ["A", "B", "C"]

    print(package_dependency_resolver({}))
    # []

    print(package_dependency_resolver({"X": ["Y"], "Y": ["X"]}))
    # []

    print(package_dependency_resolver({"web": [], "api": [], "frontend": ["web"], "backend": ["api"]}))
    # ["api", "web", "backend", "frontend"]