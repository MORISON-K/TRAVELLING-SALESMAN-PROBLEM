# TSP_som.py
import math
import random

class SimpleSOM:
    def __init__(self, adjacency_matrix):
        """Initialize a simplified Self-Organizing Map for TSP"""
        self.adjacency_matrix = adjacency_matrix
        self.num_cities = len(adjacency_matrix)
        
        # Create a simple 2D representation for cities
        self.cities = self._create_city_positions()
        
        # Neural ring: use 2x number of cities for better results
        self.num_neurons = 2 * self.num_cities
        self.neurons = self._init_neurons_circle()
        
        # Learning parameters
        self.learning_rate = 0.6
        self.neighborhood_size = 1.0
        
    def _create_city_positions(self):
        """Create simple 2D positions for cities in a circle"""
        positions = []
        for i in range(self.num_cities):
            angle = 2 * math.pi * i / self.num_cities
            x = 10 * math.cos(angle)
            y = 10 * math.sin(angle)
            positions.append((x, y))
        return positions
    
    def _init_neurons_circle(self):
        """Initialize neurons in a circle with larger radius than cities"""
        neurons = []
        for i in range(self.num_neurons):
            angle = 2 * math.pi * i / self.num_neurons
            x = 15 * math.cos(angle)  # Slightly larger radius than cities
            y = 15 * math.sin(angle)
            neurons.append((x, y))
        return neurons
    
    def _distance(self, p1, p2):
        """Euclidean distance between two points"""
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    
    def _find_winner(self, city_pos):
        """Find the neuron closest to the given city"""
        return min(range(self.num_neurons), 
                   key=lambda i: self._distance(city_pos, self.neurons[i]))
    
    def train(self, iterations=100):
        """Train the SOM for a fixed number of iterations"""
        for t in range(iterations):
            # Decay learning parameters
            decay_factor = 1.0 - t/iterations
            current_lr = self.learning_rate * decay_factor
            current_ns = self.neighborhood_size * decay_factor
            
            # For each city, update the winning neuron and its neighbors
            for city_idx in range(self.num_cities):
                # Select a random city for this iteration
                city_pos = self.cities[city_idx]
                
                # Find the winning neuron
                winner = self._find_winner(city_pos)
                
                # Update the winner and its neighbors
                for i in range(self.num_neurons):
                    # Calculate circular distance in the ring
                    dist = min(abs(i - winner), self.num_neurons - abs(i - winner))
                    
                    # Calculate influence (Gaussian neighborhood)
                    influence = math.exp(-(dist**2) / (2 * (current_ns**2)))
                    
                    # Skip negligible updates
                    if influence < 0.05:
                        continue
                    
                    # Update neuron position
                    for d in range(2):  # For both x and y coordinates
                        self.neurons[i] = (
                            self.neurons[i][0] + current_lr * influence * (city_pos[0] - self.neurons[i][0]),
                            self.neurons[i][1] + current_lr * influence * (city_pos[1] - self.neurons[i][1])
                        )
    
    def get_route(self):
        """Get the final route from the trained SOM"""
        # Map each city to its closest neuron
        city_neuron_map = {}
        for city_idx in range(self.num_cities):
            winner = self._find_winner(self.cities[city_idx])
            city_neuron_map[city_idx] = winner
        
        # Sort cities based on their mapped neurons' positions in the ring
        cities_sorted = sorted(range(self.num_cities), key=lambda city: city_neuron_map[city])
        
        # Ensure the route starts with city 0 (1 in the problem description)
        start_idx = cities_sorted.index(0)
        cities_sorted = cities_sorted[start_idx:] + cities_sorted[:start_idx]
        
        # Convert to 1-indexed (as per problem) and complete the tour by returning to start
        route = [i + 1 for i in cities_sorted]
        route.append(route[0])
        
        return route
    
    def calculate_distance(self, route):
        """Calculate the total distance of a given route"""
        total = 0
        # Convert to 0-indexed
        route_0_indexed = [city - 1 for city in route]
        
        for i in range(len(route_0_indexed) - 1):
            city1, city2 = route_0_indexed[i], route_0_indexed[i + 1]
            # Handle infinity
            if self.adjacency_matrix[city1][city2] == float('inf'):
                return float('inf')  # Route is invalid
            total += self.adjacency_matrix[city1][city2]
        
        return total

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
    
    # Set random seed for reproducibility
    random.seed(42)
    
    # Create and train the SOM
    som = SimpleSOM(adjacency_matrix)
    print("Training SOM...")
    som.train(iterations=200)
    
    # Get the route
    route = som.get_route()
    
    # Calculate distance
    distance = som.calculate_distance(route)
    
    # Print results
    print("Route found by SOM:", route)
    print("Total distance:", distance)
    
    # Print step-by-step distances
    print("\nStep-by-step distances:")
    for i in range(len(route) - 1):
        city1, city2 = route[i] - 1, route[i+1] - 1  # Convert to 0-indexed
        dist = adjacency_matrix[city1][city2]
        print(f"City {route[i]} to City {route[i+1]}: {'inf' if dist == inf else dist}")

if __name__ == "__main__":
    main()