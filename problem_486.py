"""You are given an integer array nums. Two players are playing a game with this array: player 1 and player 2.

Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of 0. At each turn, the player takes one of the numbers from either end of the array (i.e., nums[0] or nums[nums.length - 1]) which reduces the size of the array by 1. The player adds the chosen number to their score. The game ends when there are no more elements in the array.

Return true if Player 1 can win the game. If the scores of both players are equal, then player 1 is still the winner, and you should also return true. You may assume that both players are playing optimally."""
from functools import cache

nums1 = [1,5,233,7]
nums2 = [1,5,2]
nums3 = [0,0,7,6,5,6,1]
nums4 = [2,4,55,6,8]

def predict_the_winner(nums):
    @cache
    def score_recursive(numbers):
        if not numbers:
            return 0
        if len(numbers) == 1:
            return numbers[0]
        if len(numbers) == 2:
            return max(numbers)      
        return max(min(score_recursive(numbers[2:]) + numbers[0], score_recursive(numbers[1:-1]) + numbers[0]), min(score_recursive(numbers[:-2]) + numbers[-1], score_recursive(numbers[1:-1]) + numbers[-1]))
    
    return score_recursive(tuple(nums)) >= max(score_recursive(tuple(nums[1:])), score_recursive(tuple(nums[:-1])))

print(predict_the_winner(nums4))


    
    
        






    