class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        std::vector<int> result;

        int Lpointer = 0;
        int Rpointer = numbers.size() - 1;


        while (Lpointer < Rpointer) {
            cout << numbers[Lpointer] + numbers[Rpointer] << endl;
            if (numbers[Lpointer] + numbers[Rpointer] == target) {
                result.push_back(Lpointer + 1);
                result.push_back(Rpointer + 1);
                return result;
            }
            else if (numbers[Lpointer] + numbers[Rpointer] < target) {
                Lpointer++;
            }
            else {
                Rpointer--;
            }



        }



    }
};
