
#define motorInterfaceType  1
#define STEPS_PER_TURN      200

#define B_ASCII  66
#define D_ASCII  68
#define F_ASCII  70
#define L_ASCII  76
#define R_ASCII  82
#define U_ASCII  85
#define AP_ASCII 39

typedef enum
{
  Clockwise = LOW,
  CounterClockwise = HIGH
} motor_direction_t;

typedef enum
{
  Green_Face = 0,
  Orange_Face,
  Red_Face,
  Blue_Face,
  White_Face,
  Yellow_Face
} Cube_Faces_t;

void turnMotor(motor_direction_t motor_direction, uint8_t motor_number);
void ExecuteSolution(char * Solution_string, uint8_t Move_number);

const byte numChars = 100;
char receivedChars[numChars];   // an array to store the received data

boolean newData = false;

// Step and direction pins of all motors
uint8_t Motor_Pins[6][2] = 
{
  {30, 31},
  {32, 33},
  {34, 35},
  {36, 37},
  {38, 39},
  {40, 41}
};

uint8_t Enable_Pins[6] = {7, 6, 5, 4, 3, 2};

void setup() {
  // put your setup code here, to run once:
  for (uint8_t i = 0; i < 6; i++)
  {
    pinMode(Motor_Pins[i][0], OUTPUT);
    pinMode(Motor_Pins[i][1], OUTPUT);
    pinMode(Enable_Pins[i], OUTPUT);
    digitalWrite(Enable_Pins[i], HIGH);
  }

  Serial.begin(9600);

}

void loop() {

  recvWithEndMarker();

  if (newData == true)
  {
    ExecuteSolution();
    newData = false;
  }

}

void turnMotor(motor_direction_t motor_direction, Cube_Faces_t Face)
{

  // Enable the corresponding motor
  digitalWrite(Enable_Pins[Face], LOW);

  // Set the Direction pin
  digitalWrite(Motor_Pins[Face][1], motor_direction);

  // Perform the steps
  for(int i = 0; i < STEPS_PER_TURN/4; i++)
  {   
    digitalWrite(Motor_Pins[Face][0], HIGH);       
    delay(1);          
    digitalWrite(Motor_Pins[Face][0], LOW);       
    delay(1);          
  }

  // Disable the motor
  digitalWrite(Enable_Pins[Face], HIGH);
  
}

void ExecuteSolution()
{
  uint8_t i = 0;
  
  while (i < numChars)
  {
    if (receivedChars[i] == F_ASCII)
    {
      if (receivedChars[i+1] == AP_ASCII)
      {
        turnMotor(CounterClockwise, Green_Face);
        delay (50);
        i+=2;
      }
      else
      {
        turnMotor(Clockwise, Green_Face);
        delay (50);
        i++;
      }
    }
    else if (receivedChars[i] == R_ASCII)
    {
      if (receivedChars[i+1] == AP_ASCII)
      {
        turnMotor(CounterClockwise, Red_Face);
        delay (50);
        i+=2;
      }
      else
      {
        turnMotor(Clockwise, Red_Face);
        delay (50);
        i++;
      }
    }
    else if (receivedChars[i] == L_ASCII)
    {
      if (receivedChars[i+1] == AP_ASCII)
      {
        turnMotor(CounterClockwise, Orange_Face);
        delay (50);
        i+=2;
      }
      else
      {
        turnMotor(Clockwise, Orange_Face);
        delay (50);
        i++;
      }
    }
    else if (receivedChars[i] == B_ASCII)
    {
      if (receivedChars[i+1] == AP_ASCII)
      {
        turnMotor(CounterClockwise, Blue_Face);
        delay (50);
        i+=2;
      }
      else
      {
        turnMotor(Clockwise, Blue_Face);
        delay (50);
        i++;
      }
    }
    else if (receivedChars[i] == U_ASCII)
    {
      if (receivedChars[i+1] == AP_ASCII)
      {
        turnMotor(CounterClockwise, White_Face);
        delay (50);
        i+=2;
      }
      else
      {
        turnMotor(Clockwise, White_Face);
        delay (50);
        i++;
      }
    }
    else if (receivedChars[i] == D_ASCII)
    {
      if (receivedChars[i+1] == AP_ASCII)
      {
        turnMotor(CounterClockwise, Yellow_Face);
        delay (50);
        i+=2;
      }
      else
      {
        turnMotor(Clockwise, Yellow_Face);
        delay (50);
        i++;
      }
    }
  }
}

void recvWithEndMarker(void) 
{
    static byte ndx = 0;
    char endMarker = '\n';
    char rc;
    
    while (Serial.available() > 0 && newData == false) 
    {
        rc = Serial.read();

        if (rc != endMarker) 
        {
            receivedChars[ndx] = rc;
            ndx++;
        }
        else 
        {
            ndx = 0;
            newData = true;
        }
    }
}
