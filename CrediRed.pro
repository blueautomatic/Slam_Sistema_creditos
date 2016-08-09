#-------------------------------------------------
#
# Project created by QtCreator 2016-07-18T21:37:01
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = CrediRed
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp \
    form_clientes_nuevo.cpp \
    form_clientes_actualizar.cpp \
    form_clientes_borrar.cpp \
    form_agregar_nuevos_creditos.cpp \
    form_datos_actualizar.cpp \
    form_datos_empresa_borrar.cpp \
    form_registrar_cobradores.cpp

HEADERS  += mainwindow.h \
    form_clientes_nuevo.h \
    form_clientes_actualizar.h \
    form_clientes_borrar.h \
    form_agregar_nuevos_creditos.h \
    form_datos_actualizar.h \
    form_datos_empresa_borrar.h \
    form_registrar_cobradores.h

FORMS    += mainwindow.ui \
    form_clientes_nuevo.ui \
    form_clientes_actualizar.ui \
    form_clientes_borrar.ui \
    form_clientes_buscar.ui \
    form_creditos_cuotas_buscar.ui \
    form_descargas_direccion.ui \
    form_prestamos_generar_caida.ui \
    form_usuario_actualizar.ui \
    form_usuario_borrar.ui \
    form_usuario.ui \
    form_creditos_agregar_nuevos.ui \
    form_pagare_texto.ui \
    form_cobradores_registrar.ui \
    form_empresa_datos_actualizar.ui \
    form_empresa_datos.ui \
    form_prueba.ui \
    form_prueba2.ui \
    form_prueba3.ui

DISTFILES += \
    logica de pago credired.odt \
    CrediRed.pro.user \
    form_clientes_actualizar.pyw \
    form_creditos_cuotas.pyw
