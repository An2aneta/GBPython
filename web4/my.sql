CREATE TABLE CLASSMATE (
  Id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  adress TEXT NOT NULL
);

INSERT INTO CLASSMATE VALUES (0001, 'Иван', '18', 'Москва, Ленинский проспект 1');
INSERT INTO CLASSMATE VALUES (0002, 'Елена', '24', 'Санкт-Петербург, Невский проспект 1');
INSERT INTO CLASSMATE VALUES (0003, 'Мария', '35', 'Москва, Ленинский проспект 2');
INSERT INTO CLASSMATE VALUES (0004, 'Егор', '38', 'Москва, Мичуринский проспект 1');
INSERT INTO CLASSMATE VALUES (0005, 'Александра', '27', 'Красноярск, Сиреневый бульвар 1');
INSERT INTO CLASSMATE VALUES (0006, 'Михаил', '19', 'Нижний Новгород, Ленинский проспект 2');

SELECT name FROM CLASSMATE WHERE age >= 18 and age < 30 and adress LIKE '%москва%';
