#include <SoftwareSerial.h>
#include <Servo.h> // Inclui a biblioteca do servo

SoftwareSerial mySerial(12, 13); // RX, TX

Servo servo; // define o nome do servo
Servo garra;

int valores[5] = {};
int total = 0;
int pos = 0;
int media;
int mao = 0; // 0 - aberta, 1 - fechada

String height = "";
char c;
int altura, val;

int convert (String height);

void setup() {
  // Open serial communications and wait for port to open:
  Serial.begin(9600);

  Serial.println("Conectado");

  // set the data rate for the SoftwareSerial port
  mySerial.begin(9600);

  servo.attach(13);
  servo.write(145); // 67 - 145

  garra.attach(A0);
  garra.write(50); // 105 - 50

}

void loop() { // run over and over
  if (mySerial.available()) {
     c = mySerial.read();
     if (c == ')'){ // Abre
      garra.write(50);
      mao = 0;
     }
     else if(c == '('){ // Fecha
      garra.write(105);
      mao = 1;
      }
      else{
     
     if (c!='*') height += c;
     else{
      //height += '*';
      altura = convert(height);
      height = "";
      if (mao == 0){ //mão aberta
        altura = ceil(altura*0.75);
      }
      //Serial.print(altura);
      //Serial.print ("  -  ");
      val = map(altura, 70, 300, 50,107);

      /*valores[pos++] = val;
      if (pos == 5){
        pos = 0;
        media = mediaVetor(valores,5);*/
        media = val;
        if (media >= 67 and media <= 145) servo.write(media);
        Serial.println(media);
      //}
     }
    }
  }
}

int convert (String height){

  int altura = 0;
  
  for (int i = 0; height[i] != '\0'; i++){
    altura = altura*10;
    altura += height[i] - '0';
  }

  return altura;
}

int mediaVetor(int vet[], int tam){
  int media, soma = 0;
  int i;

  for(i =0; i<tam; i++){
    soma = soma + vet[i];
  }
  media = soma/tam;

  return media;
}
