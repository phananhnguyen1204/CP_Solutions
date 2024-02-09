
#include <bits/stdc++.h>
#define MAX 1e9 + 5
using namespace std;


long long t,sx,sy,ex,ey;
string s;


int main()
{
    cin >> t >> sx >> sy >> ex >> ey;
    cin >> s;
    long long diffx = ex - sx;
    long long diffy = ey - sy;
    long long cnt = 0;
    for(char c: s){
        if(sx != ex){
            if(diffx <0){
                if(c == 'W'){
                    sx--;
                }
            }
            else if (diffx > 0){
                if(c == 'E'){
                    sx++;
                }
            }            
        }
        if(sy != ey){
            if(diffy <0){
                if(c == 'S'){
                    sy--;
                }
            }
            else if(diffy > 0){
                if(c == 'N'){
                    sy++;
                }
            }            
        }

        cnt++;
        if(sx == ex && ey == sy){
            if(cnt > t){
                cout << -1;
            }
            else{
                cout << cnt;
            }
            return 0;
        }
    }
    cout << -1;

    

    return 0;
}
