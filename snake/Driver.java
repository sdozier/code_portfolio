   import javax.swing.JFrame;
    public class Driver
   {
       public static void main(String[] args)
      {
         JFrame frame=new JFrame("Snake");
         frame.setSize(700,700);
         frame.setLocation(50,50);
         frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
         frame.setContentPane(new World());
         frame.setVisible(true);
      }
   }