#ifndef FORM_DATOS_EMPRESA_BORRAR_H
#define FORM_DATOS_EMPRESA_BORRAR_H

#include <QDialog>

namespace Ui {
class form_datos_empresa_borrar;
}

class form_datos_empresa_borrar : public QDialog
{
    Q_OBJECT

public:
    explicit form_datos_empresa_borrar(QWidget *parent = 0);
    ~form_datos_empresa_borrar();

private:
    Ui::form_datos_empresa_borrar *ui;
};

#endif // FORM_DATOS_EMPRESA_BORRAR_H
