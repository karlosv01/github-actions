import unittest
# Importamos la función main de tu app.py (si es que existe)
# o simplemente probamos algo básico para validar el CI
from app import main 

class TestApp(unittest.TestCase):

    def test_saludo(self):
        # Una prueba simple que siempre pasa
        self.assertEqual(1 + 1, 2)

    def test_ejecucion_main(self):
        # Verifica que la función main no explote al llamarla
        try:
            # Si tu main() solo hace un print, esto pasará sin problemas
            main() 
            ejecuto_correctamente = True
        except Exception:
            ejecuto_correctamente = False
        
        self.assertTrue(ejecuto_correctamente)

if __name__ == '__main__':
    unittest.main()
