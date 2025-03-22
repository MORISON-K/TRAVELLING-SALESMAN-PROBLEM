# TSP_dynamic_programming.py
import sys

def tsp_dynamic_programming(adjacency_matrix):
    """
    Solve the Traveling Salesman Problem using Dynamic Programming (Held-Karp algorithm).
    
    Parameters:
    adjacency_matrix: A 2D matrix where adjacency_matrix[i][j] represents the distance from city i to city j
    
    Returns:
    (min_distance, optimal_tour): A tuple containing the minimum distance and the optimal tour
    """
    n = len(adjacency_matrix)
    
    # Replace inf with a large number
    for i in range(n):
        for j in range(n):
            if adjacency_matrix[i][j] == float('inf'):
                adjacency_matrix[i][j] = sys.maxsize
    
    # Initialize memoization table
    # dp[mask][i] = minimum distance to visit all cities in mask and end at city i
    # mask is a bit mask where the jth bit is 1 if city j has been visited
    dp = {}
    
    # Function to solve the TSP using memoization
    def solve(mask, pos):
        # If all cities have been visited
        if mask == ((1 << n) - 1):
            return adjacency_matrix[pos][0], [0]
        
        # Check if this subproblem has already been solved
        if (mask, pos) in dp:
            return dp[(mask, pos)]
        
        min_dist = sys.maxsize
        next_city = -1
        best_path = []
        
        # Try to visit each unvisited city
        for city in range(n):
            if (mask & (1 << city)) == 0:  # if city is not visited
                # Distance to visit city
                new_mask = mask | (1 << city)
                distance, path = solve(new_mask, city)
                
                if adjacency_matrix[pos][city] != sys.maxsize:
                    curr_dist = adjacency_matrix[pos][city] + distance
                    if curr_dist < min_dist:
                        min_dist = curr_dist
                        next_city = city
                        best_path = [city] + path
        
        # Store the result
        dp[(mask, pos)] = (min_dist, best_path)
        return min_dist, best_path
    
    # Start from city 0 (index 0 represents city 1 in the problem)
    # Initial mask is 1 as we start from city 0
    min_distance, path = solve(1, 0)
    
    # Convert path indices to city numbers (1-indexed as in the problem)
    optimal_tour = [i + 1 for i in [0] + path]
    
    return min_distance, optimal_tour

def main():
    # Define the adjacency matrix
    inf = float('inf')
    adjacency_matrix = [
        [0, 12, 10, inf, inf, inf, 12],  # Node 1-start (index 0)
        [12, 0, 8, 12, inf, inf, inf],   # Node 2 (index 1)
        [10, 8, 0, 11, 3, inf, 9],       # Node 3 (index 2)
        [inf, 12, 11, 0, 11, 10, inf],   # Node 4 (index 3)
        [inf, inf, 3, 11, 0, 6, 7],      # Node 5 (index 4)
        [inf, inf, inf, 10, 6, 0, 9],    # Node 6 (index 5)
        [12, inf, 9, inf, 7, 9, 0]       # Node 7 (index 6)
    ]
    
    # Solve the TSP
    min_distance, optimal_tour = tsp_dynamic_programming(adjacency_matrix)
    
    # Print the results
    print("Optimal Tour using Dynamic Programming:", optimal_tour)
    print("Minimum Distance:", min_distance)
    
    # Verify the total distance
    total_distance = 0
    for i in range(len(optimal_tour) - 1):
        city1_idx = optimal_tour[i] - 1  # Convert to 0-indexed
        city2_idx = optimal_tour[i+1] - 1  # Convert to 0-indexed
        distance = adjacency_matrix[city1_idx][city2_idx]
        if distance == sys.maxsize:
            distance = float('inf')
        print(f"Distance from City {optimal_tour[i]} to City {optimal_tour[i+1]}: {distance}")
        total_distance += distance
    
    # Add the distance from the last city back to the starting city
    last_city_idx = optimal_tour[-1] - 1  # Convert to 0-indexed
    start_city_idx = optimal_tour[0] - 1  # Convert to 0-indexed
    last_distance = adjacency_matrix[last_city_idx][start_city_idx]
    if last_distance == sys.maxsize:
        last_distance = float('inf')
    print(f"Distance from City {optimal_tour[-1]} to City {optimal_tour[0]}: {last_distance}")
    total_distance += last_distance
    
    print("Total Distance (verification):", total_distance)

if __name__ == "__main__":
    main()