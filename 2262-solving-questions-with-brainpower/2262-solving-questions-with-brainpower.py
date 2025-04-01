from typing import List

class Solution:
    def max_points(self, index: int, questions: List[List[int]], memo: List[int], total_questions: int) -> int:
        if index >= total_questions:
            return 0
        if memo[index] != -1:
            return memo[index]

        points, skip_steps = questions[index]
        take = points + self.max_points(index + skip_steps + 1, questions, memo, total_questions)
        skip = self.max_points(index + 1, questions, memo, total_questions)

        memo[index] = max(take, skip)
        return memo[index]

    def mostPoints(self, questions: List[List[int]]) -> int:
        total_questions = len(questions)
        memo = [-1] * total_questions
        return self.max_points(0, questions, memo, total_questions)
