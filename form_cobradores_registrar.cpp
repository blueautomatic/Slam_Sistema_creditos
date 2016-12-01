#include "form_cobradores_registrar.h"
#include "ui_form_cobradores_registrar.h"

Form_cobradores_registrar::Form_cobradores_registrar(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Form_cobradores_registrar)
{
    ui->setupUi(this);
}

Form_cobradores_registrar::~Form_cobradores_registrar()
{
    delete ui;
}
