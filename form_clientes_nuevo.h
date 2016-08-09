#ifndef FORM_CLIENTES_NUEVO_H
#define FORM_CLIENTES_NUEVO_H

#include <QDialog>

namespace Ui {
class form_clientes_nuevo;
}

class form_clientes_nuevo : public QDialog
{
    Q_OBJECT

public:
    explicit form_clientes_nuevo(QWidget *parent = 0);
    ~form_clientes_nuevo();

private:
    Ui::form_clientes_nuevo *ui;
};

#endif // FORM_CLIENTES_NUEVO_H
