# 🌳 Дерево проекта PROMO-PRO

## Структура файлов и папок

```
PROMO-PRO/
│
├── 📄 ПОЛИРОЛЬОТБИВКИ.py                    # Основной файл бота (~4000 строк)
│   └── Содержит весь функционал бота
│
├── ⚙️ Конфигурация
│   ├── config.py                            # Реальная конфигурация (НЕ в git ⚠️)
│   └── config.example.py                    # Пример конфигурации
│
├── 📦 Зависимости и Docker
│   ├── requirements.txt                     # Python зависимости
│   ├── Dockerfile                           # Docker образ
│   └── docker-compose.yml                   # Docker Compose конфигурация
│
├── 📚 Документация
│   ├── README.md                            # Базовая документация (стартовая точка)
│   ├── PROJECT_DOCUMENTATION.md             # Полная техническая документация ⭐
│   ├── ARCHITECTURE.md                      # Описание архитектуры
│   ├── SETUP_GUIDE.md                       # Руководство по настройке для нового инженера
│   ├── PROJECT_TREE.md                      # Этот файл (дерево проекта)
│   └── telegram-bot-docker.plan.md          # План разработки (исторический)
│
├── 🔒 secrets/                              # ⚠️ Чувствительные данные (НЕ в git)
│   ├── README.md                            # Описание папки secrets
│   ├── counters.json                        # Счетчики документов по дням
│   ├── metrics.json                         # Метрики уникальных пользователей
│   ├── vk_ord_tokens.json                   # Токены пользователей VK.ОРД
│   ├── vk_ord_state.json                    # Состояние VK.ОРД
│   ├── PASSWORD.txt                         # Пароли (если используются)
│   │
│   ├── user_data/                           # Данные пользователей
│   │   └── {user_id}/                       # Папка для каждого пользователя
│   │       ├── invoices/                    # Сгенерированные счета
│   │       │   └── Счет-оферта_*.docx
│   │       ├── contracts/                   # Сгенерированные договоры
│   │       │   └── Договор_РИМ_*.docx
│   │       └── tmp/                         # Временные файлы
│   │
│   └── vk/                                  # VK.ОРД API файлы
│       ├── API_TEST_ORD_UDOVIN(rusinov.ds).txt
│       └── API_VK_ORD_UDOVIN.txt
│
├── 📝 templates/                            # Шаблоны Word документов
│   ├── schet-oferta.docx                    # Шаблон счета-оферты (одиночный)
│   ├── schet-oferta2-multi.docx             # Шаблон счета-оферты (множественный)
│   ├── schet-oferta2-multiPRO.docx          # Шаблон счета-оферты (PRO версия)
│   ├── dogovor_rim.docx                     # Шаблон договора РИМ (одиночный)
│   └── dogovor_rim2-multi.docx              # Шаблон договора РИМ (множественный)
│
├── 📁 generated/                            # Legacy: старые сгенерированные документы
│   └── *.docx                               # Документы из старой версии
│
├── 📁 backup/                               # Резервные копии старых версий
│   ├── promo_pro_secure_vkord_auto_v11.py
│   ├── promo_pro_secure_vkord_auto_v7_fix5.py
│   ├── promopro_secure_adapted.py
│   ├── promopro.py
│   ├── RESERVE.PY
│   └── [множество других .py файлов]        # История разработки
│
├── 📁 files/                                # Вспомогательные файлы
│   ├── app.py                               # FastAPI приложение (webhook вариант)
│   ├── requirements.txt                     # Старый файл зависимостей
│   ├── test_getme.py                        # Тестовые файлы
│   └── [другие вспомогательные файлы]
│
├── 🎨 logo/                                 # Логотипы проекта
│   └── *.png, *.mp4
│
├── 📦 stickerpack/                          # Стикеры для бота
│   ├── Pack1/
│   └── Пак2/
│
├── ⚠️ ОРДГОТОВНА99.py                      # Старый файл (НЕ используется, в .gitignore)
│
└── 📄 .gitignore                            # Игнорируемые файлы git

```

## Важные файлы по назначению

### 🎯 Основной код
- `ПОЛИРОЛЬОТБИВКИ.py` - главный файл с всей логикой бота

### ⚙️ Конфигурация
- `config.py` - реальная конфигурация с токенами (создается вручную)
- `config.example.py` - шаблон конфигурации

### 📊 Данные
- `secrets/counters.json` - счетчики документов
- `secrets/metrics.json` - метрики пользователей
- `secrets/vk_ord_*.json` - состояние VK.ОРД
- `secrets/user_data/` - документы пользователей

### 📝 Шаблоны
- `templates/*.docx` - шаблоны Word документов

### 📚 Документация
- `README.md` - быстрый старт
- `PROJECT_DOCUMENTATION.md` - полная документация
- `ARCHITECTURE.md` - архитектура
- `SETUP_GUIDE.md` - настройка для нового инженера

## Размеры файлов (приблизительно)

- `ПОЛИРОЛЬОТБИВКИ.py`: ~4000 строк, ~150KB
- `PROJECT_DOCUMENTATION.md`: ~600 строк
- `ARCHITECTURE.md`: ~250 строк
- `SETUP_GUIDE.md`: ~150 строк

## Файлы, которые НЕ должны быть в git

- ✅ `config.py` - конфигурация с токенами
- ✅ `secrets/` - вся папка с чувствительными данными
- ✅ `ОРДГОТОВНА99.py` - старый файл с хардкод токенами
- ✅ `*.log` - логи
- ✅ `__pycache__/` - кэш Python

Все эти файлы указаны в `.gitignore`.

## Что должно быть в git

- ✅ Код бота (`ПОЛИРОЛЬОТБИВКИ.py`)
- ✅ Конфигурация примеров (`config.example.py`)
- ✅ Документация (`*.md`)
- ✅ Docker файлы (`Dockerfile`, `docker-compose.yml`)
- ✅ Зависимости (`requirements.txt`)
- ✅ Шаблоны (`templates/*.docx`)
- ✅ `.gitignore`

---

**Последнее обновление:** 2025-11-26

