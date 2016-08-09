#ifndef FORM_AGREGAR_NUEVOS_CREDITOS_H
#define FORM_AGREGAR_NUEVOS_CREDITOS_H

#include <QDialog>

namespace Ui {
class form_agregar_nuevos_creditos;
}

class form_agregar_nuevos_creditos : public QDialog
{
    Q_OBJECT

public:
    explicit form_agregar_nuevos_creditos(QWidget *parent = 0);
    ~form_agregar_nuevos_creditos();

private:
    Ui::form_agregar_nuevos_creditos *ui;
};

#endif // FORM_AGREGAR_NUEVOS_CREDITOS_H
