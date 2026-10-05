DROP DATABASE IF EXISTS doom_bot;
CREATE DATABASE doom_bot;
USE doom_bot;

/* Plataforma de origen (WhatsApp, Telegram, Zulip, GLPI) */
CREATE TABLE IF NOT EXISTS origin(
    id INT AUTO_INCREMENT NOT NULL,
    name VARCHAR(100) NOT NULL,
    CONSTRAINT PRIMARY KEY(id)
);

/* Usuarios identificados según su origen */
CREATE TABLE IF NOT EXISTS users(
    id INT AUTO_INCREMENT NOT NULL,
    name VARCHAR(100) NOT NULL,
    identity VARCHAR(100) NOT NULL UNIQUE, /* Ej: ID de Telegram, Celular WhatsApp */
    id_origin INT NOT NULL,
    CONSTRAINT FOREIGN KEY(id_origin) REFERENCES origin(id) ON DELETE CASCADE,
    CONSTRAINT PRIMARY KEY(id)
);

/* Flujos de trabajo / Soporte */
CREATE TABLE IF NOT EXISTS process(
    id INT AUTO_INCREMENT NOT NULL,
    name VARCHAR(100) NOT NULL,
    CONSTRAINT PRIMARY KEY(id)
);

/* Pasos dentro de un proceso (Estado en la máquina de estados) */
CREATE TABLE IF NOT EXISTS steps(
    id INT AUTO_INCREMENT NOT NULL,
    name VARCHAR(100) NOT NULL,
    id_process INT NOT NULL,
    CONSTRAINT FOREIGN KEY(id_process) REFERENCES process(id) ON DELETE CASCADE,
    CONSTRAINT PRIMARY KEY(id)
);

/* Sesión de Chat / Ticket activo */ 
CREATE TABLE IF NOT EXISTS chats(
    id INT AUTO_INCREMENT NOT NULL,
    serial VARCHAR(100) NOT NULL UNIQUE,
    status BOOLEAN NOT NULL DEFAULT TRUE,
    date_start DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    date_end DATETIME NULL, /* Permite NULL mientras el chat siga activo */
    id_process INT NOT NULL,
    id_steps INT NOT NULL,
    CONSTRAINT FOREIGN KEY(id_process) REFERENCES process(id),
    CONSTRAINT FOREIGN KEY(id_steps) REFERENCES steps(id),
    CONSTRAINT PRIMARY KEY(id)
);

/* Auditoría de eventos del chat */ 
CREATE TABLE IF NOT EXISTS logs_chats(
    id INT AUTO_INCREMENT NOT NULL,
    id_chat INT NOT NULL,
    content TEXT NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT FOREIGN KEY(id_chat) REFERENCES chats(id) ON DELETE CASCADE, 
    CONSTRAINT PRIMARY KEY(id)
);

/* Mensajes intercambiados en la sesión */
CREATE TABLE IF NOT EXISTS messages(
    id INT AUTO_INCREMENT NOT NULL,
    message TEXT NOT NULL,
    id_transmitter INT NOT NULL, /* ID del usuario que envía el mensaje */ 
    date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    id_chat INT NOT NULL,
    CONSTRAINT FOREIGN KEY(id_transmitter) REFERENCES users(id),
    CONSTRAINT FOREIGN KEY(id_chat) REFERENCES chats(id) ON DELETE CASCADE, /* Corregido: apunta a chats*/ 
    CONSTRAINT PRIMARY KEY(id)
);

/* Participantes del chat (Cliente, Agente, Bot) */
CREATE TABLE IF NOT EXISTS participants(
    id INT AUTO_INCREMENT NOT NULL,
    id_user INT NOT NULL,
    id_chat INT NOT NULL,
    CONSTRAINT FOREIGN KEY(id_user) REFERENCES users(id) ON DELETE CASCADE,
    CONSTRAINT FOREIGN KEY(id_chat) REFERENCES chats(id) ON DELETE CASCADE, 
    CONSTRAINT UNIQUE(id_user, id_chat), /* Evita duplicados de participantes en un mismo chat */
    CONSTRAINT PRIMARY KEY(id)
);