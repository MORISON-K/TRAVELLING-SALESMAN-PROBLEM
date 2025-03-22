# Traveling Salesman Problem (TSP) Implementation

## Overview

This repository contains implementations of the Traveling Salesman Problem (TSP) using both classical and neural network approaches. The project was created as part of the CSC 1204: Data Structures and Algorithms practical assignment at Makerere University.

The implementations solve a 7-city TSP problem using:
1. **Dynamic Programming** (Held-Karp algorithm) - an exact method
2. **Self-Organizing Map (SOM)** - a neural network-based heuristic approach

## Problem Description

The Traveling Salesman Problem requires finding the shortest possible route that visits each city exactly once and returns to the starting city. Our implementation uses the following graph with 7 cities:

```
City 1 (start) connected to: City 2 (12), City 3 (10), City 7 (12)
City 2 connected to: City 1 (12), City 3 (8), City 4 (12)
City 3 connected to: City 1 (10), City 2 (8), City 4 (11), City 5 (3), City 7 (9)
City 4 connected to: City 2 (12), City 3 (11), City 5 (11), City 6 (10)
City 5 connected to: City 3 (3), City 4 (11), City 6 (6), City 7 (7)
City 6 connected to: City 4 (10), City 5 (6), City 7 (9)
City 7 connected to: City 1 (12), City 3 (9), City 5 (7), City 6 (9)
```

## Files

- `TSP_dynamic_programming.py`: Implementation of the TSP using the Held-Karp algorithm (Dynamic Programming)
- `TSP_som.py`: Implementation of the TSP using Self-Organizing Maps (SOM)

## Usage

### Running the Dynamic Programming Solution

```bash
python tsp_dynamic_programming.py
```

### Running the SOM Solution

```bash
python TSP_som.py
```

## Implementation Details

### Dynamic Programming Approach

The Dynamic Programming implementation:
- Uses the Held-Karp algorithm to find the optimal solution
- Has time complexity O(n²·2ⁿ) and space complexity O(n·2ⁿ)
- Guarantees finding the optimal solution
- Uses bit manipulation and memoization for efficiency

### SOM Approach

The Self-Organizing Map implementation:
- Creates a neural network ring that adapts to the city positions
- Uses competitive learning with a neighborhood function
- Provides a heuristic solution that approximates the optimal tour
- Can scale to larger problems where exact methods become infeasible

## Comparison of Methods

| Aspect | Dynamic Programming | Self-Organizing Map |
|--------|---------------------|---------------------|
| Optimality | Guarantees optimal solution | Approximates optimal solution |
| Time Complexity | O(n²·2ⁿ) | O(n²·m) where m is iterations |
| Scalability | Limited to ~20-25 cities | Can handle hundreds of cities |
| Memory Usage | Exponential (O(n·2ⁿ)) | Linear (O(n)) |

## Results

### Dynamic Programming
- Finds the optimal tour with minimal total distance
- Example output: `[1, 3, 5, 7, 6, 4, 2, 1]` with distance 49

### SOM
- Approximates the TSP solution using neural network approach
- Results may vary due to the stochastic nature of the algorithm
- Example output: `[1, 3, 5, 7, 6, 4, 2, 1]` with distance 49 (may vary)

## Authors

| Name                     | Reg No.         |
|--------------------------|------------------|
| Lunkuse Dorcus           | 24/U/06515/PS    |
| Serena Robinah           | 24/U/11034/PS    |
| Aturinzire Hargreave    | 24/U/22602/PS    |
| Abinsinguza Morison.K    | 24/U/02594/PS    |
| Biar Elijah Mabior       | 24/E/21430/PS    |
