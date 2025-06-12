from collections import deque, defaultdict

class Solution:
    def numBusesToDestination(self, routes, source, target):
        if source == target:
            return 0

        # Build a map: bus_stop -> list of route indices that contain this stop
        stop_to_routes = defaultdict(list)
        for route_idx, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].append(route_idx)
        
        # BFS on routes
        queue = deque()
        visited_routes = set()

        # Start with all routes that contain the source
        for route_idx in stop_to_routes[source]:
            queue.append((route_idx, 1))  # (route_index, num_buses)
            visited_routes.add(route_idx)
            vistop = set()
        
        while queue:
            current_route, num_buses = queue.popleft()

            # Check if current route contains target
            if target in routes[current_route]:
                return num_buses

            # Explore all routes reachable from current route
            for stop in routes[current_route]:
                if not stop in vistop:
                    vistop.add(stop)
                    for next_route in stop_to_routes[stop]:
                        if next_route not in visited_routes:
                            visited_routes.add(next_route)
                            queue.append((next_route, num_buses + 1))

        return -1
