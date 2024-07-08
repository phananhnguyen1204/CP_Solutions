#include <bits/stdc++.h>

using namespace std;

int T, N;
int res = 0;
string s;

int main()
{
    cin >> T;
    for (int tc = 1; tc <= T; tc++)
    {
        cout << "Case #" << tc << ": ";
        cin >> s;
        int size = s.length();
        string temp = s;
        bool found = false;
        for (int i = 0; i < size; i++)
        {
            int swap_index = i;
            for (int j = i + 1; j < size; j++)
            {
                if (i == 0)
                {
                    if (temp[i] > temp[j] && temp[j] != '0')
                    {
                        if (temp[j] <= temp[swap_index])
                        {
                            swap_index = j;
                        }
                        found = true;
                    }
                }
                else
                {
                    if (temp[i] > temp[j])
                    {
                        if (temp[j] <= temp[swap_index])
                        {
                            swap_index = j;
                            found = true;
                        }
                    }
                }
            }
            if (found)
            {
                swap(temp[i], temp[swap_index]);
                break;
            }
        }
        cout << temp << " ";
        temp = s;
        found = false;
        for (int i = 0; i < size; i++)
        {
            int swap_index = i;
            for (int j = i + 1; j < size; j++)
            {
                if (temp[j] > temp[i])
                {
                    if (temp[j] >= temp[swap_index])
                    {
                        swap_index = j;
                        found = true;
                    }
                }
            }
            if (found)
            {
                swap(temp[i], temp[swap_index]);
                break;
            }
        }
        cout << temp << endl;
    }
    return 0;
}