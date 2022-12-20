import re


def flatten(flows, neigh):
    res = {}
    for node, flow in flows.items():
        if flow == 0 and node != "AA":
            continue
        res[node] = []
        seen = {node}
        dist = 1
        frontier = set(neigh[node])
        while frontier:
            new_frontier = set()
            for n in frontier.difference(seen):
                seen.add(n)
                if flows[n] != 0:
                    res[node].append((n, dist))
                new_frontier.update(neigh[n])
            dist += 1
            frontier = new_frontier
    for key in res:
        res[key] = [(n, d+1) for (n, d) in res[key]]
    return res


def open_flows(m, flows, start_timer, with_elephant, memo, node_map):
    def open_flow(remaining, node, visited, res, has_reset):
        if has_reset:
            if (remaining, node, visited) in memo:
                return res + memo[remaining, node, visited]
        res += flows[node]*remaining
        res2 = res
        new_visited = visited + node_map[node]
        for neigh, dist in m[node]:
            if not node_map[neigh] & visited:
                if remaining - dist > 0:
                    res2 = max(res2, open_flow(
                        remaining - dist, neigh, new_visited, res, has_reset))
                if not has_reset:
                    res2 = max(res2, open_flow(
                        start_timer, "AA", new_visited, res, True))
        if has_reset:
            memo[remaining, node, visited] = res2 - res
        return res2
    return open_flow(start_timer, "AA", 0, 0, not with_elephant)


flows, neigh = {}, {}
with (open("16", "r")) as f:
    for line in f.read().splitlines():
        node, rate, tunnels = re.search(
            r"Valve ([A-Z]{2}) has flow rate=(\d*); tunnels? leads? to valves? (\D*)", line).groups()
        flows[node] = int(rate)
        neigh[node] = tunnels.split(', ')
memo = {}
flattened = flatten(flows, neigh)
node_map = {node: 1 << i if node !=
            "AA" else 0 for i, node in enumerate(flattened)}
print(open_flows(flattened, flows, 30, False, memo, node_map))
print(open_flows(flattened, flows, 26, True, memo, node_map))
