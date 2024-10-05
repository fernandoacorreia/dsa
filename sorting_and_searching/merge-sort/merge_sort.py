# See https://en.wikipedia.org/wiki/Merge_sort

def merge_sort(arr):

    # Top-down implementation using lists
    def merge_sort_list(m):
        if len(m) <= 1:
            return m

        # Recursive case. First, divide the list into equal-sized sublists
        # consisting of the first half and second half of the list.
        left = []
        right = []
        for i, x in enumerate(m):
            if i < (len(m) / 2):
                left.append(x)
            else:
                right.append(x)

        # Recursively sort both sublists.
        left = merge_sort_list(left)
        right = merge_sort_list(right)

        # Then merge the now-sorted sublists.
        return merge(left, right)

    def merge(left, right):
        # Initialize variables.
        result = []
        len_left = len(left)
        len_right = len(right)
        l = 0  # current index on left
        r = 0  # current index on right

        # Append to result from either left or right (whichever is smaller).
        while l < len_left and r < len_right:
            if left[l] <= right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1

        # Either left or right may have elements left; consume them.
        # (Only one of the following loops will actually be entered.)
        while l < len_left:
            result.append(left[l])
            l += 1
        while r < len_right:
            result.append(right[r])
            r += 1
        return result

    return merge_sort_list(arr)
