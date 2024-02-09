#include <bits/stdc++.h>

using namespace std;

int main()
{
    vector<int> v(6);
    unordered_map<int,int> freqs;
    for(int i = 0; i < 6; ++i){
        cin >> v[i];
        freqs[v[i]]++;
    }
    vector<int> res;
    bool found = false;
    for(auto it: freqs){
        if(it.second >= 4){
            found = true;
        }
        else{
            for(int j = 0; j < it.second; j++){
                res.push_back(it.first);
            }
        }
    }
    if(!found){
        cout << "Alien";
        return 0;
    }
    if(res.size() == 0){
        cout << "Elephant";
    }
    else if(res.size() == 1){
        cout << "Bear";
    }
    else{
        cout << (res[0] != res[1] ? "Bear" : "Elephant");
    }
    

    return 0;
}
