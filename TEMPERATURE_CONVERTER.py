#!/usr/bin/env python
# coding: utf-8

# In[1]:


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Welcome to the Temperature Converter!")

    try:
        value = float(input("Enter the temperature value: "))
        source_unit = input("Enter the source unit (C for Celsius, F for Fahrenheit): ").upper()
        target_unit = input("Enter the target unit (C for Celsius, F for Fahrenheit): ").upper()

        if source_unit == target_unit:
            print("Source and target units are the same. No conversion needed.")
        elif source_unit == 'C' and target_unit == 'F':
            result = celsius_to_fahrenheit(value)
            print(f"{value}° Celsius is equal to {result}° Fahrenheit.")
        elif source_unit == 'F' and target_unit == 'C':
            result = fahrenheit_to_celsius(value)
            print(f"{value}° Fahrenheit is equal to {result}° Celsius.")
        else:
            print("Unsupported units. Please enter either 'C' or 'F' for Celsius or Fahrenheit.")

    except ValueError:
        print("Invalid input. Please enter a numeric value for temperature.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()


# In[ ]:




