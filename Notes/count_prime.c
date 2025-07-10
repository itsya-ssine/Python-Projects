// def count_primes(n):
//     if n < 2:
//         return 0  # No prime numbers below 2

//     # Initialize a boolean array to track prime numbers
//     is_prime = [True] * (n + 1)
//     is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

//     # Sieve of Eratosthenes
//     for i in range(2, int(n**0.5) + 1):
//         if is_prime[i]:
//             # Mark multiples of i as non-prime
//             for j in range(i * i, n + 1, i):
//                 is_prime[j] = False

//     # Count the number of primes
//     return sum(is_prime)

#include <stdbool.h>

int count_primes(int n) {
    if (n < 2) return 0; // No prime numbers below 2

    // Create a boolean array to track prime numbers
    bool is_prime[n + 1];
    for (int i = 0; i <= n; i++)
        is_prime[i] = true; // Initialize all entries as true

    is_prime[0] = is_prime[1] = false; // 0 and 1 are not prime

    // Sieve of Eratosthenes
    for (int i = 2; i <= sqrt(n); i++)
        if (is_prime[i])
            // Mark multiples of i as non-prime
            for (int j = i * i; j <= n; j += i)
                is_prime[j] = false;

    // Count the number of primes
    int count = 0;
    for (int i = 2; i <= n; i++)
        if (is_prime[i])
            count++;

    return count;
}

// 1991. Find the Middle Index in Array

// Given a 0-indexed integer array nums, find the leftmost middleIndex (i.e., the smallest amongst all the possible ones).

// A middleIndex is an index where nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1].

// If middleIndex == 0, the left side sum is considered to be 0. Similarly, if middleIndex == nums.length - 1, the right side sum is considered to be 0.

// Return the leftmost middleIndex that satisfies the condition, or -1 if there is no such index.

 

// Example 1:

// Input: nums = [2,3,-1,8,4]
// Output: 3
// Explanation: The sum of the numbers before index 3 is: 2 + 3 + -1 = 4
// The sum of the numbers after index 3 is: 4 = 4
// Example 2:

// Input: nums = [1,-1,4]
// Output: 2
// Explanation: The sum of the numbers before index 2 is: 1 + -1 = 0
// The sum of the numbers after index 2 is: 0
// Example 3:

// Input: nums = [2,5]
// Output: -1
// Explanation: There is no valid middleIndex.

int findMiddleIndex(int* nums, int numsSize) {
    if (numsSize == 0) return -1;

    int totalSum = 0;
    for (int i = 0; i < numsSize; i++) {
        totalSum += nums[i];
    }

    int leftSum = 0;
    for (int i = 0; i < numsSize; i++) {
        if (leftSum == totalSum - leftSum - nums[i]) {
            return i;
        }
        leftSum += nums[i];
    }

    return -1;
}