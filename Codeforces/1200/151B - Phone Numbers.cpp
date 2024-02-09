#include <bits/stdc++.h>

using namespace std;

int n,m;
string name,phone;

bool check_taxi(string str){
    int prev = str[0] - '0';
    for(char c: str){
        if(isdigit(c) && c - '0' != prev){
            return false;
        }
    }
    return true;
}

bool check_pizza(string str){
    int prev = str[0] - '0';
    for(int i = 1; i < str.length(); i++){
        if(isdigit(str[i]) && (str[i] - '0' >= prev)){
            return false;
        }
        if(isdigit(str[i])){
            prev = str[i] - '0';
        }
        
    }
    return true;
}

int main(){
    cin >> n;
    vector<int> taxi(n,0);
    vector<int> pizza(n,0);
    vector<int> girl(n,0);
    vector<string> s(n);
    int max_taxi = 0, max_pizza = 0, max_girl = 0;
    for(int i = 0; i < n; i++){
        cin >> m >> name;
        s[i] = name;
        for(int j = 0; j < m; j++){
            cin >> phone;
            if(check_taxi(phone)){
                taxi[i]++;
            }
            else if(check_pizza(phone)){
                pizza[i]++;
            }
            else{
                girl[i]++;
            }
        }
    }
    max_taxi = *max_element(taxi.begin(),taxi.end());
    max_pizza = *max_element(pizza.begin(), pizza.end());
    max_girl = *max_element(girl.begin(),girl.end());
    cout << "If you want to call a taxi, you should call: ";
    int flag_taxi = 0;
    for(int i = 0; i < taxi.size(); i++){
        if(taxi[i] == max_taxi && flag_taxi == 0){
            cout << s[i];
            flag_taxi++;
        }
        else if(taxi[i] == max_taxi && flag_taxi != 0){
            cout << ", " << s[i];
        }
    }
    cout << "." << endl;
     cout << "If you want to order a pizza, you should call: ";
    int flag_pizza = 0;
    for(int i = 0; i < pizza.size(); i++){
        if(pizza[i] == max_pizza && flag_pizza == 0){
            cout << s[i];
            flag_pizza++;
        }
        else if(pizza[i] == max_pizza && flag_pizza != 0){
            cout << ", " << s[i];
        }
    }
    cout << "." << endl;
   
    cout << "If you want to go to a cafe with a wonderful girl, you should call: ";
    int flag_girl = 0;
    for(int i = 0; i < girl.size(); i++){
        if(girl[i] == max_girl && flag_girl == 0){
            cout << s[i];
            flag_girl++;
        }
        else if(girl[i] == max_girl && flag_girl != 0){
            cout << ", " << s[i];
        }
    }
    cout << "." << endl;
  
  
  
  return 0;
}