//  # 11726 2xn타일링 
#include <stdio.h>

int main()
{    
    int DP[2000];
    DP[1] = 1;
    DP[2] = 2;
    int n;
    scanf("%d",&n);
    for(int i = 3; i<= n; i++)
    {
        DP[i]= DP[i-1] + DP[i-2];
        DP[i]= DP[i]%10007;
    }
    printf("%d",DP[n]);
}