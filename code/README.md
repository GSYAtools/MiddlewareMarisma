Para ejecutar, primero arrancar en el entorno virtual: .venv\Scripts\Activate.ps1
Si no coge bien el comando: curl.exe -X POST http://127.0.0.1:8000/run_all 
Hacer:
$env:PYTHONPATH="C:\Users\Natalia\Documents\GitHub\MiddlewareMarisma\code"
uvicorn app:app --reload
