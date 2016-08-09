#ifndef FORM_CLIENTES_ACTUALIZAR_H
#define FORM_CLIENTES_ACTUALIZAR_H

#include <QDialog>

namespace Ui {
class form_clientes_actualizar;
}

class form_clientes_actualizar : public QDialog
{
    Q_OBJECT

public:
    explicit form_clientes_actualizar(QWidget *parent = 0);
    ~form_clientes_actualizar();

private:
    Ui::form_clientes_actualizar *ui;
};

#endif // FORM_CLIENTES_ACTUALIZAR_H
