# Проект по оценочным словам на основе корпуса отзывов на рестораны

## Команда Актимель
* [Картозия Инга](github.com/kartozia)
* [Мельник Анастасия](github.com/NastyaMelnik57)
* [Бибаева Мария](github.com/mbibaeva)
* [Уэтова Екатерина](github.com/euetova)

## Задача
Расширить изначальный [список оценочных слов](https://github.com/mbibaeva/nlp_Kartozia/blob/master/Project_4th_year/seed.txt)
## Ход работы

- [x] Разметка текстов
[1](https://github.com/mbibaeva/nlp_Kartozia/blob/master/Project_4th_year/annotation_Kartozia%20(1).txt),
[2](https://github.com/mbibaeva/nlp_Kartozia/blob/master/Project_4th_year/annotation_Bibaeva.csv),
[3](https://github.com/mbibaeva/nlp_Kartozia/blob/master/Project_4th_year/annotation_Uetova_27221%2C%2029097%2C%2023065%2C%2038116.txt),
[4](https://github.com/mbibaeva/nlp_Kartozia/blob/master/Project_4th_year/14418.txt)

- [x] Извлечены тексты плюс оценки по аспектам

- [x] Предобработка текстов: лемматизация, удалены стоп-слова

- [x] [Рассчитаны tf-idf](https://github.com/mbibaeva/nlp_Kartozia/blob/master/Project_4th_year/sentiment_dic.ipynb) [результат]

- [x] Обучена [word2vec модель](https://github.com/mbibaeva/nlp_Kartozia/blob/master/Project_4th_year/Sentiment_Analysis.ipynb)

- [ ] Представить каждое слово в виде вектора, и обучить SVM на векторах слов, закодированных числами частях речи (слова, двух слов до и двух слов после), и векторах двух слов до и двух слов после, и целевой переменной (0,1,2: neg, neutral, pos)

- [ ] Обучить w2v, найти ближайшие слова к словам из seed.

- [ ] Topic modeling

- [ ] Сравнить с [десятитысячным списком](https://github.com/mbibaeva/nlp_Kartozia/blob/master/Project_4th_year/rusentilex.txt)

Выбираем тексты с самыми высокими оценками по аспекту food и отдельно с самыми низкими, и потом делаем по ним частотный список и ура
