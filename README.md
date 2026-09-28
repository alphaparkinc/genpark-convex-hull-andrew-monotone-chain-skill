# genpark-convex-hull-andrew-monotone-chain-skill

Agent Skill implementing **Andrew's Monotone Chain 2D Convex Hull Algorithm** ($O(n \log n)$) with cross product orientation tests, collinear handling, and polygon geometry calculations.

## Architectural Overview
```mermaid
flowchart TD
    Points["Raw 2D Point Set"] --> Sort["Lexicographical Sort (X then Y)"]
    Sort --> Lower["Build Lower Hull (CCW cross product > 0)"]
    Sort --> Upper["Build Upper Hull (CCW cross product > 0)"]
    Lower & Upper --> Merge["Concatenate Lower + Upper"]
    Merge --> Polygon["Convex Hull Polygon"]
    Polygon --> Metrics["Compute Shoelace Area & Euclidean Perimeter"]
```

## Features
- **100% Python Standard Library**: Zero dependencies.
- **Strict $O(n \log n)$ Complexity**: Optimal sorting step followed by linear scan.
- **MCP Integration**: Compatible with Claude Desktop, Cursor, and Windsurf via JSON-RPC 2.0 stdio.
