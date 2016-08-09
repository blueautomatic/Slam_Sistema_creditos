#include "form_agregar_nuevos_creditos.h"
#include "ui_form_agregar_nuevos_creditos.h"

form_agregar_nuevos_creditos::form_agregar_nuevos_creditos(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::form_agregar_nuevos_creditos)
{
    ui->setupUi(this);
}

form_agregar_nuevos_creditos::~form_agregar_nuevos_creditos()
{
    delete ui;
}
