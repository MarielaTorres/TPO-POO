CREATE TABLE IF NOT EXISTS persona (
    id_persona INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS organizador (
    id_persona INTEGER PRIMARY KEY,
    empresa TEXT NOT NULL,
    FOREIGN KEY (id_persona) REFERENCES persona(id_persona)
);

CREATE TABLE IF NOT EXISTS speaker (
    id_persona INTEGER PRIMARY KEY,
    especialidad TEXT NOT NULL,
    biografia TEXT,
    FOREIGN KEY (id_persona) REFERENCES persona(id_persona)
);

CREATE TABLE IF NOT EXISTS asistente (
    id_persona INTEGER PRIMARY KEY,
    dni TEXT NOT NULL UNIQUE,
    FOREIGN KEY (id_persona) REFERENCES persona(id_persona)
);

CREATE TABLE IF NOT EXISTS evento (
    id_evento INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    fecha TEXT NOT NULL,
    lugar TEXT NOT NULL,
    capacidad INTEGER NOT NULL CHECK (capacidad > 0),
    id_organizador INTEGER NOT NULL,
    FOREIGN KEY (id_organizador)
        REFERENCES organizador(id_persona)
);

CREATE TABLE IF NOT EXISTS sala (
    id_sala INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    capacidad INTEGER NOT NULL CHECK (capacidad > 0),
    id_evento INTEGER NOT NULL,
    FOREIGN KEY (id_evento) REFERENCES evento(id_evento),
    UNIQUE (id_sala, id_evento)
);

CREATE TABLE IF NOT EXISTS charla (
    id_charla INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    horario_inicio TEXT NOT NULL,
    horario_fin TEXT NOT NULL,
    id_evento INTEGER NOT NULL,
    id_speaker INTEGER,
    id_sala INTEGER,
    CHECK (horario_fin > horario_inicio),
    FOREIGN KEY (id_evento) REFERENCES evento(id_evento),
    FOREIGN KEY (id_speaker) REFERENCES speaker(id_persona),
    FOREIGN KEY (id_sala, id_evento)
        REFERENCES sala(id_sala, id_evento)
);

CREATE TABLE IF NOT EXISTS inscripcion (
    id_inscripcion INTEGER PRIMARY KEY AUTOINCREMENT,
    id_asistente INTEGER NOT NULL,
    id_evento INTEGER NOT NULL,
    fecha TEXT NOT NULL,
    estado TEXT NOT NULL DEFAULT 'Pendiente'
        CHECK (estado IN ('Pendiente', 'Confirmada', 'Cancelada')),
    FOREIGN KEY (id_asistente) REFERENCES asistente(id_persona),
    FOREIGN KEY (id_evento) REFERENCES evento(id_evento),
    UNIQUE (id_asistente, id_evento)
);
