#include "form_clientes_actualizar.h"
#include "ui_form_clientes_actualizar.h"

form_clientes_actualizar::form_clientes_actualizar(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::form_clientes_actualizar)
{
    ui->setupUi(this);
}

form_clientes_actualizar::~form_clientes_actualizar()
{
    delete ui;
}
