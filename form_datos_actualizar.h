#ifndef FORM_DATOS_ACTUALIZAR_H
#define FORM_DATOS_ACTUALIZAR_H

#include <QDialog>

namespace Ui {
class form_datos_actualizar;
}

class form_datos_actualizar : public QDialog
{
    Q_OBJECT

public:
    explicit form_datos_actualizar(QWidget *parent = 0);
    ~form_datos_actualizar();

private:
    Ui::form_datos_actualizar *ui;
};

#endif // FORM_DATOS_ACTUALIZAR_H
