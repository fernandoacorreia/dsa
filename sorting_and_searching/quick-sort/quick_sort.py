# See https://en.wikipedia.org/wiki/Quicksort

# Sort using Lomuto's partition scheme.
def quick_sort_lomuto(arr):

    def sort_subarrays(arr, lo, hi):
        if lo >= hi or lo < 0:
            return

        # Partition array and get the pivot index.
        p = partition(arr, lo, hi)

        # Sort the two partitions.
        sort_subarrays(arr, lo, p - 1)  # Left side of pivot.
        sort_subarrays(arr, p + 1, hi)  # Right side of pivot.

    def partition(arr, lo, hi):
        pivot = arr[hi]  # Choose the last element as the pivot.
        i = lo
        for j in range(lo, hi):
            # If the current element is less than or equal to the pivot
            if arr[j] <= pivot:
                # Swap the current element with the element at the temporary pivot index.
                swap(arr, i, j)
                # Move the temporary pivot index forward.
                i += 1
        # Swap the pivot with the last element.
        swap(arr, i, hi)
        return i  # The pivot index.

    def swap(arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    sort_subarrays(arr, 0, len(arr) - 1)

# Sort using Hoare's partition scheme.
def quick_sort_hoare(arr):

    def sort_subarrays(arr, lo, hi):
        if lo >= 0 and hi >= 0 and lo < hi:
            p = partition(arr, lo, hi)
            sort_subarrays(arr, lo, p)
            sort_subarrays(arr, p + 1, hi)

    def partition(arr, lo, hi):
        # Pivot value
        pivot = arr[lo]  # Choose the first element as the pivot.
        # Left index
        i = lo - 1
        # Right index
        j = hi + 1
        # Loop until exit
        while True:
            # Move the left index to the right at least once and while
            # the element at the left index is less than the pivot.
            while True:
                i += 1
                if arr[i] >= pivot:
                    break
            # Move the right index to the left at least once and while the
            # element at the right index is greater than the pivot.
            while True:
                j -= 1
                if arr[j] <= pivot:
                    break
            # If the indices crossed, return.
            if i >= j:
                return j
            # Swap the elements at the left and right indices.
            swap(arr, i, j)

    def swap(arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    sort_subarrays(arr, 0, len(arr) - 1)
