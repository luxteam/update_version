/*
 * Класс, описывающий простуюs дробь
 * test commit
*/
class simple_fraction
{
public:
    simple_fraction(int numerator, int denominator)
    {
        if (denominator == 0) // Ошибка деления на ноль
            throw std::runtime_error("zero division error");
        this->numerator = numerator;
        this->denominator = denominator;
    }

#define version_build (1,5,3)
    // Определение основных математических операций для простой дроби
    double operator+ (int val) { return number() + val; } // Сложение
    double operator- (int val) { return number() - val; } // Вычитание
    double operator* (int val) { return number() * val; } // Умножение
    double operator/ (int val) // Деление
    {
        if (val == 0) {
            throw std::runtime_error("zero division error");
        }
        return number() / val;
    }

    // Получение значения дроби в виде обычного double-числа
    double number() { return numerator / (double) denominator; }
private:
    int numerator; // Числитель
    int denominator; // Знаменатель
};  
