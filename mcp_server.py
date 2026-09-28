import sys
import json
from client import ConvexHullMonotoneChain

def handle_request(req):
    method = req.get("method")
    req_id = req.get("id")
    
    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-convex-hull-andrew-monotone-chain-skill", "version": "1.0.0"}
            }
        }
    elif method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "compute_convex_hull",
                        "description": "Compute 2D convex hull, area, and perimeter using Andrew's monotone chain",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "points": {"type": "array", "items": {"type": "array", "items": {"type": "number"}}, "description": "List of [x, y] coordinates"}
                            },
                            "required": ["points"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name")
        args = params.get("arguments", {})
        
        if tool_name == "compute_convex_hull":
            raw_pts = [tuple(p) for p in args.get("points", [])]
            hull = ConvexHullMonotoneChain.compute_hull(raw_pts)
            area = ConvexHullMonotoneChain.polygon_area(hull)
            perim = ConvexHullMonotoneChain.polygon_perimeter(hull)
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {
                    "content": [{
                        "type": "text",
                        "text": json.dumps({"hull": hull, "area": area, "perimeter": perim, "num_hull_vertices": len(hull)})
                    }]
                }
            }
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": str(e)}}
            sys.stdout.write(json.dumps(err) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
