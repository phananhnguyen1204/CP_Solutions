#include <bits/stdc++.h>

using namespace std;

int n;
string name, type;

bool option(pair<string,pair<int,int>> a, pair<string,pair<int,int>> b){
    return a.second.first < b.second.first || (a.second.first == b.second.first && a.second.second < b.second.second);
}

int main()
{
    cin >> n;
    vector<pair<string,pair<int,int>>> v(n);
    for(int i =0; i < n; i++){
        cin >> name >> type;
        if(type == "captain"){
            v[i] = {name,{5,i}};
        }
        else if(type == "man"){
            v[i] = {name,{4,i}};
        }
        else if(type == "woman"){
            v[i] = {name,{3,i}};
        }
        else if(type == "child"){
            v[i] = {name,{3,i}};
        }
        else{
            v[i] = {name,{1,i}};
        }
    }
    sort(v.begin(), v.end(),option);
    for(int i = 0; i < n; i++){
        cout << v[i].first << endl;
    }
    
    return 0;
}
