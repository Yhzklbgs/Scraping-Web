import requests

while True:
    tanya = input('Chat dengan simi (ketik "exit" untuk keluar): ')
    if tanya.lower() == 'exit':
        break  # Exit the loop if the user types "exit"
    r = requests.get(f'https://api.simsimi.net/v2/?text={tanya}&lc=id')
    data = r.json()
    if data["methods"] == 'GET':
        jawab = f"Jawaban simi: {data['success']}"
    else:
        jawab = "Tidak ada jawaban dari SimiSimi."
    print(jawab)
