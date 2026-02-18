import unittest
# Importamos el objeto 'app' de Flask, ya no existe 'main'
from app import app 

class TestApp(unittest.TestCase):

    def test_saludo_basico(self):
        # Una prueba matemática simple para validar el runner
        self.assertEqual(1 + 1, 2)

    def test_flask_response(self):
        # Creamos un cliente de prueba de Flask
        # Esto permite probar la app sin levantar el servidor real
        tester = app.test_client(self)
        response = tester.get('/')
        
        # Verificamos que responda 200 OK
        self.assertEqual(response.status_code, 200)
        # Verificamos que el contenido sea el esperado
        self.assertEqual(response.data.decode('utf-8'), "Hola Mundo desde Flask!")

if __name__ == '__main__':
    unittest.main()
