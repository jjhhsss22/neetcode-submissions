class Solution {
public:
    int maxArea(vector<int>& heights) {
        int maximum = 0;
        int Lpointer = 0;
        int Rpointer = heights.size() - 1;

        while (Lpointer < Rpointer) {
            int area = (Rpointer - Lpointer) * (heights[Lpointer] > heights[Rpointer] ? heights[Rpointer] : heights[Lpointer]);

            if (area > maximum) maximum = area;

            if (heights[Lpointer] > heights[Rpointer]) Rpointer--;
            else Lpointer++;
        }

        return maximum;
    }
};
