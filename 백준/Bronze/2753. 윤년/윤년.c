#include <stdio.h>

int main(void) {
  int a;
  scanf("%d", &a);
  int r1 = a%4;
  int r2 = a%400;
  int r3 = a%100;
  if(  (r1==0 && r3!=0) || r2==0 ){
    printf("1");
  }
  else{
    printf("0");
  }
}