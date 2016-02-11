   import javax.swing.*;
   import java.awt.*;

    public class Piece
   {
      private int myX;
      private int myY;
       public Piece(int x, int y)
      {
         myX = x;
       myY = y;
      }
       public void setPlace(int x, int y)
      {
         myX = x;
         myY = y;
      }
       public int getX()
      {
         return myX;
      }
       public int getY()
      {
         return myY;
      }
   }