"""
Task 4.1: Truck Loading as 0/1 Knapsack (Dynamic Programming)
"""
def knapsack_dp(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    # Traceback
    w = capacity
    loaded_parcels = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            loaded_parcels.append(i)
            w -= weights[i-1]
            
    return dp[n][capacity], loaded_parcels

if __name__ == "__main__":
    S = 7148
    W = 20 + (S % 11)
    print(f"--- TASK 4.1: 0/1 KNAPSACK TRUCK LOADING (Capacity W = {W} kg) ---")
    
    weights = [2, 3, 4, 5, 6, 7, 8, 9]
    values = [180, 250, 300, 420, 450, 560, 610, 700]
    
    max_fee, loaded = knapsack_dp(weights, values, W)
    print(f"Optimal Total Delivery Fee: PHP {max_fee}")
    print(f"Loaded Parcels (1-indexed): {loaded}")
    print("Task 4.1 executed successfully.\n")
