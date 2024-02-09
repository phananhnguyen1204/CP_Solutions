#include <bits/stdc++.h>

using namespace std;

int n;
string s;


int main()
{
    cin >> n;
    stack<char> st;
    cin >> s;
    for(char c: s){
        if(!st.empty() && st.top() != c){
            st.pop();
        }
        else{
            st.push(c);
        }
    }
    cout << st.size();
    
    return 0;
}
