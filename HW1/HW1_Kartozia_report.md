## Отчёт ДЗ №1, Картозия
#### В наличии:
- [Навигация](nlp_Kartozia/homeworks.md)
- [_KeyWords](./HW1_Kartozia_KeyWords.txt) (ключевые слова взяты из RuCorTestSet/TestSet/Lenta/2013_04_02_daughter_.txt)
- [_WordListTest](./HW1_Kartozia_WordListTest.txt)
- [таблица к заданию 1.2](./HW1_Kartozia_12.xlsx)
- [таблица к заданию 1.3](./HW1_Kartozia_13.xlsx)
- [таблица к заданию 1.4](./HW1_Kartozia_14.xlsx)
- отчёт

#### Ответы на вопрос к заданию 1.1:
1. Есть ли среди выбранных вами ключевых слов редкие слова?
  Можно посчитать слово *преемник* за редкое, слова *твиттер* в частотном словаре нет, я посчитала его частотность по запросу в НКРЯ. *Но оно скорее не редкое, а просто новое*
2.  Есть ли среди выбранных вами слов слова, вошедшие в топ 500 по частоте?
  *президент* **(326/500)**
3.  К каким частям речи относятся выбранные вами слова, слов какой части речи больше?
  Большинство слов относятся к существительным

#### Ответ на вопрос к заданию 1.2:
в таблице [HW1_Kartozia_12](./HW1_Kartozia_12.xlsx) выделены красным.

#### Ответы на вопросы задания 1.3:
1. Соответствуют ли те слова, которые попали вверх списка, упорядоченного по убыванию tf.idf, Вашей интуиции? 
  Дочь соответствует, но вот я предполагала, что президент обгонит вице-премьера
2. Все ли ключевые слова попали в верхнюю часть списка (в первые шесть слов), ранжированного по tf.idf?
  да
3. Какие слова попали вниз ранжированного списка? Каковы их характеристики с точки зрения грамматических характеристик, семантики.
  Вниз попали самые частотные, которые брались не из текста а из частотного словаря. "Сказать" — глагол, обозначающий произнесение высказывания.
  Все — местоимение со значение всеобщности.
4. Как, по-вашему, должен быть устроен список «стоп»-слов, данные о которых нет смысла включать в таблицу?
  Я уже так устала, что не могу придумать

#### Ответ на вопрос к заданию 1.4:
1. Отличаются ли диаграммы для самых частотных в языке слов и для слов с высоким tf.idf в Вашем списке, если отличаются, то чем?
  Да, слова с высоким tf.idf имеют более резкие перепады в значения (где-то они не встречаются совсем, где-то их кол-во мизерное или относительно большое).
  Высокочастотные слова более менее всегда на одном уровне.

