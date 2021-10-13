--
-- PostgreSQL database dump
--
--
-- Dumped from database version 9.5.6
-- Dumped by pg_dump version 9.5.6

ALTER TABLE IF EXISTS ONLY public."user" DROP CONSTRAINT IF EXISTS pk_user_id CASCADE;

DROP TABLE IF EXISTS public."user";
CREATE TABLE "user" (
    id serial NOT NULL,
    name text,
    surname text,
    mail text,
    password text
);

ALTER TABLE ONLY "user"
    ADD CONSTRAINT pk_user_id PRIMARY KEY (id);

INSERT INTO "user" VALUES (0, 'Joe', 'Black', 'joe.black@yahoo.com', '$2b$12$udIf8lX4P5EkuYwLSTiZxuAV527ZOSHJvDIQ1wzlvuHO2sw41mzia');
INSERT INTO "user" VALUES (1, 'Ben', Null, 'ben@gmail.com', '$2b$12$nCLo/BYc3/GzX.E0SuvRhOreowM.Kn.Ha.NPKFBOA25ibcUW3h1Ky');
INSERT INTO "user" VALUES (2, 'Alice', 'Smith', 'alice123@wp.pl', '$2b$12$s3UjpNvw66eTC/E1ftbsyObURwPVe0i3LSIWwsNRfegB.PvLtp/by');
INSERT INTO "user" VALUES (7, 'wally-e', 'cleaning robot', 'wally-e@pixar.com', '$2b$12$Pnv9fMdAc8E7JS7PQNAyNuwgFaFSgEpvLA9PM9i5E5vW0CgjcwF6q');
