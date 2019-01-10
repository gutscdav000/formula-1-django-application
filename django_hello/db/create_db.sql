create table public.circuits
(circuitid serial primary key ,
 circuitRef varchar(255) not null,
 name varchar(255) not null,
 location varchar(255) null,
 country varchar(255) null,
 lat float(8) null,
 lng float(8) null,
 alt integer null,
 url varchar(255) not null unique
);

create table public.constructor_results
  (
    constructorResultsId serial primary key,
    raceId integer references races(raceid) ON UPDATE CASCADE ON DELETE CASCADE,
    constructorId integer references constructors(constructorid) ON UPDATE CASCADE ON DELETE CASCADE,
    points float(8),
    status varchar(255)
  );


create table public.constructor_standings
  (
    constructorStandingsId serial primary key,
    raceId integer references races(raceid) ON UPDATE CASCADE ON DELETE CASCADE,
    constructorId integer references constructors(constructorId) ON UPDATE CASCADE ON DELETE CASCADE,
    points float(8),
    position integer,
    positionText varchar(255),
    wins integer not null default 0
  );



create table public.constructors
  (
    constructorId serial primary key,
    constructorRef varchar(255) not null,
    name varchar(255) not null unique,
    nationality varchar(255),
    url varchar(255) not null
  );

create table public.driver_standings
  (
    driverStandingsId serial primary key,
    raceId integer references races(raceid) ON UPDATE CASCADE ON DELETE CASCADE,
    driverId integer references drivers(driverid) ON UPDATE CASCADE ON DELETE CASCADE,
    points float(8) not null default 0,
    position integer,
    positionText varchar(255),
    wins integer not null default 0
  );

create table public.drivers
  (
    driverId serial primary key,
    driverRef varchar(255) not null,
    number integer,
    code varchar(3),
    forename varchar(255) not null,
    surname varchar(255) not null,
    dob date,
    nationality varchar(255),
    url varchar(255) not null unique
  );

create table public.lap_times
  (
    id serial primary key,
    raceId integer references races(raceid) ON UPDATE CASCADE ON DELETE CASCADE,
    driverId integer references drivers(driverid) ON UPDATE CASCADE ON DELETE CASCADE,
    lap integer not null,
    position integer,
    time varchar(255),
    milliseconds integer
  );

create table public.pit_stops
  (
    id serial primary key,
    raceId integer references races(raceid) ON UPDATE CASCADE ON DELETE CASCADE,
    driverId integer references drivers(driverid) ON UPDATE CASCADE ON DELETE CASCADE,
    stop integer not null,
    lap integer not null,
    time time not null,
    duration varchar(255),
    milliseconds integer
  );

create table public.qualifying
  (
    qualifyId serial primary key,
    raceId integer references races(raceid) ON UPDATE CASCADE ON DELETE CASCADE,
    driverId integer references drivers(driverid) ON UPDATE CASCADE ON DELETE CASCADE,
    constructorId integer references constructors(constructorid) ON UPDATE CASCADE ON DELETE CASCADE,
    number integer not null default 0,
    position integer,
    q1 varchar(255),
    q2 varchar(255),
    q3 varchar(255)
  );


create table public.races
  (
    raceId serial primary key,
    year integer not null default 0,
    round integer not null default 0,
    circuitId integer references circuits(circuitid) ON UPDATE CASCADE ON DELETE CASCADE,
    name varchar(255) not null,
    date date,
    time time,
    url varchar(255) unique
  );

create table public.results
  (
    resultId serial primary key,
    raceId integer references races(raceId) ON UPDATE CASCADE ON DELETE CASCADE,
    driverId integer references drivers(driverId) ON UPDATE CASCADE ON DELETE CASCADE,
    constructorId integer references constructors(constructorId) ON UPDATE CASCADE ON DELETE CASCADE,
    number integer,
    grid integer not null default 0,
    position integer,
    positionText varchar(255),
    positionOrder integer not null default 0,
    points float(8) not null default 0,
    laps integer not null default 0,
    time varchar(255),
    milliseconds integer,
    fastestLap integer,
    rank integer default 0,
    fastestLapTime varchar(255),
    fastestLapSpeed varchar(255),
    statusId integer
  );

create table public.seasons
  (
    year integer primary key default 0,
    url varchar(255) unique
  );


create table public.status
  (
    statusId serial primary key,
    status varchar(255) not null
  );



/*
this query is for moving
tables between schemas


UPDATE pg_catalog.pg_class
SET relnamespace = (SELECT oid FROM pg_catalog.pg_namespace
                    WHERE nspname = 'public')
WHERE relnamespace = (SELECT oid FROM pg_catalog.pg_namespace
                      WHERE nspname = 'f1_history')
AND relname = 'seasons';


UPDATE pg_catalog.pg_type
SET typnamespace = (SELECT oid FROM pg_catalog.pg_namespace
                    WHERE nspname = 'public')
WHERE typnamespace = (SELECT oid FROM pg_catalog.pg_namespace
                      WHERE nspname = 'f1_history')
AND typname = 'seasons';
*/

/* THis query finds the unused qualifyid's

select statusid as "this id", statusid + 1 as "next id" from status where statusid + 1 not in (
select statusid from status order by statusid) order by statusid;


*/


insert into races 
 values (990 , 2018 ,    14 ,        14 , 'Italian Grand Prix'            , '2018-09-02' , '13:10:00' , 'https://en.wikipedia.org/wiki/2018_Italian_Grand_Prix');
