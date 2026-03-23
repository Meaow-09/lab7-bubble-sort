import time
import os


def clear_terminal() -> None:
    """
    TODO: Clear the terminal screen for in-place animation.
    Hint: Use ANSI escape code '\033[2J\033[H' or os.system('clear').
    """
    pass


def render_bar_chart(arr: list) -> str:
    """
    TODO: Convert list of numbers into a visual bar chart.
    Args:
        arr: List of integers to visualize
    Returns:
        A string representation of horizontal bars (e.g., using '*' or '█')
    
    Hint: Normalize each number to a width (e.g., arr[i] // max(arr) * 20 chars)
    """
    pass


def visualize_step(arr: list, delay: float = 0.1) -> None:
    """
    TODO: Display current array state with animation.
    Args:
        arr: Current state of the array being sorted
        delay: Time in seconds to pause before next frame
    
    Hint: Call clear_terminal(), render_bar_chart(), print result, then time.sleep(delay)
    """
    pass


def bubble_sort(arr : list) -> list:
    """
    Sorts an array in-place using bubble sort with real-time animation.
    
    TODO: Uncomment the visualization call below to see the animation.
    """
    for o in range(len(arr)):
        swapped = False
        for i in range(len(arr) - o - 1):
            if arr[i + 1] < arr[i]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                # TODO: Call visualize_step(arr) here to animate each swap
        if not swapped:
            break
    return arr

if __name__ == '__main__':
    a = [8, 2, 5, 6, 7, 0, 9]
    print(bubble_sort(a))
