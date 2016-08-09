#ifndef FORM_REGISTRAR_COBRADORES_H
#define FORM_REGISTRAR_COBRADORES_H

#include <QDialog>

namespace Ui {
class form_registrar_cobradores;
}

class form_registrar_cobradores : public QDialog
{
    Q_OBJECT

public:
    explicit form_registrar_cobradores(QWidget *parent = 0);
    ~form_registrar_cobradores();

private:
    Ui::form_registrar_cobradores *ui;
};

#endif // FORM_REGISTRAR_COBRADORES_H
