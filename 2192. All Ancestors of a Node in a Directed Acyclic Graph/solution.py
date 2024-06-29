class Solution:
    def getAncestors(self, n, edges):
        adjacency_list = [[] for _ in range(n)]

        indegree = [0 for _ in range(n)]
        for edge in edges:
            from_node = edge[0]
            to = edge[1]
            adjacency_list[from_node].append(to)
            indegree[to] += 1

        nodes_with_zero_indegree = [i for i in range(n) if indegree[i] == 0]

        topological_order = []
        while nodes_with_zero_indegree:
            current_node = nodes_with_zero_indegree.pop(0)
            topological_order.append(current_node)

            for neighbor in adjacency_list[current_node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    nodes_with_zero_indegree.append(neighbor)
        print(topological_order)
        print(adjacency_list)
        ancestors_list = [[] for _ in range(n)]
        ancestors_set_list = [set() for _ in range(n)]

        for node in topological_order:
            for neighbor in adjacency_list[node]:
                ancestors_set_list[neighbor].add(node)
                ancestors_set_list[neighbor].update(ancestors_set_list[node])

        for i in range(n):
            ancestors_list[i].extend(ancestors_set_list[i])
            ancestors_list[i].sort()

        return ancestors_list


sol = Solution()
print(
    sol.getAncestors(
        8, [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7],
            [4, 6]]
    )
)
