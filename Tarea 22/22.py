import requests
import logging
import argparse
import getpass
import six

# Configurar argparse
parser = argparse.ArgumentParser(description="Usar la API de Have I Been Pwned")
parser.add_argument('--email', type=str, required=True, help="Correo electrónico a investigar")
args = parser.parse_args()

key = getpass.getpass("Ingrese la API key: ")

headers = {
    'content-type': 'application/json',
    'api-version': '3',
    'User-Agent': 'python',
    'hibp-api-key': key
}

try:
    url = f'https://haveibeenpwned.com/api/v3/breachedaccount/{args.email}?truncateResponse=false'
    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        data = r.json()
        encontrados = len(data)
        if encontrados > 0:
            print(f"Los sitios en los que se ha filtrado el correo {args.email} son:")
            for filtracion in data:
                print(filtracion["Name"])
        else:
            print(f"El correo {args.email} no ha sido filtrado")

        msg = f"{args.email} - Filtraciones encontradas: {encontrados}"
        logging.basicConfig(filename='hibpINFO.log',
                            format="%(asctime)s %(message)s",
                            datefmt="%m/%d/%Y %I:%M:%S %p",
                            level=logging.INFO)
        logging.info(msg)

    elif r.status_code == 404:
        print(f"No se encontraron datos para el correo {args.email}.")
        logging.warning(f"No se encontraron datos para el correo {args.email}.")

    else:
        msg = f"Error: {r.status_code} - {r.text}"
        print(msg)
        logging.basicConfig(filename='hibpERROR.log',
                            format="%(asctime)s %(message)s",
                            datefmt="%m/%d/%Y %H:%M:%S",
                            level=logging.ERROR)
        logging.error(msg)

except requests.exceptions.RequestException as e:
    error_msg = f"Error al realizar la solicitud: {e}"
    print(error_msg)
    logging.error(error_msg)

if six.PY3:
    print("El script está corriendo en Python 3.")
else:
    print("El script está corriendo en Python 2.")


#Alumno: Raúl Cárdenas Ibarra