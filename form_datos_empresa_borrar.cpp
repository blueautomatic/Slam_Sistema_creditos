#include "form_datos_empresa_borrar.h"
#include "ui_form_datos_empresa_borrar.h"

form_datos_empresa_borrar::form_datos_empresa_borrar(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::form_datos_empresa_borrar)
{
    ui->setupUi(this);
}

form_datos_empresa_borrar::~form_datos_empresa_borrar()
{
    delete ui;
}
