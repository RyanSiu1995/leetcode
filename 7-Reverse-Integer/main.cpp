#include <math.h> 
#include <limits.h>

class Solution {
public:
    int reverse(int x) {
        if (x == 0) { return 0; }
        double result = 0;
        int incrementor = 0;
        for (int i = 9; i >= 0; i--) {
            int digit = int(x / pow(10, i)) % 10;
            if (digit == 0 && incrementor == 0) { continue; }
            result += digit * pow(10, incrementor);
            incrementor++;
        }
        return ((result / abs(result)) > 0 ? result > INT_MAX : result < INT_MIN ) ? 0 : (int) result;
    }
};
