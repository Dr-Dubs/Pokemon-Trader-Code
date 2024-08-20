// Celebi (Lv. 30), Mew, Mewtwo, and Celebi (Lv. 5)

#include <stdint.h>

#define PLAYER_LENGTH_GEN_II 444	//11+8+2+(48*6)+(11*6)+(11*6)+3

uint8_t INPUT_BLOCK_GEN_II[PLAYER_LENGTH_GEN_II];

uint8_t poke_arr[PLAYER_LENGTH_GEN_II] = {
  0x87, 0x80, 0x82, 0x8A, 0x84, 0x91, 0x50, 0x00, 0x00, 0x00, 0x00, // name
  0x4, 0xfb, 0x97, 0x96, 0xfb, 0xFF, 0xFF, 0xFF, 
  0x0, 0x0, 
    // 6 pokemon
    //spc Held  mv1   mv2   mv3   mv4   OT ID       exp.              HP_EV       Attack_EV   Def_EV      Speed_EV    Special_EV  IV_Data     m1pp  m2pp  m3pp  m4pp  frnd  virus cght_data   lvl   sat.  N/A   curr_HP     max_HP      attack      defence     speed       spcl_att    spcl_def
  0xfb, 0x0, 0xd7, 0xdb, 0xf6, 0xf8, 0x0, 0x0, 0x0, 0x55, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x2e, 0x37, 0x5, 0x19, 0x5, 0xf, 0x46, 0x0, 0x0, 0x0, 0x1e, 0x0, 0x0, 0x0, 0x65, 0x0, 0x65, 0x0, 0x42, 0x0, 0x49, 0x0, 0x42, 0x0, 0x45, 0x0, 0x45, 
  0x97, 0x0, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x87, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x56, 0x86, 0x23, 0x0, 0x0, 0x0, 0x46, 0x0, 0x0, 0x0, 0x5, 0x0, 0x0, 0x0, 0x19, 0x0, 0x19, 0x0, 0xf, 0x0, 0xf, 0x0, 0xf, 0x0, 0xf, 0x0, 0xf, 
  0x96, 0x0, 0xf4, 0xf8, 0x36, 0x5e, 0x0, 0x0, 0x6, 0x8a, 0xce, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x2e, 0x19, 0xa, 0xf, 0x1e, 0xa, 0x46, 0x0, 0x0, 0x0, 0x46, 0x0, 0x0, 0x0, 0xe8, 0x0, 0xe8, 0x0, 0xa1, 0x0, 0x96, 0x0, 0xbc, 0x0, 0xe9, 0x0, 0x8f, 
  0xfb, 0x0, 0x49, 0x5d, 0xd7, 0x69, 0x0, 0x0, 0x0, 0x0, 0x87, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x11, 0x1, 0xa, 0x19, 0x5, 0x14, 0x46, 0x0, 0x0, 0x0, 0x5, 0x0, 0x0, 0x0, 0x1a, 0x0, 0x1a, 0x0, 0xf, 0x0, 0xf, 0x0, 0xf, 0x0, 0xf, 0x0, 0xf, 
  0xd8, 0x0, 0xa, 0x2b, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x7d, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0xfb, 0xe2, 0x23, 0x1e, 0x0, 0x0, 0x46, 0x0, 0x0, 0x0, 0x5, 0x0, 0x0, 0x0, 0x16, 0x0, 0x16, 0x0, 0xe, 0x0, 0xb, 0x0, 0xa, 0x0, 0xa, 0x0, 0xa, 
  0xe2, 0x0, 0x21, 0x91, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x9c, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x78, 0x4b, 0x23, 0x1e, 0x0, 0x0, 0x46, 0x0, 0x0, 0x0, 0x5, 0x0, 0x0, 0x0, 0x16, 0x0, 0x16, 0x0, 0x9, 0x0, 0xc, 0x0, 0xc, 0x0, 0xe, 0x0, 0x14, 
    // 6 trainer names
  0x87, 0x80, 0x82, 0x8A, 0x84, 0x91, 0x50, 0x00, 0x00, 0x00, 0x00,
  0x87, 0x80, 0x82, 0x8A, 0x84, 0x91, 0x50, 0x00, 0x00, 0x00, 0x00,
  0x87, 0x80, 0x82, 0x8A, 0x84, 0x91, 0x50, 0x00, 0x00, 0x00, 0x00,
  0x87, 0x80, 0x82, 0x8A, 0x84, 0x91, 0x50, 0x00, 0x00, 0x00, 0x00,
  0x87, 0x80, 0x82, 0x8A, 0x84, 0x91, 0x50, 0x00, 0x00, 0x00, 0x00,
  0x87, 0x80, 0x82, 0x8A, 0x84, 0x91, 0x50, 0x00, 0x00, 0x00, 0x00,
    // 6 nicknames
  0x82, 0x84, 0x8b, 0x84, 0x81, 0x88, 0x50, 0x50, 0x50, 0x50, 0x50, 
  0x8c, 0x84, 0x96, 0x50, 0x50, 0x50, 0x50, 0x50, 0x50, 0x50, 0x50, 
  0x8c, 0x84, 0x96, 0x93, 0x96, 0x8e, 0x50, 0x50, 0x50, 0x50, 0x50, 
  0x82, 0x84, 0x8b, 0x84, 0x81, 0x88, 0x50, 0x50, 0x50, 0x50, 0x50, 
  0x93, 0x84, 0x83, 0x83, 0x88, 0x94, 0x91, 0x92, 0x80, 0x50, 0x50, 
  0x8c, 0x80, 0x8d, 0x93, 0x88, 0x8d, 0x84, 0x50, 0x50, 0x50, 0x50, 
  // 2 useless bytes??
  0x00, 0x00, 0x00
};
