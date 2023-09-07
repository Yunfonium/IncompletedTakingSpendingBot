CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT UNIQUE,
    user_telegram_id BIGINT NOT NULL UNIQUE,
    PRIMARY KEY (id)
    );

CREATE TABLE if not exists records (
    Id INT NOT NULL AUTO_INCREMENT,
    User_id INT NOT NULL,
    Year INT NOT NULL,
    Month INT NOT NULL,
    Day INT NOT NULL,
    Cost INT NOT NULL ,
    Description varchar(255),
    PRIMARY KEY (Id)
    );