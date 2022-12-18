import re


def flatten(flows, neigh):
    res = {}
    for node, flow in flows.items():
        if flow == 0 and node != "AA":
            continue
        res[node] = []
        seen = set()
        seen.add(node)
        dist = 1
        frontier = set(neigh[node])
        while frontier:
            new_frontier = set()
            for n in frontier:
                if n in seen:
                    continue
                seen.add(n)
                if flows[n] != 0:
                    res[node].append((n, dist))
                new_frontier.update(neigh[n])
            dist += 1
            frontier = new_frontier
    return res


def open_flows(m, flows):
    def open_flow(remaining, node, visited, res):
        remaining -= 1
        if remaining <= 0:
            return res
        res += flows[node]*remaining
        res2 = res
        new_visited = visited.copy()
        new_visited.add(node)
        for neigh, dist in m[node]:
            if neigh not in visited and remaining - dist > 0:
                res2 = max(res2, open_flow(
                    remaining - dist, neigh, new_visited, res))
        return res2
    return open_flow(31, "AA", set(), 0)


flows = {}
neigh = {}

with (open("16", "r")) as f:
    for line in f.read().splitlines():
        node, rate, tunnels = re.search(
            r"Valve ([A-Z]{2}) has flow rate=(\d*); tunnels? leads? to valves? (\D*)", line).groups()
        tunnels = tunnels.split(', ')
        rate = int(rate)
        flows[node] = rate
        neigh[node] = tunnels
print(open_flows(flatten(flows, neigh), flows))
