#include <bits/stdc++.h>

using namespace std;

int n;

int main()
{
    vector<string> x = {"tmp", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"};
    vector<string> y = {"zero","one","two","three","four","five","six","seven","eight","nine"};
    vector<string> z = {"ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"};
    cin >> n;
    int a = n / 10;
    int b = n % 10;
    if(n < 10){
        cout << y[n];
    }
    else if(n<20){
        cout << z[b];
    }
    else{
        cout << x[a];
        if(b!=0){
            cout << "-" << y[b];
        }
    }
    return 0;
}
