
#include <bits/stdc++.h>
#define MAX 1e9 + 5
using namespace std;

long long n,value;


int main()
{   
    cin >> n;
    long long sum = 0;
    long long min_odd = 1e9+ 5;
    for(int i = 0; i < n; i++){
        cin >> value;
        sum += value;
        if(value %2 == 1){
            min_odd = min(min_odd,value);
        }
    }
    if(sum % 2 == 1){
        if(min_odd == (1e9 + 5)){
            cout << 0;
        }
        else{
            cout << (sum - min_odd);
        }
    }
    else{
        cout << sum;
    }


    

    return 0;
}
