"""There are several squares being dropped onto the X-axis of a 2D plane.

You are given a 2D integer array positions where positions[i] = [lefti, sideLengthi] represents the ith square with a side length of sideLengthi that is dropped with its left edge aligned with X-coordinate lefti.

Each square is dropped one at a time from a height above any landed squares. It then falls downward (negative Y direction) until it either lands on the top side of another square or on the X-axis. A square brushing the left/right side of another square does not count as landing on it. Once it lands, it freezes in place and cannot be moved.

After each square is dropped, you must record the height of the current tallest stack of squares.

Return an integer array ans where ans[i] represents the height described above after dropping the ith square.



Example 1:


Input: positions = [[1,2],[2,3],[6,1]]
Output: [2,5,5]
Explanation:
After the first drop, the tallest stack is square 1 with a height of 2.
After the second drop, the tallest stack is squares 1 and 2 with a height of 5.
After the third drop, the tallest stack is still squares 1 and 2 with a height of 5.
Thus, we return an answer of [2, 5, 5].
Example 2:

Input: positions = [[100,100],[200,100]]
Output: [100,100]
Explanation:
After the first drop, the tallest stack is square 1 with a height of 100.
After the second drop, the tallest stack is either square 1 or square 2, both with heights of 100.
Thus, we return an answer of [100, 100].
Note that square 2 only brushes the right side of square 1, which does not count as landing on it.


Constraints:

1 <= positions.length <= 1000
1 <= lefti <= 108
1 <= sideLengthi <= 106

APPROACH: KEEP AN ORDERED QUEUE OF STACKS TO KEEP TRACK OF TALLEST STACK;
IF NEW INTERVAL OVERLAPS TOP BLOCK OF TALLEST STACK, ADD TO STACK THAT IS THE NEW TALLEST, UPDATE STACKS;
IF NEW INTERVAL OVERLAPS TOP BLOCK OF NEXT TALLEST STACK, ADD TO STACK, UPDATE STACK AND ORDERED QUEUE AND SO ON;
RETURN HEIGHT OF TALLEST STACK"""
from collections import namedtuple
from sortedcontainers import SortedSet

positions = [[1,2],[2,3],[6,1], [0, 2]]
output = [2,5,5]
positions2 = [[100,100],[200,100]]
output2 =  [100,100]
positions3 = [[1,2],[2,3],[6,1], [0, 2], [-2, 4]]

Stack = namedtuple('Stack', ['height', 'interval'])

def overlaps(position, stack):
    """Check for overlap with current stack"""
    stack_start, stack_end = stack.interval
    position_start, position_end = position[0], position[0] + position[1]
    return not (position_end <= stack_start or position_start >= stack_end)

def update_stack(position, stack, interval):
    """Create new stack if position overlaps stack"""
    return Stack(stack.height + position[1], interval)
    
def highest(stacks):
    """Return current heightest stack"""
    return stacks[0]

def falling_squares(positions):
    """Return max height after every block in positions"""
    intervals = [(position[0], position[0] + position[1]) for position in positions]
    ordered_stacks = SortedSet([Stack(positions[0][1], intervals[0])], key=lambda x: -x.height)
    ans = [positions[0][1]]
    for i, position in enumerate(positions[1:], start=1):
        overlaps_stack = False
        for stack in ordered_stacks:
            if overlaps(position, stack):
                new_stack = update_stack(position, stack, intervals[i])
                ordered_stacks.add(new_stack)
                overlaps_stack = True
                break
        if not overlaps_stack:
            ordered_stacks.add(Stack(positions[i][1], intervals[i]))
        ans.append(highest(ordered_stacks).height)
    return ans

    
print(falling_squares(positions3))