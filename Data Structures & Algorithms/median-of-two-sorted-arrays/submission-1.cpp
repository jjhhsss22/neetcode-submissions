class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int n = nums1.size() + nums2.size();
        int mid = (n + 1) / 2;

        int l = 0;

        if (nums1.size() > nums2.size()) {
            std::swap(nums1, nums2);
        }

        int r = nums1.size();

        while (l <= r) {
            int m = (l + r) / 2;
            int m2 = mid - m;

            int left1 = (m > 0) ? nums1[m - 1] : INT_MIN;
            int right1 = (m < nums1.size()) ? nums1[m] : INT_MAX;
            int left2 = (m2 > 0) ? nums2[m2 - 1] : INT_MIN;
            int right2 = (m2 < nums2.size()) ? nums2[m2] : INT_MAX;

            if (left1 <= right2 && left2 <= right1) {
                if ((n % 2) == 0) {
                    return (std::max(left1, left2) + std::min(right1, right2)) / 2.0;
                } else {
                    return std::max(left1, left2);
                }
            } else if (left1 > right2) {
                r = m - 1;
            } else {
                l = m + 1;
            }
        }

        return -1;
    }
};
