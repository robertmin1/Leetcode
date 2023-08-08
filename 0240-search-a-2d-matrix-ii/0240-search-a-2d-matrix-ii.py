class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        s, e = 0, len(matrix[0]) - 1  # Initialize start and end indices.

        def helper(s, e):
            while s < len(matrix) and e >= 0:  # Check bounds.
                if matrix[s][e] == target:  # Target found.
                    return True
                elif matrix[s][e] > target:  # Move left.
                    e -= 1
                else:  # Move down.
                    s += 1
            return False  # Target not found.

        return helper(s, e)