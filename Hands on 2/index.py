import math

def sum(arraySum):
    suma = 0
    for element in arraySum:
        suma = suma + element

    return suma

def xy(array_x, array_y):
    arrayAux= []

    for i in range(len(array_x)):
        arrayAux.append(array_x[i] * array_y[i])

    return arrayAux

def array_raised_to(array):
    auxArray = []

    for element in array:
        auxArray.append(element * element)

    return auxArray


sales_y = [651, 762, 856, 1063, 1190, 1298, 1421, 1440, 1518]
advertising_x = [23, 26, 30, 34, 43, 48, 52, 57, 58]

sales_adv_xy = xy(advertising_x, sales_y)
sum_sales_y = sum(sales_y)
sum_adv_x= sum(advertising_x)
sum_adv_sales_xy = sum(sales_adv_xy)
x_rised_to_2 = array_raised_to(advertising_x)
y_rised_to_2 = array_raised_to(sales_y)
sum_x_rised_to_2 = sum(x_rised_to_2)
sum_y_rised_to_2 = sum(y_rised_to_2)

#Calcular correlación
prom_x = sum_adv_x / len(advertising_x)
prom_y = sum_sales_y / len(sales_y)

array_x_promx = []
for element in advertising_x:
    array_x_promx.append(element - prom_x)

array_x_promx_pow = []
for element in array_x_promx:
    array_x_promx_pow.append(element * element)

sum_array_x_promx_pow = sum(array_x_promx_pow)

array_y_promy = []
for element in sales_y:
    array_y_promy.append(element - prom_y)

array_y_promy_pow = []
for element in array_y_promy:
    array_y_promy_pow.append(element * element)

sum_array_y_promy_pow = sum(array_y_promy_pow)

array_x_promx_array_y_promy = []
for ele1, ele2 in zip(array_x_promx, array_y_promy):
    array_x_promx_array_y_promy.append(ele1 * ele2)

sum_array_x_promx_array_y_promy = sum(array_x_promx_array_y_promy)

correlation = sum_array_x_promx_array_y_promy / (math.sqrt(sum_array_x_promx_pow) * math.sqrt(sum_array_y_promy_pow))
determination = correlation ** 2

B1 = (9 * sum_adv_sales_xy - sum_adv_x * sum_sales_y) / (9 * sum_x_rised_to_2 - sum_adv_x * sum_adv_x)
B2 = (sum_sales_y - B1 * sum_adv_x) / 9



adv = 23

print(f"Formula: {B2} + {B1} * {adv}")

print("Coeficiente de correlcion: ", correlation)
print("Determinacion: ", determination)
print("Prediccion de datos: ", (B2 + B1 * adv))