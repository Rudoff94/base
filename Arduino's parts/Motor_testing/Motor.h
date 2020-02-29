#define FORWARD 1
#define BACKWARD 0
class Motor
{
  private:
    int port1;
    int port2;
    int power;
  public:
    Motor()
    {
      power = 0;
      port1 = -1;
      port2 = -1;
    }
    void setup(int port1_, int port2_)
    {
      port1 = port1_;
      port2 = port2_;
      pinMode(port1, OUTPUT);
      pinMode(port2, OUTPUT);
    }
    
    void setMotor(bool dir, int _power)
    {
      if (dir == FORWARD)
      {
        power = _power;
        digitalWrite(port2, 0);
        analogWrite(port1, power);
      }
      else
      {
        power = _power;
        digitalWrite(port1, 0);
        analogWrite(port2, power);
      }
    }

};
