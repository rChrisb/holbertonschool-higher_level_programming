-- Cities by States

SELECT cities.id, cities.name, states.name FROM states JOIN cities ORDER BY cities.id;