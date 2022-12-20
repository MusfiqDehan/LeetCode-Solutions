from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms):
        # Create a queue to store the rooms that need to be visited
        queue = deque([0])

        # Create a set to store the rooms that have been visited
        visited = set()

        # While there are rooms in the queue
        while queue:
            # Get the next room to visit
            room = queue.popleft()

            # If the room has not been visited
            if room not in visited:
                # Mark the room as visited
                visited.add(room)

                # Add the keys for the room to the queue
                queue.extend(rooms[room])

        # Return whether all rooms have been visited
        return len(visited) == len(rooms)