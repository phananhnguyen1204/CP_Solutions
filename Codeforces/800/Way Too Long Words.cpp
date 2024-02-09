#include <bits/stdc++.h>
#define ll long long

using namespace std;

int n;
string word;

int main(){
    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> word;
        if(word.length() <= 10){
            cout << word << endl;
        }
        else{
            cout << word[0] << word.length()-2 << word[word.length()-1] << endl;
        }
    }

  
  return 0;
}