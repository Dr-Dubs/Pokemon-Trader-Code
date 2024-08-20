// Choose your Pokemon set
#include "Gen2_Starters.h"

#include <SPI.h>
#include "Pokemon.h"
#include "Trade_Protocol_Gen2.h"

// Notes:
// Black - GND
// Yellow - 13 (CLK)
// Green - 12 (MISO)
// Blue - 11 (MOSI)

void setup(){
  Serial.begin(115200);

  SPI.begin();
  // SPI.beginTransaction(SPISettings(16384, MSBFIRST, SPI_MODE0));

  // Time has to be at least 16384 for clock signal to work
  SPI.beginTransaction(SPISettings(16384, MSBFIRST, SPI_MODE3)); 

}

void loop(){

  in = SPI.transfer(out);
  delay(d_t);

  // print_state();

  out = protocol_gen2(in);
}

void print_state(void){
  if (d_t > 10){
    Serial.print(trade_center_state);
    Serial.print(" ");
    Serial.print(in, HEX);
    Serial.print(" ");
    Serial.print(out, HEX);
    Serial.print("\n");
  }
}