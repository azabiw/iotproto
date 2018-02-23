#include <wiringPi.h>
#include <stdio.h>
int main(void)
{
  int in = 24;
  int out = 4;
  wiringPiSetupGpio();
  pinMode(in, INPUT);
  pinMode(out, OUTPUT);
  for(int i = 0; i < 50; i++)
  {
    if(digitalRead(in) == 1)
    {
      digitalWrite(out, HIGH);
      printf("havaittu liiketta\n");
    }
    else {
      digitalWrite(out, LOW);
      printf("ei havaita liiketta\n");
    }
    delay (250);
  }
  return 0;
}
