#include <bits/stdc++.h>

using namespace std;

int x,a,n;

int main()
{
    cin >> n;
    vector<pair<int,int>> negative, positive;
    for(int i = 0; i < n; i++){
        cin >> x >> a;
        if(x < 0){
            negative.push_back({x,a});
        }
        else{
            positive.push_back({x,a});
        }
    }
    sort(negative.begin(), negative.end(), greater<pair<int,int>>());
    sort(positive.begin(), positive.end());
    int res = 0;
    int neg_size = negative.size();
    int pos_size = positive.size();
    if(neg_size > pos_size){
        for(int i = 0; i < pos_size; i++){
            res += positive[i].second;
        }
        for(int i = 0; i < pos_size + 1; i++){
            res += negative[i].second;
        }
    }
    else if(neg_size == pos_size){
        for(int i = 0; i < pos_size; i++){
            res += negative[i].second + positive[i].second;
        }
    }
    else{
        for(int i = 0; i < neg_size; i++){
            res += negative[i].second;
        }     
        for(int i = 0 ; i < neg_size + 1; i++){
            res += positive[i].second;
        }
    }
    cout << res;
    return 0;
}
