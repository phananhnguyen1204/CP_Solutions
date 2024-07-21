class Solution {
public:
    int minChanges(int n, int k) {
        if ((n | k) != n) {
            return -1;
        }
        int res = n ^ k;
        int cnt = 0;
        while (res) {
            cnt += res & 1;
            res >>= 1;
        }
        return cnt;
    }
};