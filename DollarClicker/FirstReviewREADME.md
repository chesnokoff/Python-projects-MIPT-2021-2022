# Python-projects-MIPT-2021-2022

1) Описание структуры проекта. В данном проекте реализован простой кликер с
   помощью графической библиотеки kivy. Файл design.kv предназначен для
   создания каркаса программы(аналог html файла). Файл main.py выполняет
   функциональную часть проекта.

2) Запуск. Для старта необходимо запустить main.py файл, предварительно скачав
   библиотеку kivy.

```
pip install kivy

cd DollarClicker

python main.py
```

3) Игровой процесс. В игре можно набирать деньги с помощью нажатия на пробел и
   его удерживания, или кнопки с помощью кнопки "Create one dollar". Заработав
   определенную сумму, Вы можете купить новые кликеры, которые будут делать за
   вас работу.

4) Дополнительные подробности реализации. Реализован полноценный event loop, то
   есть нет торможения из-за купленных кликеров, так как для них создается свой
   поток.
