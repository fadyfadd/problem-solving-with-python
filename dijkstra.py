from typing import List, Dict, Optional
import heapq

class PriorityItem:
    def __init__(self, item: str, weight: int):
        self.item = item
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

class DijkstraQueue:
    def __init__(self):
        self.heap = []

    def put(self, priority_item: PriorityItem):
        heapq.heappush(self.heap, priority_item)

    def contains(self) -> bool:
        return len(self.heap) > 0

    def get_priority_node(self) -> PriorityItem:
        return heapq.heappop(self.heap)

class Graph:
    def __init__(self):
        self.content: Dict[str, List[PriorityItem]] = {}

    def add_edge(self, from_node: str, to_node: str, weight: int):
        if from_node not in self.content:
            self.content[from_node] = []
        self.content[from_node].append(PriorityItem(to_node, weight))

    def get_content(self):
        return self.content

class Dijkstra:
    def __init__(self):
        self.path: List[str] = []
        self.shortest_distance: int = -1
        self.dijkstra_queue: Optional[DijkstraQueue] = None
        self.previous: Dict[str, Optional[str]] = {}
        self.distance: Dict[str, int] = {}

    def dijkstra_path(self, start: str, finish: str, graph: Graph):
        self.dijkstra_queue = DijkstraQueue()
        self.path = []
        self.previous = {}
        self.distance = {}

        for key in graph.get_content():
            if key == start:
                self.distance[key] = 0
                self.dijkstra_queue.put(PriorityItem(key, 0))
            else:
                self.distance[key] = float('inf')
                self.dijkstra_queue.put(PriorityItem(key, float('inf')))
            self.previous[key] = None

        while self.dijkstra_queue.contains():
            current_node = self.dijkstra_queue.get_priority_node()

            if current_node.item == finish:
                while self.previous[current_node.item] is not None:
                    self.path.append(current_node.item)
                    current_node.item = self.previous[current_node.item]
                break

            if current_node.weight != float('inf'):
                children = graph.get_content().get(current_node.item, [])
                for child_node in children:
                    new_weight = child_node.weight + self.distance[current_node.item]
                    current_weight = self.distance.get(child_node.item, float('inf'))

                    if new_weight < current_weight:
                        self.distance[child_node.item] = new_weight
                        self.previous[child_node.item] = current_node.item
                        self.dijkstra_queue.put(PriorityItem(child_node.item, new_weight))

        self.path.append(start)
        self.path.reverse()
        self.shortest_distance = self.distance.get(finish, -1)


g = Graph()
g.add_edge("A", "B", 1)
g.add_edge("B", "C", 2)
d = Dijkstra()
d.dijkstra_path("A", "C", g)
print(d.path, d.shortest_distance)
