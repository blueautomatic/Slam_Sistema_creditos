#ifndef FORM_COBRADORES_REGISTRAR_H
#define FORM_COBRADORES_REGISTRAR_H

#include <QWidget>

namespace Ui {
class Form_cobradores_registrar;
}

class Form_cobradores_registrar : public QWidget
{
    Q_OBJECT

public:
    explicit Form_cobradores_registrar(QWidget *parent = 0);
    ~Form_cobradores_registrar();

private:
    Ui::Form_cobradores_registrar *ui;
};

#endif // FORM_COBRADORES_REGISTRAR_H
