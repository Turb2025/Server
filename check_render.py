import asyncio
from pyppeteer import launch
import logging

URL = "https://texten-3zgc.onrender.com/loop"

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(message)s')

async def check_render():
    logging.info("🔄 Iniciando Puppeteer para verificar o Render...")

    try:
        browser = await launch(headless=True, args=['--no-sandbox'])
        page = await browser.newPage()

        logging.info(f"🌐 Acessando {URL}")
        response = await page.goto(URL, timeout=60000)  # 60s

        # Aguarda até 1 minuto (Render pode demorar a acordar)
        await asyncio.sleep(60)

        if response and response.status == 200:
            logging.info("✅ Render acordado com sucesso!")
        else:
            logging.warning(f"⚠️ Render inativo ou sem resposta válida (status: {response.status if response else 'None'})")

        await browser.close()

    except Exception as e:
        logging.error(f"❌ Erro ao tentar acordar o Render: {e}")

asyncio.get_event_loop().run_until_complete(check_render())
