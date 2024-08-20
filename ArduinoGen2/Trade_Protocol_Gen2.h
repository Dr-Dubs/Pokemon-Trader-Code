connection_state_t connection_state = NOT_CONNECTED;
trade_center_state_t trade_center_state = INIT;
int counter = 0;

byte in = 0x00;
byte out = 0x01;

byte random_data[10] = {0x95, 0xDE, 0xCC, 0xB9, 0x90, 0x7A, 0x63, 0x4B, 0x32, 0x69} ;
int d_t = 5;
byte poke_select;

int trade_pokemon = -1;
int poke = 0;
int trainer = 0;
int nickname = 0;
int trade_pokemon2 = -1;
int poke2 = 0;
int trainer2 = 0;
int nickname2 = 0;
int end = 0;


byte protocol_gen2(byte in) {

  switch (connection_state) {

    case NOT_CONNECTED:

      if (in == 0x02) {
        // Confirmation bytes
        d_t = 16;
        SPI.transfer(0x00);
        delay(16);
        SPI.transfer(0x00);
        delay(16);

        // Pause for save
        delay(6000);

        // Sync after save
        out = 0x61;

      }

      else if (in == 0x61) {
        for (int i = 0; i < 13; i++) {
          SPI.transfer(0x61);
          delay(16);
        }

        out = 0x00;

      }

      else if (in == 0xD1) {
        SPI.transfer(0xD1);
        delay(16);
        SPI.transfer(0xD1);
        delay(16);
        connection_state = TRADE_CENTER;
        out = 0x00;
      }

      break;


    case TRADE_CENTER:


      if (trade_center_state == INIT) {
        // d_t = 100;
        if (in == 0x00) {
          out = 0x75;
        }

        else if (in == 0x70) {
          out = 0x70;
        }

        else if (in == 0x71) {
          out = 0x71;
        }

        else if (in == 0x72) {
          out = 0x72;
        }

        else if (in == 0x75) {
          trade_center_state = READY_TO_GO;
          out = 0x00;
        }
      }

      else if (trade_center_state == READY_TO_GO) {

        if (in == 0x00) {
          out = 0x76;
        }

        else if (in == 0x76) {
          trade_center_state = SEEN_FIRST_WAIT;
          out = 0x00;
        }
      }

      else if (trade_center_state == SEEN_FIRST_WAIT) {

        if (in == 0x00) {
          SPI.transfer(0x00);
          delayMicroseconds(300);
          SPI.transfer(0x00);
          delayMicroseconds(300);
          out = 0xFD;
        }

        else if (in == 0xFD) {
          trade_center_state = SENDING_RANDOM_DATA;
          // out = 0xFB;
        }
      }

      else if (trade_center_state == SENDING_RANDOM_DATA) {

        for (int i = 0; i < 10; i++) {
          SPI.transfer(random_data[i]);
          delayMicroseconds(300);
        }

        if (in == 0xFD) {
          trade_center_state = WAITING_TO_SEND_DATA;
          out = 0xFD;
        }
      }

      else if (trade_center_state == WAITING_TO_SEND_DATA) {
        if (in == 0xFD) {
          trade_center_state = SENDING_DATA;
          out = 0xFD;
        }
      }

      else if (trade_center_state == SENDING_DATA) {
        for (int i = 0; i < 5; i++) {
          SPI.transfer(0xFD);
          delayMicroseconds(300);
        }
        
        for (int i = 0; i < PLAYER_LENGTH_GEN_II; i++) {
          INPUT_BLOCK_GEN_II[i] = SPI.transfer(poke_arr[i]);
          delayMicroseconds(300);
        }

        trade_center_state = SENDING_PATCH_DATA;
        counter = 0;
        out = 0xFD;
      }

      else if (trade_center_state == SENDING_PATCH_DATA) {

        // out = 0xFE;
        if (in == 0x00){
          for (int i = 0; i < 7; i++) {
            SPI.transfer(0x00);
            delayMicroseconds(300);
          }
          SPI.transfer(0xFF);
          delayMicroseconds(300);
          SPI.transfer(0xFF);
          delayMicroseconds(300);
        }

        else if (in == 0xFE){
          // out = 0xFE;
          trade_center_state = TRADE_PENDING;
        }
      }

      else if (trade_center_state == TRADE_PENDING) {
        d_t = 100;

        if (in == 0x7F || in == 0x76) {  // Canceled or trade complete
          out = 0x7F;
          trade_center_state = INIT;
        }
        
        else if (in >= 0x70 && in <= 0x75) {  // Pokemon selected

          // store the slot, change the poke_arr
          d_t = 100;

          // Serial.print(in, HEX);
          // Serial.print("\n");
          poke_select = in;
          trade_pokemon = (poke_select - 0x70);
          poke = 21 + 48 * trade_pokemon;
          trainer = 21 + 48 * 6 + 11 * trade_pokemon;
          nickname = 21 + 48 * 6 + 11 * 6 + 11 * trade_pokemon;
          // delay(1000);

          // In case the generated party is smaller
          if (trade_pokemon > poke_arr[11]) {
            trade_pokemon2 = poke_arr[11] - 1;
            out = 0x70 + trade_pokemon2;
          }
          else {
            out = poke_select;
            trade_pokemon2 = trade_pokemon;
          }

          poke2 = 21 + 48 * trade_pokemon2;
          trainer2 = 21 + 48 * 6 + 11 * trade_pokemon2;
          nickname2 = 21 + 48 * 6 + 11 * 6 + 11 * trade_pokemon2;

          for (int i = 0; i < 5; i++){
            SPI.transfer(out);
            delay(d_t);
          }
          SPI.transfer(0x00);
          delay(d_t);
          SPI.transfer(0x00);
          delay(d_t);

          trade_center_state = TRADE_INIT;
        }

        else if (in == 0xFE) {
          // trade_center_state = TRADE_CONFIRMATION;
          out = 0xFE;
        } else if (in == 0x00) {
          out = 0x00;
        } else if (in == poke_select) {
          out = poke_select;
        }
      }

      else if (trade_center_state == TRADE_INIT){
        out = in;
        if (in == 0xFE){
          trade_center_state = TRADE_CONFIRMATION;
        }
      }

      else if (trade_center_state == TRADE_CONFIRMATION) {

        if (in == 0x72) {  // Confirmed trade
          trade_center_state = DONE;
          out = 0x72;

          // Only works for first in party!!
          // Need to adapt the poke_arr index values

          poke_arr[12 + trade_pokemon2] = INPUT_BLOCK_GEN_II[12 + trade_pokemon];  // preamble line

          for (int i = 0; i <= 48; i++) {  // pokemon data
            poke_arr[poke2 + i] = INPUT_BLOCK_GEN_II[poke + i];
          }

          for (int i = 0; i <= 11; i++) {  // trainer name and nickname
            poke_arr[trainer2 + i] = INPUT_BLOCK_GEN_II[trainer + i];
            poke_arr[nickname2 + i] = INPUT_BLOCK_GEN_II[nickname + i];
          }

        }

        else if (in == 0x71) {  // Cancel trade, be careful going to patch data with 0x71
          trade_center_state = TRADE_CANCELED;
          out = 0x71;
          //out = 0x00;
        }

      }

      else if (trade_center_state == TRADE_CANCELED) {
        if (in != 0x71) {
          trade_center_state = SENDING_PATCH_DATA;
          out = 0x00;
        }
      }

      else if (trade_center_state == DONE) {
        // delay(10000);
        d_t = 100;
        if (in == 0xFE) {
          trade_center_state = INIT;
          out = 0xFE;
        } else if (in == 0x00) {
          out = 0x00;
        }
      }
  }

  return out;
}