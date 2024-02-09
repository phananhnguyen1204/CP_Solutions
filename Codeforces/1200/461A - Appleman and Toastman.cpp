
#include <bits/stdc++.h>

using namespace std;

int n;

int main()
{
    cin >> n;
    vector<int> v(n);
    long long sum = 0;
    for(int i = 0; i < n; i++){
        cin >> v[i];
        sum += v[i];
    }
    sort(v.begin(), v.end());
    int cnt = v.size();
    long long res = sum;
    int index = 0;
    while(cnt > 1){
        res += sum;
        cnt--;
        sum -= v[index];
        index++;
    }
    cout << res;

    return 0;
}
