#include <bits/stdc++.h>

using namespace std;

int n;
string s;

int main()
{
    
    cin >> n;
    vector<int> l;
    vector<int> r;
    int l_sum = 0, r_sum = 0;
    cin >> s;
    for(int i = 0; i < n; i++){
        l_sum+= s[i] - '0';
        l.push_back(s[i] - '0');
    }
    
    for(int i =n; i < 2*n; i++){
        r_sum += s[i] - '0';
        r.push_back(s[i] - '0');
    }
    sort(l.begin(),l.end());
    sort(r.begin(), r.end());
    if(l_sum < r_sum){
        bool flag = true;
        for(int i = 0; i < n; i++){
            if(l[i] >= r[i]){
                flag = false;
                break;
            }
        }
        if(!flag){
            cout << "NO";
        }
        else{
            cout << "YES";
        }
        return 0;
    }
    else if(l_sum > r_sum){
        bool flag = true;
        for(int i = 0; i < n; i++){
            if(l[i] <= r[i]){
                flag = false;
                break;
            }
        }
        if(!flag){
            cout << "NO";
        }
        else{
            cout << "YES";
        }
        return 0;
    }
    else{
        cout << "NO";
    }

    

    return 0;
}
