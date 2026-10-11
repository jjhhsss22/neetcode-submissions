class Solution {
public:
    int trap(vector<int>& height) {
        std::vector<int> prefixMax, suffixMax;

        int total_water = 0;

        for (int i = 0; i < height.size(); i++) {
            int preMax = 0;
            int suffMax = 0;
            for (int j = 0; j < i; j++) {
                preMax = std::max(preMax, height[j]);
            }
            for (int k = i + 1; k < height.size(); k++) {
                suffMax = std::max(suffMax, height[k]);
            }
            int water_trapped = std::min(preMax, suffMax) - height[i];
            if (water_trapped > 0) total_water += water_trapped;
        }

        return total_water;

    }
};

