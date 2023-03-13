-- Cities by States

SELECT cities.id, cities.name, states.name FROM states JOIN cities ON cities.state_id = states.id ORDER BY cities.id;