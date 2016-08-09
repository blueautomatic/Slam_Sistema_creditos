#include "form_clientes_nuevo.h"
#include "ui_form_clientes_nuevo.h"

form_clientes_nuevo::form_clientes_nuevo(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::form_clientes_nuevo)
{
    ui->setupUi(this);
}

form_clientes_nuevo::~form_clientes_nuevo()
{
    delete ui;
}
