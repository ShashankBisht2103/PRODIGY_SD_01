#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double temperature;
    char unit;

    cout << "Temperature Conversion Program\n";
    cout << "------------------------------\n";

    cout << "Enter temperature: ";
    cin >> temperature;

    cout << "Enter original unit (C/F/K): ";
    cin >> unit;

    double celsius, fahrenheit, kelvin;

    switch (toupper(unit)) {
        case 'C':
            celsius = temperature;
            fahrenheit = (celsius * 9.0 / 5.0) + 32;
            kelvin = celsius + 273.15;
            break;

        case 'F':
            fahrenheit = temperature;
            celsius = (fahrenheit - 32) * 5.0 / 9.0;
            kelvin = celsius + 273.15;
            break;

        case 'K':
            kelvin = temperature;
            celsius = kelvin - 273.15;
            fahrenheit = (celsius * 9.0 / 5.0) + 32;
            break;

        default:
            cout << "Invalid unit entered!" << endl;
            return 1;
    }

    cout << fixed << setprecision(2);
    cout << "\nConverted Temperatures:\n";
    cout << "Celsius:    " << celsius << " °C\n";
    cout << "Fahrenheit: " << fahrenheit << " °F\n";
    cout << "Kelvin:     " << kelvin << " K\n";

    return 0;
}