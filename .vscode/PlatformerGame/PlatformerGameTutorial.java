package PlatformerGame;
import java.awt.Dimension;
import java.awt.Toolkit;
import static javax.swing.WindowConstants.DISPOSE_ON_CLOSE;

public class PlatformerGameTutorial {
    public static void main(String[] args) {
        MainFrame frame = new MainFrame();
        frame.setSize(700, 700);
        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
        frame.setLocation((int)(screenSize.getWidth()/2-frame.getWidth()/2), (int)(screenSize.getHeight()/2-frame.getHeight()/2));
        frame.setResizable(false);
        frame.setTitle("Platformer Game");
        frame.setVisible(true);
        frame.setDefaultCloseOperation((DISPOSE_ON_CLOSE));
        
    }
}
