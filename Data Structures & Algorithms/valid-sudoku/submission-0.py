
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows =  [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        cols =  [set(), set(), set(), set(), set(), set(), set(), set(), set()]
        boxes = [set(), set(), set(), set(), set(), set(), set(), set(), set()]

        # Create Hash Sets while checking
        for i, row in enumerate(board):
            for j, val in enumerate(row):
                if (val == "."):
                    continue

                k = i // 3 + j // 3 * 3
                if (val in rows[i] or val in cols[j] or val in boxes[k]):
                    return False
                else:
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[k].add(val)

        return True