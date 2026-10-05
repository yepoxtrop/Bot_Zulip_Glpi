package front;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import back.Main;


public class Index extends JFrame{
    private JPanel panelPrincipal;
    private JPanel panelTitulo;
    private JLabel espacioCodigo;
    private JPanel panelCodigo;
    private JButton generarCódigoButton;
    private JPanel panelBoton;

    public Index(){
        iniciarIndex();

        generarCódigoButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                espacioCodigo.setText(Main.rusdesk_codigo());
            }
        });
    }

    public void iniciarIndex(){
        setContentPane(panelPrincipal);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(600,200);
        setResizable(false);
        setLocationRelativeTo(null); // Centrar pantalla
        setTitle("Código Rustdesk");
        setIconImage(getIconImage());
    }

    @Override
    public Image getIconImage() {
        // Carga la imagen desde la carpeta de recursos o src
        return Toolkit.getDefaultToolkit().getImage(
                ClassLoader.getSystemResource("src/main/java/front/media/image.ico")
        );
    }
}
