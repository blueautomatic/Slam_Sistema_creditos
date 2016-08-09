#ifndef FORM_CLIENTES_BORRAR_H
#define FORM_CLIENTES_BORRAR_H

#include <QDialog>

namespace Ui {
class form_clientes_borrar;
}

class form_clientes_borrar : public QDialog
{
    Q_OBJECT

public:
    explicit form_clientes_borrar(QWidget *parent = 0);
    ~form_clientes_borrar();

private:
    Ui::form_clientes_borrar *ui;
};

#endif // FORM_CLIENTES_BORRAR_H
