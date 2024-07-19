class Solution {
public:
    vector<int> luckyNumbers (vector<vector<int>>& matrix) {
        vector<int> res;
        int rows = matrix.size();
        int cols = matrix[0].size();
        
        vector<int> min_rows(rows,0);
        vector<int> max_cols(cols,0);
        for(int r = 0; r < rows; r++){
            int curr_min = 1e9;
            for(int c = 0; c < cols; c++){
                curr_min = min(curr_min, matrix[r][c]);
            }
            min_rows[r] = curr_min;
        }

        for(int c = 0; c < cols; c++){
            int curr_max = -1e9;
            for(int r = 0; r < rows; r++){
                curr_max = max(curr_max, matrix[r][c]);
            }
            max_cols[c] = curr_max;
        }

        for(int r = 0; r < rows; r++){
            for(int c = 0; c < cols; c++){
                if(matrix[r][c] == max_cols[c] && matrix[r][c] == min_rows[r]){
                    res.push_back(matrix[r][c]);
                }
            }
        }

        return res;
    }
};