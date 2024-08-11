import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='/', intents=intents)


@bot.command(name='info')
async def info(ctx):
    response = """
    Вот список комманд:
    /decom - бот расскажет вам сколько разлагается предмет
    /eco-tips - бот расскажет как можно помочь природе
    /sorting - бот расскажет куда надо выбрасывать мусор
    
    """
    await ctx.send(response)
@bot.command(name='eco-tips')
async def info(ctx):
    response = """
    1. Разделяйте отходы - sorting
    Начните с разделения мусора на разные категории: органические отходы, пластик, стекло, бумага и металл.
    Узнайте о возможностях раздельного сбора мусора в вашем районе. Возможно, есть специальные баки или пункты приема.
    2. Сократите использование одноразовых предметов
    Постепенно отказывайтесь от одноразовых пластиковых пакетов, бутылок и посуды. Замените их многоразовыми аналогами, такими как тканевые сумки, металлические бутылки и стеклянные контейнеры.
    3. Используйте повторно
    Прежде чем выбросить вещь, подумайте, можно ли ее использовать повторно. Например, банки от консервов можно использовать для хранения мелочей или как контейнеры для растений.
    4. Покупайте товары без упаковки
    При возможности выбирайте товары, которые продаются без упаковки, или с минимальной упаковкой. Некоторые магазины предлагают опцию покупки на развес, что позволяет использовать собственные контейнеры.
    5. Планируйте покупки
    Планируйте покупки еды и других товаров заранее, чтобы избежать излишков и не покупать лишнее. Это поможет снизить количество пищевых отходов.
    6. Компостируйте органические отходы
    Если у вас есть сад или небольшой участок земли, начните компостировать органические отходы, такие как остатки овощей и фруктов, скорлупу яиц и кофейную гущу. Компостирование превращает органические отходы в полезное удобрение.
    7. Выбирайте многоразовые товары
    Замените одноразовые предметы в быту многоразовыми аналогами, например, используйте тканевые салфетки вместо бумажных, многоразовые губки и тряпки вместо одноразовых.
    8. Ремонтируйте и перерабатывайте
    Если что-то ломается, попробуйте сначала отремонтировать, прежде чем выбрасывать. Сломанные вещи также могут быть переработаны или использованы для других целей.
    9. Сократите использование пластика
    Попробуйте найти альтернативы пластиковым продуктам, например, используйте деревянные или металлические предметы вместо пластиковых.
    """
    await ctx.send(response)
@bot.command(name='decom')
async def info(ctx):
    response = """
    1. Пластиковая бутылка — 450 лет
    2. Стеклянная бутылка — более 1 миллиона лет
    3. Алюминиевая банка — 200-500 лет
    4. Газета — 2-6 недель
    5. Банановая кожура — 2-5 недель
    6. Бумажный стаканчик — 5-30 лет
    7. Сигаретный окурок — 1-5 лет
    8. Пластиковый пакет — 10-1000 лет
    9. Стеклянная банка — более 1 миллиона лет
    10. Одноразовый подгузник — 450 лет
    11. Жевательная резинка — 50 лет
    12. Пенопластовый стаканчик — 50 лет
    13. Деревянный брусок — 13 лет
    14. Консервная банка — 50 лет
    15. Бумажная упаковка — 2-4 недели
    16. Картон — 2 месяца
    17. Хлопчатобумажная ткань — 1-5 месяцев
    18. Шерстяная ткань — 1-5 лет
    19. Апельсиновая кожура — 6 месяцев
    20. Яичная скорлупа — 2 месяца
    21. Тетрадь — 2-6 недель
    22. Фольга — 200-500 лет
    23. Бумажный пакет — 1 месяц
    24. Картонная коробка — 2 месяца
    25. Кожаная обувь — 25-40 лет
    26. Полиэтиленовая пленка — 100-400 лет
    27. Автомобильные шины — 50-80 лет
    28. Старая одежда — 1-3 года
    29. Молочный пакет — 5 лет
    30. Зубная щетка — 500 лет
    31. Хлеб — 2-3 недели
    32. Чайный пакетик — 3-6 месяцев
    33. Кофейная гуща — 3 месяца
    34. Газонная трава — 2-6 недель
    35. Пластиковая крышка — 400 лет
    36. Стекловолокно — более 1 миллиона лет
    37. Металлический гвоздь — 10-20 лет
    38. Одноразовый пластиковый контейнер — 100 лет
    39. Тканевая салфетка — 1 год
    40. Резиновый мячик — 50 лет
    41. Мобильный телефон — 1000 лет
    42. CD-диск — 1 миллион лет
    43. Соломинка — 200 лет
    44. Картонная упаковка — 2 месяца
    45. Кухонная губка — 52 года
    46. Лоток для яиц — 2 месяца
    47. Деревянная ложка — 1 год
    48. Старая газета — 2-6 недель
    49. Металлическая проволока — 10-20 лет
    50. Пластиковая трубка — 500 лет
    51. Пенопласт — 500 лет
    52. Шинель — 3 года
    53. Фанера — 1-3 года
    54. Батарейка — 100 лет
    55. Голубое стекло — 1 миллион лет
    56. Полиэстер — 20-200 лет
    

  

    """
    await ctx.send(response)

@bot.command(name='sorting')
async def sorting(ctx):
    response = """
    Разделение отходов по разным сортирующим контейнерам является важным шагом для эффективной переработки и уменьшения вреда для окружающей среды. Вот основные типы контейнеров и что в них выбрасывать:

    1. Контейнер для бумаги (синий)
       - Что выбрасывать:
         - Газеты, журналы, книги
         - Грязную или жирную бумагу (например, от пиццы).
         - Обои.
         - Бумагу с покрытием (например, ламинированную или вощеную).

    2. Контейнер для пластика и металла (желтый)
       - Что выбрасывать:
         - Пластиковые бутылки и канистры.
         - Пластиковые контейнеры (например, от йогурта, шампуня).
       - Что не выбрасывать:
         - Пластик с остатками пищи или масла.
         - Батарейки и аккумуляторы.
         - Лампы и электронику.
    3. Контейнер для стекла (зеленый)
       - Что выбрасывать:
         - Стеклянные бутылки (от напитков, масла).
    4. Контейнер для органических отходов (коричневый)
       - Что выбрасывать:
         - Остатки овощей и фруктов.
         - Кофейную гущу и чайные пакетики.
         - Скорлупу яиц.
    5. Контейнер для смешанных отходов (серый или черный)
       - Что выбрасывать:
         - Все, что не подлежит переработке: загрязненные пищей пластик и бумага, одноразовые подгузники, изделия из керамики и фарфора, пыль и мелкий мусор, упаковки с комбинированными материалами (например, из фольги и пластика).
       - Что не выбрасывать:
         - Отходы, которые можно переработать (они должны быть выброшены в соответствующие контейнеры).
    6. Контейнер для опасных отходов (отдельный сбор)
       - Что выбрасывать:
         - Батарейки и аккумуляторы.
    """
    await ctx.send(response)


bot.run('MTI3MjIyMTMyMTQxNzE5NTU4MA.GVcpxh.KNu9NHqg38y0fstZ7-35bq_sdX5bpybcsVCoVE')