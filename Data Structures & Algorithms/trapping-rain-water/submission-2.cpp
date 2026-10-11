class Solution {
public:
    int trap(vector<int>& height) {
        if (height.size() == 0) return 0;

        std::vector<int> prefixMax(height.size()), suffixMax(height.size());

        prefixMax[0] = height[0];
        for (int i = 1; i < height.size(); i++) {
            prefixMax[i] = std::max(prefixMax[i - 1], height[i]);
        }

        suffixMax[height.size() - 1] = height[height.size() - 1];
        for (int i = height.size() - 2; i >= 0; i--) {
            suffixMax[i] = std::max(suffixMax[i + 1], height[i]);
        }

        int total_water = 0;

        for (int i = 0; i < prefixMax.size(); i++) {
            total_water += std::min(prefixMax[i],suffixMax[i]) - height[i];
        }

        return total_water;

    }
};

