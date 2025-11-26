# 🏗️ Архитектура проекта PROMO-PRO

## Обзор архитектуры

PROMO-PRO построен на **монолитной архитектуре** - весь код находится в одном файле `ПОЛИРОЛЬОТБИВКИ.py` (~4000 строк).

## Компоненты системы

### 1. Telegram Bot Layer (aiogram 3.x)

```
┌─────────────────────────────────────┐
│         Telegram Bot API            │
│         (aiogram 3.12)              │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│      Dispatcher & Handlers          │
│  - cmd_start                         │
│  - cmd_stats                         │
│  - InvoiceForm handlers              │
│  - ContractForm handlers             │
│  - VK.ОРД handlers                   │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│       Business Logic Layer          │
│  - Document generation               │
│  - VK.ОРД API client                 │
│  - Metrics tracking                  │
│  - File management                   │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│        Storage Layer                │
│  - JSON files (counters, metrics)    │
│  - User data directories             │
│  - Template files                    │
└─────────────────────────────────────┘
```

## Потоки данных

### Поток создания счета

```
User → /start → cmd_start()
  ↓
User → "Выставить счёт" → start_invoice_flow()
  ↓
FSM: InvoiceForm.customer_name → invoice_customer_name()
  ↓
FSM: InvoiceForm.customer_inn → invoice_customer_inn()
  ↓
FSM: InvoiceForm.item_channel → item_channel()
  ↓
FSM: InvoiceForm.item_period → item_period()
  ↓
FSM: InvoiceForm.item_amount → item_amount()
  ↓
"Добавить пункт" → add_item_start() (цикл)
  ↓
"Сформировать счёт" → form_invoice_entry()
  ↓
render_docx_with_dynamic_rows()
  ↓
save → secrets/user_data/{user_id}/invoices/
  ↓
send_document() → User
```

### Поток VK.ОРД интеграции

```
User → "Перейти в кабинет VK.ОРД" → connect_vk_ord_lk()
  ↓
User → "Добавить контрагента" → vk_ord_add_contractor()
  ↓
FSM: выбор типа → vk_ord_person_type_step()
  ↓
FSM: ввод данных → vk_ord_person_*_step()
  ↓
FSM: подтверждение → vk_ord_person_confirm_step()
  ↓
vk_ord_api_request("PUT", "/v1/person/{id}", payload)
  ↓
save state → secrets/vk_ord_state.json
  ↓
response → User
```

## Модули и зависимости

### Основные модули

1. **aiogram** - Telegram Bot Framework
   - Bot, Dispatcher, FSM
   - Message, CallbackQuery types

2. **python-docx** - Работа с Word документами
   - Document, Paragraph, Table
   - Замена плейсхолдеров

3. **aiohttp** - Асинхронные HTTP запросы
   - VK.ОРД API клиент

4. **cryptography** - Шифрование (если используется)

### Внутренние модули (в одном файле)

- **FSM States** - состояния форм
- **Handlers** - обработчики команд и сообщений
- **Utils** - вспомогательные функции
- **DOCX Renderer** - рендеринг документов
- **Metrics** - отслеживание метрик
- **VK.ОРД Client** - клиент API

## Паттерны проектирования

### State Machine Pattern
Используется aiogram FSM для управления состоянием пользователя в формах.

### Template Method Pattern
Шаблоны документов (DOCX) с подстановкой переменных.

### Repository Pattern (упрощенный)
Функции `load_*()` и `save_*()` для работы с файловым хранилищем.

## Обработка ошибок

```python
try:
    # основная логика
except Exception as e:
    logging.error(f"Ошибка: {e}")
    await message.answer("❌ Произошла ошибка...")
```

## Асинхронность

Все операции I/O асинхронные:
- Запросы к Telegram API
- Запросы к VK.ОРД API
- Чтение/запись файлов (частично синхронное)

## Расширяемость

Для добавления новых функций:
1. Добавить новый FSM State Group (если нужна форма)
2. Добавить handlers для регистрации в `main()`
3. Добавить клавиатуры (если нужны)
4. Добавить функции бизнес-логики

## Ограничения текущей архитектуры

1. **Монолит** - весь код в одном файле (сложно поддерживать при росте)
2. **Файловое хранилище** - нет БД (ограничения при масштабировании)
3. **Синхронные операции с файлами** - блокируют event loop
4. **Нет миграций** - структура данных меняется без версионирования

## Рекомендации для будущего развития

1. Разделить на модули:
   - `handlers/` - обработчики
   - `services/` - бизнес-логика
   - `models/` - модели данных
   - `utils/` - утилиты

2. Перейти на БД (SQLite/PostgreSQL):
   - Для метрик и счетчиков
   - Для состояния пользователей

3. Добавить middleware для логирования и обработки ошибок

4. Вынести конфигурацию в отдельный модуль

5. Добавить тесты (pytest)

