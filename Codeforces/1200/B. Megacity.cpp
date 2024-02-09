

#include <bits/stdc++.h>

using namespace std;

int n,s,x,y,w;

int main()
{
    cin >> n >> s;
    map<double, int> locations;
    for(int i = 0; i < n; i++){
        cin >> x >> y >> w;
        double r = x*x + y*y;
        locations[r] += w;
    }
    double res = -1;
    double curr = s;
    for(auto it = locations.begin(); it!=locations.end();it++ ){
        curr += it->second;
        if(curr >= 1000000){
            res = it->first;
            break;
        }
    }
    if(res == -1){
        cout << -1 << endl;
        return 0;
    }
    cout << fixed << setprecision(6) << sqrt(res);
    return 0;
    
}
