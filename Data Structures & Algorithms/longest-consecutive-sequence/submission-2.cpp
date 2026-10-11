class Solution {
public:
    int longestConsecutive(std::vector<int> &nums) {
        std::unordered_set<int> starters = checkValidStarters(nums);

        int counter = 0;

        for (int starter : starters) {
            int i = 1;
            int target = starter;
            while (true) {
                target++;
                if (std::find(nums.begin(), nums.end(), target) != nums.end()) {
                    i++;
                }
                else {
                    if (counter < i) {
                        counter = i;
                    }

                    break;
                }
            }
        }

        return counter;
    }

private:
    std::unordered_set<int> checkValidStarters(std::vector<int> &nums) {
        std::unordered_set<int> validStarters;
        std::unordered_set<int> numsSet(nums.begin(), nums.end());

        for (int num : numsSet) {
            if (numsSet.count(num - 1) == 0) {
                validStarters.insert(num);
            }
        }

        return validStarters;
    }
};
