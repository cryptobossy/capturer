import requests
from app.config import Config

def main():
    domain = input("Introduce el dominio actual (ejemplo: https://midominio.com): ").strip()
    if not domain.startswith("http"):
        print("El dominio debe comenzar con http:// o https://")
        return

    webhook_url = f"{domain}/webhook"

    # 1. Verificar el webhook actual
    get_webhook_url = f"{Config.TELEGRAM_API_URL}/getWebhookInfo"
    resp = requests.get(get_webhook_url)
    if resp.ok:
        current_url = resp.json().get("result", {}).get("url", "")
        if current_url:
            print(f"Webhook actual: {current_url}")
            # 2. Eliminar el webhook si está ocupado
            delete_url = f"{Config.TELEGRAM_API_URL}/deleteWebhook"
            del_resp = requests.post(delete_url)
            if del_resp.ok:
                print("Webhook anterior eliminado correctamente.")
            else:
                print(f"Error al eliminar el webhook anterior: {del_resp.text}")
                return
        else:
            print("No hay webhook configurado actualmente.")
    else:
        print(f"Error al obtener información del webhook: {resp.text}")
        return

    # 3. Setear el nuevo webhook
    set_url = f"{Config.TELEGRAM_API_URL}/setWebhook"
    response = requests.post(set_url, data={"url": webhook_url})
    if response.ok:
        print(f"Webhook actualizado correctamente a: {webhook_url}")
    else:
        print(f"Error al actualizar el webhook: {response.text}")

if __name__ == "__main__":
    main()