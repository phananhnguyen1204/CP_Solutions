#include <iostream>
#include <vector>

using namespace std;

int main(){
  int na,nb,k,m;
  cin >> na >> nb >> k >> m;
  vector<int>a(na);
  for(int i =0;i<na;i++){
    cin >> a[i];
  }
  vector<int>b(nb);
  for(int i =0;i<nb;i++){
    cin >> b[i];
  }
  cout << (b[nb-m]>a[k-1] ? "YES" : "NO");
  return 0;
}