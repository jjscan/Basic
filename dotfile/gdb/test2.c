#include<stdio.h>

int hap(int x,int y);

main(void) 
{
	int a,b,gap;
	printf("정수 a,b를 입력하세요:");
	scanf("%d %d",&a,&b);
	gap = hap(a,b);
	printf("\n%d + %d = %d \n",a,b,gap);
}
int hap(int x, int y)
{
	return(x + y);
}
