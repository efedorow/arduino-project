void setup() {
    // put your setup code here, to run once:
    Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int temp_meas = analogRead(A5);
  int pres_meas = analogRead(A0);
  float V1 = temp_meas*(5.0/1000.0);
  float V2 = pres_meas*(5.0/100000.0);
  //Serial.print(temp_meas);
  delay(500);
  float i1 = V1/1000.0;
  float R1 = (5.00-V1)/i1;
  
  float temp_C = ((R1/1000-1)/0.00385);


  
  float i2 = V2/100.0;
  float R2 = (5.00-V2)/i2;
  
   
  
  Serial.print("Temperature: ");
  Serial.print(temp_C);
  
  Serial.print("  Resistance: ");
  Serial.println(R2);
  
}
