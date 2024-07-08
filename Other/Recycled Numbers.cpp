#include <bits/stdc++.h>

using namespace std;

int T, n, m;
int cnt = 0;
int A, B;

void check(int i)
{
    int temp = i;
    int power = 1;
    int j = i;
    while (temp >= 10)
    {
        temp /= 10;
        power *= 10;
    }
    do
    {
        j = j / 10 + (j % 10) * power;
        if (j > i && j <= B)
        {
            cnt++;
        }
    } while (i != j);
}

int main()
{
    cin >> T;
    for (int tc = 1; tc <= T; tc++)
    {
        cin >> A >> B;
        cnt = 0;
        for (int i = A; i <= B; i++)
        {
            check(i);
        }

        cout << "Case #" << tc << ": " << cnt;
        cout << endl;
    }
    return 0;
}