package Grafico; // Paket für die grafische Benutzeroberfläche

import java.awt.Color; // Farbeinstellungen für Komponenten
import java.awt.EventQueue; // Hilfsklasse für die Ereignisverarbeitung
import java.awt.Font; // Einstellungen für Schriftart und -größe
import java.awt.event.ActionEvent; // Klasse für ausgelöste Ereignisse
import java.awt.event.ActionListener; // Interface für die Ereignisbehandlung

import javax.swing.JButton; // Schaltflächen für die Eingabe
import javax.swing.JFrame; // Hauptfenster der Anwendung
import javax.swing.JPanel; // Bereich für die Gruppierung von Komponenten
import javax.swing.JTextField; // Textfeld zur Anzeige von Ergebnissen
import javax.swing.SwingConstants; // Ausrichtung von Text im Textfeld
import javax.swing.border.EmptyBorder; // Rand für den contentPane

public class Calculadora extends JFrame { // Hauptklasse für die Rechner-Anwendung

	private JPanel contentPane; // Hauptbereich für Komponenten
	private JTextField txtPantalla; // Textfeld zur Anzeige

	// ----------------------------------------
	// VARIABLES (Variablen für die Berechnung)
	// ----------------------------------------
	double numero1; // Erster Operand
	double numero2; // Zweiter Operand
	double resultado; // Ergebnis der Berechnung
	String operacion; // Speichert die ausgewählte Operation

	// ----------------------------------------
	// Hauptmethode, Startpunkt der Anwendung
	// ----------------------------------------
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() { // Ausführen in der Event-Dispatch-Thread
			public void run() {
				try {
					Calculadora frame = new Calculadora(); // Erzeugen des Rechnerfensters
					frame.setVisible(true); // Fenster anzeigen
				} catch (Exception e) { // Fehlerbehandlung
					e.printStackTrace();
				}
			}
		});
	}

	// --------------------------------------------------------------------
	// Konstruktor, erstellt die grafische Oberfläche der Rechner-Anwendung
	// --------------------------------------------------------------------
	public Calculadora() {

		setTitle("Calculator"); // Titel des Fensters
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // Anwendung beenden beim Schließen des Fensters
		setBounds(100, 100, 251, 360); // Größe und Position des Fensters
		contentPane = new JPanel(); // Hauptbereich erzeugen
		contentPane.setBackground(new Color(224, 255, 255)); // Hintergrundfarbe
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5)); // Ränder hinzufügen
		setContentPane(contentPane); // Hauptbereich setzen
		contentPane.setLayout(null); // Keine vordefinierte Layout-Verwaltung

		// ----------------------------------------------------
		// TEXTFELD (Erstellen und Positionieren des Textfelds)
		// ----------------------------------------------------
		txtPantalla = new JTextField();
		txtPantalla.setHorizontalAlignment(SwingConstants.RIGHT); // Rechtsbündige Ausrichtung
		txtPantalla.setFont(new Font("Arial", Font.BOLD, 18)); // Schriftart und -größe
		txtPantalla.setBounds(10, 11, 208, 42); // Position und Größe
		contentPane.add(txtPantalla); // Zum Hauptbereich hinzufügen
		txtPantalla.setColumns(10); // Anzahl der Spalten

		// ------------------------------------------------
		// Erstellen eines Buttons mit der Beschriftung "C"
		// ------------------------------------------------
		JButton btnLimpiar = new JButton("C");

		btnLimpiar.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				txtPantalla.setText(""); // Textfeld "txtPantalla" leeren, wenn der Button "C" geklickt wird
			}
		}); // Hinzufügen eines ActionListeners zum Button, um auf Klicks zu reagieren

		// Legt die Vordergrundfarbe des "Löschen"-Knopfes auf Rot fest.
		btnLimpiar.setForeground(new Color(255, 0, 0)); // Rot
		// Stellt Schriftart und -größe für den "Löschen"-Knopf ein.
		btnLimpiar.setFont(new Font("Arial", Font.BOLD, 17)); // Arial, fett, Größe 17

		// Positioniert den "Löschen"-Knopf im Layout und legt seine Größe fest.
		btnLimpiar.setBounds(163, 64, 57, 42); // x, y, Breite, Höhe

		// Fügt den "Löschen"-Knopf zum Hauptbereich des Fensters hinzu.
		contentPane.add(btnLimpiar);

		// -------------------------------------
		// --- Beispiel für eine Zahlentaste ---
		// -------------------------------------

		// Erstellt einen neuen Knopf mit der Beschriftung "3".
		JButton btn3 = new JButton("3");

		// Fügt einen ActionListener hinzu, der bei Klick auf den Knopf reagiert.
		btn3.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				// NUMMER 3 // Kommentar (nicht Teil des Codes)

				// Liest den aktuellen Text aus dem Anzeigefeld und hängt die "3" an.
				String IngreseNumero = txtPantalla.getText() + btn3.getText();

				// Aktualisiert das Anzeigefeld mit dem neuen Text.
				txtPantalla.setText(IngreseNumero);
			}
		});
		// Stellt Schriftart und -größe für den Knopf ein.
		btn3.setFont(new Font("Arial", Font.BOLD, 18)); // Arial, fett, Größe 18

		// Positioniert den Knopf im Layout und legt seine Größe fest.
		btn3.setBounds(120, 117, 45, 36); // x, y, Breite, Höhe

		// Fügt den Knopf zum Hauptbereich des Fensters hinzu.
		contentPane.add(btn3);

		// --------------------------------------------------------------------------------
		// --- Weitere Zahlentasten (2, 1, 6, 5, 4, 9, 8, 7) folgen dem gleichen Muster
		// ---
		// --------------------------------------------------------------------------------
		JButton btn2 = new JButton("2");
		btn2.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				// NUMERO 2

				String IngreseNumero = txtPantalla.getText() + btn2.getText();
				txtPantalla.setText(IngreseNumero);
			}
		});
		btn2.setFont(new Font("Arial", Font.BOLD, 18));
		btn2.setBounds(65, 117, 45, 36);
		contentPane.add(btn2);

		JButton btn1 = new JButton("1");
		btn1.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				// NUMERO 1
				String IngreseNumero = txtPantalla.getText() + btn1.getText();
				txtPantalla.setText(IngreseNumero);

			}
		});
		btn1.setFont(new Font("Arial", Font.BOLD, 18));
		btn1.setBounds(10, 117, 45, 36);
		contentPane.add(btn1);

		JButton btn6 = new JButton("6");
		btn6.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				// NUMERO 6
				String IngreseNumero = txtPantalla.getText() + btn6.getText();
				txtPantalla.setText(IngreseNumero);
			}
		});
		btn6.setFont(new Font("Arial", Font.BOLD, 18));
		btn6.setBounds(120, 164, 45, 36);
		contentPane.add(btn6);

		JButton btn5 = new JButton("5");
		btn5.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				// NUMERO 5
				String IngreseNumero = txtPantalla.getText() + btn5.getText();
				txtPantalla.setText(IngreseNumero);
			}
		});
		btn5.setFont(new Font("Arial", Font.BOLD, 18));
		btn5.setBounds(65, 164, 45, 36);
		contentPane.add(btn5);

		JButton btn4 = new JButton("4");
		btn4.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				// NUMERO 4
				String IngreseNumero = txtPantalla.getText() + btn4.getText();
				txtPantalla.setText(IngreseNumero);
			}
		});
		btn4.setFont(new Font("Arial", Font.BOLD, 18));
		btn4.setBounds(10, 164, 45, 36);
		contentPane.add(btn4);

		JButton btn9 = new JButton("9");
		btn9.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				// NUMERO 9
				String IngreseNumero = txtPantalla.getText() + btn9.getText();
				txtPantalla.setText(IngreseNumero);
			}
		});
		btn9.setFont(new Font("Arial", Font.BOLD, 18));
		btn9.setBounds(120, 211, 45, 36);
		contentPane.add(btn9);

		JButton btn8 = new JButton("8");
		btn8.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				// NUMERO 8
				String IngreseNumero = txtPantalla.getText() + btn8.getText();
				txtPantalla.setText(IngreseNumero);
			}
		});
		btn8.setFont(new Font("Arial", Font.BOLD, 18));
		btn8.setBounds(65, 211, 45, 36);
		contentPane.add(btn8);

		JButton btn7 = new JButton("7");
		btn7.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				// NUMERO 7
				String IngreseNumero = txtPantalla.getText() + btn7.getText();
				txtPantalla.setText(IngreseNumero);
			}
		});
		btn7.setFont(new Font("Arial", Font.BOLD, 18));
		btn7.setBounds(10, 211, 45, 36);
		contentPane.add(btn7);

		JButton btnCero = new JButton("0");
		btnCero.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				// CERO
				String IngreseNumero = txtPantalla.getText() + btnCero.getText();
				txtPantalla.setText(IngreseNumero);
			}
		});
		btnCero.setFont(new Font("Arial", Font.BOLD, 18));
		btnCero.setBounds(63, 258, 45, 36);
		contentPane.add(btnCero);

		JButton btnPunto = new JButton(".");
		btnPunto.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				// PUNTO
				String IngreseNumero = txtPantalla.getText() + btnPunto.getText();
				txtPantalla.setText(IngreseNumero);
			}
		});
		btnPunto.setForeground(new Color(255, 0, 0));
		btnPunto.setFont(new Font("Arial", Font.BOLD, 23));
		btnPunto.setBounds(8, 258, 45, 36);
		contentPane.add(btnPunto);

		// -----------------------------------------
		// --- Beispiel für eine Operationstaste ---
		// -----------------------------------------
		JButton btnSuma = new JButton("+");
		btnSuma.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				// Liest die erste Zahl aus dem Anzeigefeld und speichert sie.
				numero1 = Double.parseDouble(txtPantalla.getText());

				// Leert das Anzeigefeld für die Eingabe der zweiten Zahl.
				txtPantalla.setText("");

				// Speichert die ausgewählte Operation ("+").
				operacion = "+";
			}
		});

		// Legt die Vordergrundfarbe des "+"-Knopfes auf Rot fest.
		btnSuma.setForeground(Color.RED);
		// Stellt Schriftart und -größe für den Knopf ein.
		btnSuma.setFont(new Font("Arial", Font.BOLD, 18));

		// Positioniert den Knopf im Layout und legt seine Größe fest.
		btnSuma.setBounds(173, 117, 45, 36);

		// Fügt den Knopf zum Hauptbereich des Fensters hinzu.
		contentPane.add(btnSuma);

		// ---------------------------------------------------------------------
		// --- Weitere Operationstasten (-, x, /) folgen dem gleichen Muster ---
		// ---------------------------------------------------------------------
		JButton btnResta = new JButton("-");
		btnResta.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				// RESTA
				numero1 = Double.parseDouble(txtPantalla.getText());
				txtPantalla.setText("");
				;
				operacion = "-";
			}
		});
		btnResta.setForeground(Color.RED);
		btnResta.setFont(new Font("Arial", Font.BOLD, 18));
		btnResta.setBounds(175, 164, 45, 36);
		contentPane.add(btnResta);

		JButton btnMulti = new JButton("x");
		btnMulti.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				// MULTIPLICACI�N
				numero1 = Double.parseDouble(txtPantalla.getText());
				txtPantalla.setText("");
				;
				operacion = "*";
			}
		});
		btnMulti.setForeground(Color.RED);
		btnMulti.setFont(new Font("Arial", Font.BOLD, 18));
		btnMulti.setBounds(173, 211, 45, 36);
		contentPane.add(btnMulti);

		JButton btnDivi = new JButton("/");
		btnDivi.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				// DIVICI�N
				numero1 = Double.parseDouble(txtPantalla.getText());
				txtPantalla.setText("");
				;
				operacion = "/";
			}
		});
		btnDivi.setForeground(Color.RED);
		btnDivi.setFont(new Font("Arial", Font.BOLD, 18));
		btnDivi.setBounds(173, 258, 45, 36);
		contentPane.add(btnDivi);

		// ----------------------------------------------------------------
		// RECHENOPERATIONEN (Ereignisbehandlung für die Rechenoperationen)
		// ----------------------------------------------------------------
		JButton btnIgual = new JButton("=");
		btnIgual.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				numero2 = Double.parseDouble(txtPantalla.getText()); // Zweite Zahl aus dem Textfeld holen

				if (operacion.equals("+")) { // String-Vergleich mit .equals()
					resultado = numero1 + numero2;
				} else if (operacion.equals("-")) {
					resultado = numero1 - numero2;
				} else if (operacion.equals("*")) {
					resultado = numero1 * numero2;
				} else if (operacion.equals("/")) {
					if (numero2 != 0) { // Prüfung auf Division durch Null
						resultado = numero1 / numero2;
					} else {
						txtPantalla.setText("Error"); // Fehlermeldung anzeigen
						return; // Methode verlassen, da Division durch Null nicht erlaubt ist
					}
				}

				// -----------------------------------------------------------------
				// Formatierung des Ergebnisses (zwei Nachkommastellen, falls nötig)
				// -----------------------------------------------------------------
				String seleccionar = String.format("%.2f", resultado);
				txtPantalla.setText(seleccionar); // Ergebnis im Textfeld anzeigen
			}
		});
		// ... (Einstellungen für Farbe, Schriftart, Position usw.)
		btnIgual.setForeground(Color.RED);
		btnIgual.setFont(new Font("Arial", Font.BOLD, 18));
		btnIgual.setBounds(120, 258, 45, 36);
		contentPane.add(btnIgual);

	}
}