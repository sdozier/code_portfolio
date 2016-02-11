import java.io.*;
import java.awt.image.*;
import javax.swing.JOptionPane;
import javax.swing.*;
import java.awt.event.*;
import java.awt.*;
public class World extends JPanel
{
   private int[][] world;
   private JLabel[][] label;
   private Snake snake;
   private int oldbackx, oldbacky, oldfrontx, oldfronty, frontx,fronty, eggx, eggy, dir, bomb;
   private ImageIcon apple, north, south, east, west, none, bad;
   private Timer t;
	

   public World()
   {
      String intro = "Use the arrow keys to move.";
      intro = intro + "\nEat apples to increase your score, but don't eat the gunky ones.";
      intro = intro + "\nApples you've captured will trail behind you. Don't crash into your tail!";
      JOptionPane.showMessageDialog(null, intro);
   
      String message = "Type the number next to the difficulty you want.";
      message = message + "\nVery easy: 200";
      message = message + "\nEasy: 150";
      message = message + "\nMedium: 100";
      message = message + "\nHard: 50";
      message = message + "\n\n Typing a number in-between will give you an in-between difficulty.";
      message = message + "\nOut of range inputs are accepted, but may be boring.";
   
      String diffinput = JOptionPane.showInputDialog(message);
      int difficulty=1;
      if(diffinput!=null){
         try{
            difficulty = Integer.parseInt(diffinput);
         }
         catch(NumberFormatException e) {
            JOptionPane.showMessageDialog(null, "Invalid input");
            System.exit(0);
         }
      }
      else{
         System.exit(0);
      }
   
      dir = 1;
      apple = new ImageIcon("apple.gif");
      north = new ImageIcon("north.gif");
      south = new ImageIcon("south.gif");
      east = new ImageIcon("east.gif");
      west = new ImageIcon("west.gif");
      none = new ImageIcon("0.gif");
      bad = new ImageIcon("gunky.gif");
      label = new JLabel[30][30];
      
      //setLayout(new BorderLayout());
      setLayout(new GridLayout(30,30));
      for(int a = 0; a < 30; a++)
         for(int b = 0; b < 30; b++)
         {
            label[a][b] = new JLabel();
            label[a][b].setIcon(none);
            label[a][b].setOpaque(true);
            label[a][b].setBackground(Color.white);
            add(label[a][b]);
         }
      snake = new Snake();
      eggx = (int)(Math.random()*20 +6);
      eggy = (int)(Math.random()*26);
      label[eggy][eggx].setIcon(apple);
    
      t = new Timer(difficulty, new Listener());
      t.start();
      addKeyListener(new Key());
      setFocusable(true);  
   	
      move();
   }
   private void movingtomanager()
   {
      frontx = snake.frontx();
      fronty = snake.fronty();
      
      try{
         switch(dir)
         {
            case 0: movingto(frontx,fronty-1);
               break;
            case 1: movingto(frontx+1,fronty);
               break;
            case 2: movingto(frontx,fronty+1);
               break;
            case 3: movingto(frontx-1,fronty);
               break;
         }
      }
      catch(ArrayIndexOutOfBoundsException e)
      {
         String message = "You hit a wall. :(\nScore: "+(snake.length()-4);
         /*System.out.println("You hit a wall. :(");
         System.out.println("Score: " + (snake.length()-4));*/
         JOptionPane.showMessageDialog(null, message);
         System.exit(0);
      }
   }
   private void movingto(int x,int y)
   {
      
      if(willGetEgg(x,y))
      {
         snake.gotegg(eggx,eggy);
         label[fronty][frontx].setIcon(apple);
         frontx = eggx;
         fronty = eggy;
         setFront();
         makeEgg();
      }
      else if(willCrash(x,y))
      {
         String message = "You crashed. :(\nScore: "+(snake.length()-4);
         JOptionPane.showMessageDialog(null, message);
         /*System.out.println("You crashed. ):");
         System.out.println("Score: " + (snake.length()-4));*/
         System.exit(0);
      }
      else
      {
         move();
      }
   }
   private void makeEgg()
   {
      do{
         eggx = (int)(Math.random()*30);
         eggy = (int)(Math.random()*30);
      }while((eggx == frontx && eggy == fronty)||label[eggy][eggx].getIcon()!=none);
      label[eggy][eggx].setIcon(apple);
   }
   private void makeBadApple()
   {
      int ax, ay;
      do{
         ax = (int)(Math.random()*30);
         ay = (int)(Math.random()*30);
      }while(label[ay][ax].getIcon()!=none || tooClose(ax,ay));
      label[ay][ax].setIcon(bad);
   }
   private boolean tooClose(int ax, int ay){
   //Try to avoid making a bomb where the user doesn't have time to avoid it
      int diffx = frontx-ax;
      int diffy = fronty-ay;
      return diffx<=4 && diffx>=-4 && diffy <=4 && diffy >=-4;
   }
   private boolean willCrash(int x, int y)
   {
      return label[y][x].getIcon()!=none;
   }
   private boolean willGetEgg(int x, int y)
   {
      return (eggx == x && eggy == y);
   }
   private void display()
   {
      /*Piece[] temp = snake.array();
      for(int a = 0; a < snake.length(); a++)
      {
         label[temp[a].getY()][temp[a].getX()].setIcon(apple);
      }*/
      label[oldfronty][oldfrontx].setIcon(apple);
      label[oldbacky][oldbackx].setIcon(none);
      setFront();
   }
   private void move()
   {
      oldbackx = snake.backx();
      oldbacky = snake.backy();
      oldfrontx = snake.frontx();
      oldfronty = snake.fronty();
      snake.move();
      display();
   }
   private void turn(int x)
   {
      snake.turn(x);
      display();
   }
   private void setFront()
   {
      switch(dir)
      {
         case 0: label[snake.fronty()][snake.frontx()].setIcon(north);
            break;
         case 1: label[snake.fronty()][snake.frontx()].setIcon(east);
            break;
         case 2: label[snake.fronty()][snake.frontx()].setIcon(south);
            break;
         case 3: label[snake.fronty()][snake.frontx()].setIcon(west);
            break;
      }
   }
   private class Key extends KeyAdapter
   {
      public void keyPressed(KeyEvent e)
      {
         if(e.getKeyCode() == KeyEvent.VK_UP)
         {
            if(dir != 2)
            {
               dir = 0;
               turn(0);
               //movingtomanager();
            }
         }
         if(e.getKeyCode() == KeyEvent.VK_DOWN)
         {
            if(dir != 0)
            {
               dir = 2;
               turn(2);
               //movingtomanager();
            }
         }
         if(e.getKeyCode() == KeyEvent.VK_LEFT)
         {
            if(dir != 1)
            {
               dir = 3;
               turn(3);
               //movingtomanager();
            }
         }
         if(e.getKeyCode() == KeyEvent.VK_RIGHT)
         {
            if(dir != 3)
            {
               dir = 1;
               turn(1);
               //movingtomanager();
            }
         }
      }
   }
   private class Listener implements ActionListener
   {
      public void actionPerformed(ActionEvent e)
      {
         movingtomanager();
         bomb++;
         if(bomb % 100 == 0)
         {
            makeBadApple();
         }
      }
   }

}