CREATE DATABASE IF NOT EXISTS figures_db;
CREATE USER IF NOT EXISTS 'user'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON figures_db.* TO 'user'@'%';
FLUSH PRIVILEGES;

USE figures_db;

CREATE TABLE IF NOT EXISTS figures (
    id INT PRIMARY KEY AUTO_INCREMENT,
    type ENUM('rectangle', 'circle', 'triangle') NOT NULL,
    color VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS figure_dimensions (
    figure_id INT PRIMARY KEY,
    height INT DEFAULT NULL,
    width INT DEFAULT NULL,
    radius INT DEFAULT NULL,
    FOREIGN KEY (figure_id) REFERENCES figures(id) ON DELETE CASCADE
);

