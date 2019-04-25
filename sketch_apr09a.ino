
int i = 0;

void setup() {
//pinMode(2, INPUT);
//pinMode(3, INPUT); 
//pinMode(4, INPUT); 
//pinMode(5, INPUT); 
//pinMode(6, INPUT); 
//pinMode(7, INPUT); 
//pinMode(8, INPUT); 
//pinMode(9, INPUT);
//pinMode(13, OUTPUT);
//pinMode(12, OUTPUT);
//pinMode(11, OUTPUT);
//pinMode(10, OUTPUT);
pinMode(2, OUTPUT);
pinMode(3, OUTPUT); 
pinMode(4, OUTPUT); 
pinMode(5, OUTPUT);
pinMode(6, OUTPUT);
pinMode(7, OUTPUT);
pinMode(8, OUTPUT);
pinMode(9, OUTPUT);
pinMode(10, OUTPUT);
pinMode(11, OUTPUT);
pinMode(12, OUTPUT);
Serial.begin(9600);
}

void loop(){
  digitalWrite(11,0);
// read the state of the pushbutton value:
if(Serial.available()){
 // delay(100);
//{i++;
//  if(i==9)
//  {i =0;
//  delay(300);}

int a = Serial.parseInt();
Serial.println(a);
if(a==-1)
{
  digitalWrite(12,1);
}
else if(a==-2)
{
  digitalWrite(12,0);
}
else
{
  digitalWrite(2,a%2);
  a = (a>>1);
  digitalWrite(3,a%2);
  a = (a>>1);
  digitalWrite(4,a%2);
  a = (a>>1);
  digitalWrite(5,a%2);
  a = (a>>1);
  digitalWrite(6,a%2);
  a = (a>>1);
  digitalWrite(7,a%2);
  a = (a>>1);
  digitalWrite(8,a%2);
  a = (a>>1);
  digitalWrite(9,a%2);
  a = (a>>1);
  digitalWrite(10,a%2);
  a = (a>>1);
}
digitalWrite(11,1);
delay(1);
}

}
