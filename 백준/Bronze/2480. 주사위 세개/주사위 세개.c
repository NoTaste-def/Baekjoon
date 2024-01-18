#include <stdio.h>

int main(void) {
  int arr[3] = {0};
  scanf("%d %d %d", &arr[0], &arr[1], &arr[2]);

  int cnt = 0;
  int max = arr[0];
  int eq = 0;

  for(int i=0 ; i<3 ; i++){
    for(int j=i+1 ; j<3 ; j++){
      if(arr[i]==arr[j]){
        eq=arr[j];
        cnt++;
      }
    }
    if(cnt == 2){
      break;
    }
    if(arr[i]>max){
      max = arr[i];
    }
  }

  if(cnt==2){
    printf("%d", 10000+eq*1000);
  }
  else if(cnt==1){
    printf("%d", 1000+eq*100);
  }
  else{
    printf("%d", max*100);
  }
}