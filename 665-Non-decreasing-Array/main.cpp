#include <vector>

class Solution {
public:
    bool checkPossibility(std::vector<int>& nums) {
        bool possible = true;
        for (int i = 0; i < int(nums.size()-1); i++) {
            if (!(nums[i] <= nums[i+1])) {
                if (!possible) {
                    return false;
                } else {
                    if (i < int(nums.size()-2) && nums[i+2] < nums[i]) {
                        if (i != 0 && nums[i-1] > nums[i+1]) {
                            return false;
                        }
                        nums[i] = nums[i+2];
                    } else {
                        nums[i+1] = nums[i];
                    }
                    possible = false;
                }
            }
        }
        return true;
    }
};
