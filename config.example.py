# Пример конфигурационного файла
# Скопируйте этот файл в config.py и заполните реальными значениями

# Токен Telegram бота
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

# VK.ОРД API настройки
VK_ORD_API_TOKEN = "YOUR_VK_ORD_API_TOKEN_HERE"
VK_ORD_API_BASE = "https://api-sandbox.ord.vk.com"  # или production URL

# ID группы Telegram для отправки метрик (бот должен быть админом)
ADMIN_CHAT_ID = "1003460901654"

# Пути к шаблонам (относительно корня проекта или абсолютные)
TEMPLATE_INVOICE_SINGLE = "templates/schet-oferta.docx"
TEMPLATE_INVOICE_MULTI = "templates/schet-oferta2-multi.docx"
TEMPLATE_INVOICE_MULTI_PRO = "templates/schet-oferta2-multiPRO.docx"
TEMPLATE_CONTRACT = "templates/dogovor_rim.docx"
TEMPLATE_CONTRACT_MULTI = "templates/dogovor_rim2-multi.docx"

# Прочие настройки
OUTPUT_DIR = "generated"
COUNTERS_FILE = "counters.json"
METRICS_FILE = "metrics.json"
MAX_ITEMS_FOR_TEMPLATE = 50
CAPTION_LIMIT = 1024

