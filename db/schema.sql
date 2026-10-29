CREATE DATABASE IF NOT EXISTS eventmanager
CHARACTER SET utf8mb4;

USE eventmanager;

-- Personas
CREATE TABLE IF NOT EXISTS persona (
    id_persona INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE
) ENGINE=InnoDB;

-- Organizadores
CREATE TABLE IF NOT EXISTS organizador (
    id_persona INT PRIMARY KEY,
    empresa VARCHAR(150) NOT NULL,
    FOREIGN KEY (id_persona)
        REFERENCES persona(id_persona)
) ENGINE=InnoDB;

-- Speakers
CREATE TABLE IF NOT EXISTS speaker (
    id_persona INT PRIMARY KEY,
    especialidad VARCHAR(100) NOT NULL,
    biografia TEXT,
    FOREIGN KEY (id_persona)
        REFERENCES persona(id_persona)
) ENGINE=InnoDB;

-- Asistentes
CREATE TABLE IF NOT EXISTS asistente (
    id_persona INT PRIMARY KEY,
    dni VARCHAR(20) NOT NULL UNIQUE,

    CONSTRAINT fk_asistente_persona
        FOREIGN KEY (id_persona)
        REFERENCES persona(id_persona)
) ENGINE=InnoDB;

-- Eventos
CREATE TABLE IF NOT EXISTS evento (
    id_evento INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    fecha DATE NOT NULL,
    lugar VARCHAR(150) NOT NULL,
    capacidad INT NOT NULL,
    id_organizador INT NOT NULL,

    CHECK (capacidad > 0),

    FOREIGN KEY (id_organizador)
        REFERENCES organizador(id_persona)
) ENGINE=InnoDB;

-- Salas
CREATE TABLE IF NOT EXISTS sala (
    id_sala INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    capacidad INT NOT NULL,
    id_evento INT NOT NULL,

    CHECK (capacidad > 0),

    UNIQUE (id_sala, id_evento),

    FOREIGN KEY (id_evento)
        REFERENCES evento(id_evento)
) ENGINE=InnoDB;

-- Charlas
CREATE TABLE IF NOT EXISTS charla (
    id_charla INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150) NOT NULL,
    horario_inicio DATETIME NOT NULL,
    horario_fin DATETIME NOT NULL,
    id_evento INT NOT NULL,
    id_speaker INT,
    id_sala INT,

    CHECK (horario_fin > horario_inicio),

    FOREIGN KEY (id_evento)
        REFERENCES evento(id_evento),

    FOREIGN KEY (id_speaker)
        REFERENCES speaker(id_persona),

    FOREIGN KEY (id_sala, id_evento)
        REFERENCES sala(id_sala, id_evento)
) ENGINE=InnoDB;

-- Inscripciones
CREATE TABLE IF NOT EXISTS inscripcion (
    id_inscripcion INT AUTO_INCREMENT PRIMARY KEY,
    id_asistente INT NOT NULL,
    id_evento INT NOT NULL,
    fecha DATE NOT NULL,
    estado VARCHAR(20) NOT NULL DEFAULT 'Pendiente',

    CHECK (
        estado IN ('Pendiente', 'Confirmada', 'Cancelada')
    ),

    UNIQUE (id_asistente, id_evento),

    FOREIGN KEY (id_asistente)
        REFERENCES asistente(id_persona),

    FOREIGN KEY (id_evento)
        REFERENCES evento(id_evento)
) ENGINE=InnoDB;
