#include <bits/stdc++.h>

using namespace std;

long long n,d,a,b,low,high;

struct Client{
    long long low,high,index;
};

bool option(Client m, Client z){
    return (m.low * a + m.high * b) < (z.low * a + z.high * b);
}

int main()
{
    cin >> n >> d >> a >> b;
    vector<Client> v;
    for(auto i = 0; i < n; i++){
        cin >> low >> high;
        long long index = i;
        v.push_back((Client){low,high,index});
    }
    sort(v.begin(),v.end(),option);
    long long cnt = 0;
    vector<long long> res;
    for(auto i = 0; i < n; i++){
        if(cnt + v[i].low * a + v[i].high * b > d){
            break;
        }
        cnt += v[i].low * a + v[i].high * b;
        res.push_back(v[i].index);
    }
    cout << res.size() << endl;
    for(auto i = 0; i < res.size(); i++){
        cout << res[i] + 1 << " ";
    }

    return 0;
}
