#include <bits/stdc++.h>

using namespace std;

int n;
int x;

int main()
{
    
    cin >> n;
    int curr = 0;
    unordered_map<int,int> cnt;
    for(int i = 0; i < n; i++){
        cin >> x;
        if(x == 25){
            cnt[25]++;
        }
        else if(x == 50){
            cnt[50]++;
            if(cnt[25] == 0){
                cout << "NO";
                return 0;
            }
            else{
                cnt[25]--;
            }
        }
        else{
            if(cnt[50] >= 1 && cnt[25] >= 1){
                cnt[50]--;
                cnt[25]--;
            }
            else if(cnt[25] >= 3){
                cnt[25] -= 3;
            }
            else{
                cout << "NO";
                return 0;
            }
        }
    }
    cout << "YES";
    

    return 0;
}
