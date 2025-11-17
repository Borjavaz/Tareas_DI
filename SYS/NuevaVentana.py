import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel,
                             QLineEdit, QVBoxLayout, QWidget, QCheckBox,
                             QHBoxLayout, QComboBox, QTextEdit, QGridLayout,
                             QRadioButton, QButtonGroup, QTableView, QTabWidget)
from PyQt6.QtGui import QFont


class NuevaVentana(QMainWindow):
    """
    Nueva ventana usando los mismos conceptos de la anterior
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nueva Ventana - Ejemplo Completo")
        self.setGeometry(200, 200, 800, 600)

        # Layout principal en grid
        layout_principal = QGridLayout()

        # ===== SECCIÓN IZQUIERDA =====
        seccion_izquierda = QVBoxLayout()

        # Grupo de información personal
        lbl_titulo = QLabel("Información Personal")
        lbl_titulo.setFont(QFont("Arial", 12, QFont.Weight.Bold))

        # Campos de texto para información personal
        self.txt_nombre = QLineEdit()
        self.txt_nombre.setPlaceholderText("Nombre completo")

        self.txt_email = QLineEdit()
        self.txt_email.setPlaceholderText("Correo electrónico")

        self.txt_telefono = QLineEdit()
        self.txt_telefono.setPlaceholderText("Teléfono")

        # ComboBox para selección de país
        self.cmb_pais = QComboBox()
        self.cmb_pais.addItems(["España", "México", "Argentina", "Colombia", "Chile", "Perú"])
        self.cmb_pais.currentIndexChanged.connect(self.cambio_pais)

        # ===== SECCIÓN RADIO BUTTONS =====
        grupo_genero = QButtonGroup(self)
        self.rbt_masculino = QRadioButton("Masculino")
        self.rbt_femenino = QRadioButton("Femenino")
        self.rbt_otro = QRadioButton("Otro")

        grupo_genero.addButton(self.rbt_masculino)
        grupo_genero.addButton(self.rbt_femenino)
        grupo_genero.addButton(self.rbt_otro)

        layout_genero = QVBoxLayout()
        layout_genero.addWidget(QLabel("Género:"))
        layout_genero.addWidget(self.rbt_masculino)
        layout_genero.addWidget(self.rbt_femenino)
        layout_genero.addWidget(self.rbt_otro)

        # ===== CHECKBOXES =====
        self.chk_terminos = QCheckBox("Acepto los términos y condiciones")
        self.chk_noticias = QCheckBox("Deseo recibir noticias")
        self.chk_noticias.setChecked(True)

        # Botón de envío
        btn_enviar = QPushButton("Enviar Información")
        btn_enviar.clicked.connect(self.enviar_informacion)

        # Añadir widgets a la sección izquierda
        seccion_izquierda.addWidget(lbl_titulo)
        seccion_izquierda.addWidget(QLabel("Nombre:"))
        seccion_izquierda.addWidget(self.txt_nombre)
        seccion_izquierda.addWidget(QLabel("Email:"))
        seccion_izquierda.addWidget(self.txt_email)
        seccion_izquierda.addWidget(QLabel("Teléfono:"))
        seccion_izquierda.addWidget(self.txt_telefono)
        seccion_izquierda.addWidget(QLabel("País:"))
        seccion_izquierda.addWidget(self.cmb_pais)
        seccion_izquierda.addLayout(layout_genero)
        seccion_izquierda.addWidget(self.chk_terminos)
        seccion_izquierda.addWidget(self.chk_noticias)
        seccion_izquierda.addWidget(btn_enviar)
        seccion_izquierda.addStretch()

        # ===== SECCIÓN DERECHA =====
        # Widget con pestañas
        tabs = QTabWidget()

        # Pestaña 1: Área de texto para resumen
        self.txa_resumen = QTextEdit()
        self.txa_resumen.setPlaceholderText("Aquí se mostrará el resumen de la información...")
        tabs.addTab(self.txa_resumen, "Resumen")

        # Pestaña 2: Información adicional
        txa_info = QTextEdit()
        txa_info.setPlainText("""INSTRUCCIONES:

1. Complete todos los campos del formulario
2. Seleccione su género
3. Elija su país de residencia
4. Acepte los términos y condiciones
5. Presione 'Enviar Información'

Los datos se mostrarán en la pestaña 'Resumen'.""")
        tabs.addTab(txa_info, "Instrucciones")

        # ===== DISPOSICIÓN FINAL =====
        layout_principal.addLayout(seccion_izquierda, 0, 0, 1, 1)
        layout_principal.addWidget(tabs, 0, 1, 1, 1)

        # Widget contenedor
        widget_central = QWidget()
        widget_central.setLayout(layout_principal)
        self.setCentralWidget(widget_central)

        # Conectar señales
        self.txt_nombre.textChanged.connect(self.actualizar_resumen)
        self.txt_email.textChanged.connect(self.actualizar_resumen)

    def cambio_pais(self, indice):
        """Maneja el cambio de selección en el ComboBox de países"""
        pais_seleccionado = self.cmb_pais.itemText(indice)
        print(f"País seleccionado: {pais_seleccionado}")
        self.actualizar_resumen()

    def actualizar_resumen(self):
        """Actualiza el área de texto con la información actual"""
        nombre = self.txt_nombre.text() if self.txt_nombre.text() else "[No especificado]"
        email = self.txt_email.text() if self.txt_email.text() else "[No especificado]"
        telefono = self.txt_telefono.text() if self.txt_telefono.text() else "[No especificado]"
        pais = self.cmb_pais.currentText()

        genero = ""
        if self.rbt_masculino.isChecked():
            genero = "Masculino"
        elif self.rbt_femenino.isChecked():
            genero = "Femenino"
        elif self.rbt_otro.isChecked():
            genero = "Otro"
        else:
            genero = "[No seleccionado]"

        resumen = f"""INFORMACIÓN ACTUAL:

Nombre: {nombre}
Email: {email}
Teléfono: {telefono}
País: {pais}
Género: {genero}

Términos aceptados: {'Sí' if self.chk_terminos.isChecked() else 'No'}
Recibir noticias: {'Sí' if self.chk_noticias.isChecked() else 'No'}"""

        self.txa_resumen.setPlainText(resumen)

    def enviar_informacion(self):
        """Maneja el envío del formulario"""
        if not self.chk_terminos.isChecked():
            self.txa_resumen.setPlainText("ERROR: Debe aceptar los términos y condiciones para enviar el formulario.")
            return

        if not self.txt_nombre.text():
            self.txa_resumen.setPlainText("ERROR: El campo 'Nombre' es obligatorio.")
            return

        # Simular envío exitoso
        self.txa_resumen.setPlainText("¡FORMULARIO ENVIADO CON ÉXITO!\n\n" +
                                      self.txa_resumen.toPlainText().replace("INFORMACIÓN ACTUAL",
                                                                             "INFORMACIÓN ENVIADA"))

        print("Información enviada correctamente")


# Ejecutar la aplicación
if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = NuevaVentana()
    ventana.show()
    aplicacion.exec()