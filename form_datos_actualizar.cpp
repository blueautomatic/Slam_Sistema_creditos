#include "form_datos_actualizar.h"
#include "ui_form_datos_actualizar.h"

form_datos_actualizar::form_datos_actualizar(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::form_datos_actualizar)
{
    ui->setupUi(this);
}

form_datos_actualizar::~form_datos_actualizar()
{
    delete ui;
}
