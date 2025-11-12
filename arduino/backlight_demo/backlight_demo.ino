
#include <FastLED.h>

#define NUM_LEDS 24 
#define DATA_PIN 30
CRGB leds[NUM_LEDS];

void setup() { 
  Serial.begin(57600);
  Serial.println("resetting");
  LEDS.addLeds<WS2812,DATA_PIN,RGB>(leds,NUM_LEDS);
  LEDS.setBrightness(60);

  pinMode(48, OUTPUT);
  pinMode(49, OUTPUT);
  pinMode(50, OUTPUT);
  pinMode(51, OUTPUT);  

  pinMode(29, INPUT);
  pinMode(28, INPUT);
  pinMode(15, INPUT);
  pinMode(16, INPUT); 
}


void loop() { 
  
  if (digitalRead(29) == HIGH) 
  {
    digitalWrite(51,HIGH);
    lamps();
  } else {
    digitalWrite(51,LOW);
  }

  if (digitalRead(15) == HIGH) 
  { 
    offlamps();  
  }

  if (digitalRead(15) == HIGH) digitalWrite(50,HIGH); else digitalWrite(50,LOW);
  if (digitalRead(28) == HIGH) digitalWrite(49,HIGH); else digitalWrite(49,LOW);
  if (digitalRead(16) == HIGH) digitalWrite(48,HIGH); else digitalWrite(48,LOW);    

 
}

void offlamps() { 
  for(int i = 0; i < NUM_LEDS; i++) { 
    leds[i] = CHSV(0, 0, 0); 
    FastLED.show();
    delay(1);
    } 
}


void lamps() {
    static uint8_t hue = 0; 
  for(int i = 0; i < NUM_LEDS; i++) {
    leds[i] = CHSV(hue++, 200, 255);
    FastLED.show(); 
    fadeall();
    delay(30);
  }
}

void fadeall() { for(int i = 0; i < NUM_LEDS; i++) { leds[i].nscale8(230); } }
