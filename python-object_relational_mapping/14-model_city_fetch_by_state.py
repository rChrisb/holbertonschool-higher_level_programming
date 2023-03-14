#!/usr/bin/python3
""" Cities in state"""


if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.orm import join

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2],
                                                    sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City, State).join(State, State.id == City.state_id).all()
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")
