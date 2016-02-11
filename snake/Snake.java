   import javax.swing.*;
   import java.awt.*;
    public class Snake
   {
      private int myLength;
      private Piece[] piece;
      private int front;
      private int back;
      private int oldback;
      private int direction; //0 = north, 1=east, 2=south, 3=west
       public Snake()
      {
         myLength = 4;
         piece = new Piece[4];
         for(int k = 0; k < 4; k++)
         {
            piece[k] = new Piece(k,29);
         }
         direction = 1;
         front = 3;
         back = 0;
      }
       public void gotegg(int x, int y)
      {
         myLength++;
         Piece temp[] = new Piece[myLength];
         
         if(back == 0)
         {
            for(int k = 0; k < myLength - 1; k++)
            {
               temp[k] = piece[k];
            }
         }
         else
         {
            int a = 0;
            for(int k = back; k <= myLength-2; k++)
            {
               temp[a] = piece[k];
               a++;
            }
            for(int k = 0; k < back; k++)
            {
               temp[a] = piece[k];
               a++;
            }
         }
         temp[myLength-1] = new Piece(x, y);
      	
         back = 0;
         front = myLength-1;
         piece = temp;
      }
       public Piece[] array()
      {
         return piece;
      }
       public int length()
      {
         return myLength;
      }
       public int backx()
      {
         return piece[back].getX();
      }
       public int backy()
      {
         return piece[back].getY();
      }
       public int frontx()
      {
         return piece[front].getX();
      }
       public int fronty()
      {
         return piece[front].getY();
      }
       public void move()
      {
      
         switch(direction)
         {
            case 0: piece[back].setPlace(piece[front].getX(),piece[front].getY()-1);
               break;
            case 1: piece[back].setPlace(piece[front].getX()+1,piece[front].getY());
               break;
            case 2: piece[back].setPlace(piece[front].getX(),piece[front].getY()+1);
               break;
            case 3: piece[back].setPlace(piece[front].getX()-1, piece[front].getY());
               break;
         }
         
         front = back;
         if(front < myLength - 1)
            back++;
         else
            back = 0;
      }
      
       public void turn(int d)
      {
         direction = d;
      }
   }