class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& numbers) {
        std::vector<std::vector<int>> result;

        std::sort(numbers.begin(), numbers.end());

        for (int i = 0; i < numbers.size(); i++) {
            if (i > 0 && numbers[i] == numbers[i - 1]) {
                continue;
            }

            int Lpointer = i + 1;
            int Rpointer = numbers.size() - 1;
            int target = numbers[i];

            while (Lpointer < Rpointer) {
                if (numbers[Lpointer] + numbers[Rpointer] == -target) {
                    result.push_back({target, numbers[Lpointer], numbers[Rpointer]});

                    while (Lpointer < Rpointer && numbers[Lpointer] == numbers[Lpointer + 1]) {
                        Lpointer++;
                    }

                    while (Rpointer > Lpointer && numbers[Rpointer] == numbers[Rpointer - 1]) {
                        Rpointer--;
                    }

                    Lpointer++;
                    Rpointer--;
                }
                else if (numbers[Lpointer] + numbers[Rpointer] < -target) {
                    Lpointer++;
                }
                else {
                    Rpointer--;
                }
            }
        }

    return result;

    }
};