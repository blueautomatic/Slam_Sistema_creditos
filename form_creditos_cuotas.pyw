#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5 import uic

class Dialogo(QDialog):
        def __init__(self):
                QDialog.__init__(self)
                uic.loadUi("form_creditos_cuotas_buscar.ui", self)





app = QApplication(sys.argv)
dialogo= Dialogo()
dialogo.show()
app.exec_()
