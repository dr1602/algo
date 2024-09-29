// javascript
let data = [21, 17, 35, "🍎", 40, 15];

data.forEach((item) => {
  try {
    // Verifica si el item es un número
    if (typeof item !== 'number') {
      throw new Error('Este elemento no es un número.');
    }

    // Si es un número, verifica si es mayor o menor de edad
    if (item >= 18) {
      console.log(`El número ${item} es mayor de edad.`);
    } else {
      console.log(`El número ${item} es menor de edad.`);
    }
  } catch (error) {
    console.log(error.message);
  }
});

/*
El número 21 es mayor de edad.
El número 17 es menor de edad.
El número 35 es mayor de edad.
Este elemento no es un número.
El número 40 es mayor de edad.
El número 15 es menor de edad.
 */
