package back;

import front.Index;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;
import java.awt.Toolkit;
import java.awt.datatransfer.Clipboard;
import java.awt.datatransfer.StringSelection;

//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    static void main() {
        Index ventana = new Index();
        ventana.setVisible(true);
    }

    public static String rusdesk_codigo() {

        final String pathRustDesk = "C:\\Program Files\\RustDesk\\rustdesk.exe";
        final String[] comandos = {pathRustDesk, "--get-id", "|", "more"};
        File rustdeskApp = new File(pathRustDesk);

        // Si no existe la ruta finaliza el metodo
        if (!rustdeskApp.exists()){
            return "Problemas con RustDesk";
        }

        // Prueba de comnandos
        try {
            Process proceso = new ProcessBuilder(comandos).start();
            BufferedReader lector = new BufferedReader(new InputStreamReader(proceso.getInputStream()));

            String linea;
            String resultado = "";
            while ((linea = lector.readLine()) != null) {
                resultado=linea;
            }

            StringSelection seleccion = new StringSelection(resultado.replace("\n", ""));
            Clipboard portapapeles = Toolkit.getDefaultToolkit().getSystemClipboard();
            portapapeles.setContents(seleccion, null);

            return resultado.replace("\n", "");
        } catch (Exception e) {
            // throw new RuntimeException(e);
            System.out.println(e.getMessage());
            return "Error interno";
        }
    }
}
