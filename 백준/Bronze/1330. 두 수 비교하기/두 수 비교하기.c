#include <stdio.h>

int flag(int arr[]){
  if(arr[0]>arr[1]){
    return 0;
  }
  else if(arr[0]<arr[1]){
    return 1;
  }
  else{
    return 2;
  }
}

int main(void) {
  int arr[2] = {0};
  scanf("%d %d", &arr[0], &arr[1]);
  switch(flag(arr)){
    case 0:
      printf(">");
      break;
    case 1:
      printf("<");
      break;
    default:
      printf("==");
      break;
  }
}