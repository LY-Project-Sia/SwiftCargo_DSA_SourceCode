"""
Task 1: Why is the daily report so slow? (Lesson 1)
Optimized report generation using Hash Sets and Merge Sort.
Student Seed S = 7148, n = 8,148
"""
import random
import time

def remove_duplicates_optimized(scans):
    """O(n) de-duplication using a hash set."""
    return list(set(scans))

def merge_sort_parcels(parcels):
    """O(n log n) Merge Sort by weight."""
    if len(parcels) <= 1:
        return parcels
    
    mid = len(parcels) // 2
    left = merge_sort_parcels(parcels[:mid])
    right = merge_sort_parcels(parcels[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][1] <= right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def count_heavy_iterative(parcels):
    """Iterative heavy parcel counter (weight > 20kg)."""
    return sum(1 for p in parcels if p[1] > 20)

def randomized_select(parcels, k):
    """Finds the k-th smallest parcel weight in expected O(n) time."""
    if len(parcels) == 1:
        return parcels[0]
    
    pivot = random.choice(parcels)
    lows = [p for p in parcels if p[1] < pivot[1]]
    pivots = [p for p in parcels if p[1] == pivot[1]]
    highs = [p for p in parcels if p[1] > pivot[1]]
    
    if k < len(lows):
        return randomized_select(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return randomized_select(highs, k - len(lows) - len(pivots))

if __name__ == "__main__":
    S = 7148
    n = 1000 + S
    print(f"--- TASK 1: REPORT MODULE OPTIMIZATION (n = {n}) ---")
    
    # Generate mock scans and parcels
    scans = [f"SC2026{i:06d}" for i in range(n)] + [f"SC2026{random.randint(0, n//2):06d}" for _ in range(500)]
    parcels = [(f"SC2026{i:06d}", round(random.uniform(1.0, 50.0), 2)) for i in range(n)]
    
    start = time.time()
    unique_scans = remove_duplicates_optimized(scans)
    print(f"De-duplication complete: {len(unique_scans)} unique scans in {time.time() - start:.4f}s")
    
    start = time.time()
    sorted_parcels = merge_sort_parcels(parcels)
    print(f"Merge Sort complete: {len(sorted_parcels)} parcels sorted in {time.time() - start:.4f}s")
    
    heavy_count = count_heavy_iterative(parcels)
    print(f"Heavy parcels (>20kg): {heavy_count}")
    
    median_parcel = randomized_select(parcels, len(parcels) // 2)
    print(f"Median parcel (Randomized-Select): {median_parcel}")
    print("Task 1 executed successfully.\n")
