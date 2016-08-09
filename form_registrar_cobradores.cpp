#include "form_registrar_cobradores.h"
#include "ui_form_registrar_cobradores.h"

form_registrar_cobradores::form_registrar_cobradores(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::form_registrar_cobradores)
{
    ui->setupUi(this);
}

form_registrar_cobradores::~form_registrar_cobradores()
{
    delete ui;
}
