class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        pair = [(s, v) for s, v in zip(position, speed)]
        pair.sort(reverse=True)

        for i in range(len(pair)):
            time = (target - pair[i][0]) / pair[i][1]

            if not stack:
                stack.append(time)
            else:
                if time <= stack[-1]:
                    continue
                else:
                    stack.append(time)

        return len(stack)