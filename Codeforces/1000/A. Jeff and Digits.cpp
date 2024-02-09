
#include <bits/stdc++.h>
#define MAX 100000 + 5
using namespace std;

int n;

int main()
{
    cin >> n;
    vector<int> v(n);
    int cnt_zero = 0, cnt_five = 0;
    for(int i = 0; i < n; i++){
        cin >> v[i];
        if(v[i] == 0){
            cnt_zero++;
        }
        else{
            cnt_five++;
        }
    }
    if(cnt_zero == 0){
        cout << "-1";
        return 0;
    }
    string res = "";
    while(cnt_five * 5 % 9 !=0){
        cnt_five--;
    }
    if(cnt_five == 0 && cnt_zero == 0){
        cout << "-1";
        return 0;
    }
    for(int i =0; i < cnt_five; i++){
        res += "5";
    }
    if(res == ""){
        cout << "0";
        return 0;
    }
    for(int i = 0; i < cnt_zero; i++){
        res += "0";
    }
    cout << res;


    return 0;
}
