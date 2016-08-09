#include "form_clientes_borrar.h"
#include "ui_form_clientes_borrar.h"

form_clientes_borrar::form_clientes_borrar(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::form_clientes_borrar)
{
    ui->setupUi(this);
}

form_clientes_borrar::~form_clientes_borrar()
{
    delete ui;
}
