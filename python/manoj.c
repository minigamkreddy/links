# include<string.h>
#include<stdio.h>
#include<stdlib.h>
int main()
{
	int ret;
    char a;
	printf("enter a character\n");
    scanf("%c",&a);
    //gets(a);
	ret=is_alpha(a);
	if(ret){
		printf("well! you've entered an alpha\n");
	}
	else {
		printf("bad ! that's not a alpha value\n");
	}
	
	return 0;
}

	int is_alpha(int c)
	
	{
		
			if( ( c > 64 && c <91 ) || ( c > 96 && c < 123 ) )
	
					{	
						return 2;
											
									}
					else return 0;
			}


