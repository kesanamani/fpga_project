int c = 0;
int arr[256];
void setup() {
pinMode(2, INPUT);
pinMode(3, INPUT); 
pinMode(4, INPUT); 
pinMode(5, INPUT); 
pinMode(6, INPUT); 
pinMode(7, INPUT); 
pinMode(8, INPUT); 
pinMode(9, INPUT);
pinMode(10,INPUT);
pinMode(11,INPUT);
pinMode(12,INPUT);
pinMode(22,INPUT);
pinMode(23,INPUT);
pinMode(24,INPUT);
pinMode(25,INPUT);
pinMode(26,INPUT);
  
pinMode(27,INPUT);

//pinMode(13, OUTPUT);
//pinMode(12, OUTPUT);
//pinMode(11, OUTPUT);
//pinMode(10, OUTPUT);
Serial.begin(9600);
}

void loop(){
// read the state of the pushbutton value:
//int a = Serial.parseInt();
//digitalWrite(13,a%2);
//a = (a>>1);
//digitalWrite(12,a%2);
//a = (a>>1);
//digitalWrite(11,a%2);
//a = (a>>1);
//digitalWrite(10,a%2);
//a = (a>>1);
int sig = digitalRead(30);
//Serial.println(sig);
if(sig == 1){
int z0 = digitalRead(2);
int z1 = digitalRead(3);
int z2 = digitalRead(4);
int z3 = digitalRead(5);
int z4 = digitalRead(6);
int z5 = digitalRead(7);
int z6 = digitalRead(8);
int z7 = digitalRead(9);
int z8 = digitalRead(10);
int z9 = digitalRead(11);
int z10 = digitalRead(12);
int z11 = digitalRead(22);
int z12 = digitalRead(23);
int z13 = digitalRead(24);
int z14 = digitalRead(25);
int z15 = digitalRead(26);
int z16 = digitalRead(27);
int z17 = digitalRead(28);
int z18 = digitalRead(29);

Serial.print(z18);
Serial.print(z17);
Serial.print(z16);
Serial.print(z15);
Serial.print(z14);
Serial.print(z13);
Serial.print(z12);
Serial.print(z11);
Serial.println(z10);
//Serial.print(z9);
//Serial.print(z8);
//Serial.print(z7);
//Serial.print(z6);
//Serial.print(z5);
//Serial.print(z4);
//Serial.print(z3);
//Serial.print(z2);
//Serial.print(z1);
//Serial.println(z0);
//int no = (z15<<15)+(z14<<14)+(z13<<13)+(z12<<12)+(z11<<11)+(z10<<10)+(z9<<9)+(z8<<8)+(z7<<7)+(z6<<6)+(z5<<5)+(z4<<4)+(z3<<3)+(z2<<2)+(z1<<1)+z0;
//arr[no]++;
//Serial.println(no);
}
//if(Serial.available() && c == 0)
//{
//  for(int i = 0;i<256;i++)
//  {
//    Serial.println(arr[i]);
//  }
//  c++;
//}
//delay(20);
}
