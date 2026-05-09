class Solution:
    def rotateGrid(self, grid, k):

        rows = len(grid)
        cols = len(grid[0])

        # number of layers
        layers = min(rows, cols) // 2

        # process each layer one by one
        for layer in range(layers):

            arr = []

            # boundaries of current layer
            top = layer
            bottom = rows - 1 - layer
            left = layer
            right = cols - 1 - layer

            # -----------------------------
            # STEP 1: EXTRACT THE LAYER
            # -----------------------------

            # top row (left -> right)
            for j in range(left, right + 1):
                arr.append(grid[top][j])

            # right column (top+1 -> bottom)
            for i in range(top + 1, bottom + 1):
                arr.append(grid[i][right])

            # bottom row (right-1 -> left)
            for j in range(right - 1, left - 1, -1):
                arr.append(grid[bottom][j])

            # left column (bottom-1 -> top+1)
            for i in range(bottom - 1, top, -1):
                arr.append(grid[i][left])

            # Example for outer layer:
            # [1,2,3,4,8,12,16,15,14,13,9,5]

            # -----------------------------
            # STEP 2: ROTATE THE ARRAY
            # -----------------------------

            k_mod = k % len(arr)

            rotated = arr[k_mod:] + arr[:k_mod]

            # -----------------------------
            # STEP 3: PUT VALUES BACK
            # -----------------------------

            idx = 0

            # top row
            for j in range(left, right + 1):
                grid[top][j] = rotated[idx]
                idx += 1

            # right column
            for i in range(top + 1, bottom + 1):
                grid[i][right] = rotated[idx]
                idx += 1

            # bottom row
            for j in range(right - 1, left - 1, -1):
                grid[bottom][j] = rotated[idx]
                idx += 1

            # left column
            for i in range(bottom - 1, top, -1):
                grid[i][left] = rotated[idx]
                idx += 1

        return grid