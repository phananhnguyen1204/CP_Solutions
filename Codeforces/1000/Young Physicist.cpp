#include <bits/stdc++.h>
#define ll long long

using namespace std;

int n,x,y,z;
vector<int> arr(3,0);


int main(){
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> x >> y >> z;
        arr[0]+=x;
        arr[1] += y;
        arr[2] += z;
    }
    if(arr[0] == 0 && arr[1] == 0 && arr[2] == 0){
        cout << "YES";
    }
    else{
        cout << "NO";
    }

  
  return 0;
}