create schema if not exists app;

DROP TABLE IF EXISTS app.ft_commits;

  CREATE TABLE app.ft_commits (
    id VARCHAR(50) NOT NULL PRIMARY KEY,
    author VARCHAR(50) NOT NULL,
    datetime TIMESTAMP NOT NULL,
    message TEXT
);

create index datetime on app.ft_commits (datetime);

create index author on app.ft_commits using hash (author);