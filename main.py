from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile
from Gui.VentanaPrincipal1 import Ventana
#from Gui.VentanaPrincipal import Ui_MainWindow
#from Vistas import interfaz
import asyncio
import uvicorn

async def main():
    config = uvicorn.Config("main:app", port=5000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()
    app = QApplication([])
    myWidget = Ventana()
    myWidget.show()
    app.exec()

if __name__ == "__main__":
    asyncio.run(main())





#interfaz.pantalla_principal()