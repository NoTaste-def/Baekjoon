#include <stdio.h>

int main(void) {
  int a[3]={0};
  scanf("%d %d\n%d", &a[0], &a[1], &a[2]);
  int m,h;
  int tmp;
  tmp = a[0]*60+a[1]+a[2];
  h = tmp/60;
  m = tmp%60; 
  printf("%d %d", h%24, m);
}