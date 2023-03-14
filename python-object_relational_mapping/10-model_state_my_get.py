#!/usr/bin/python3


"""Get a State"""

if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    import sys

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2],
                                                    sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_found = session.query(State).filter(State.name == sys.argv[4]).first()
    if state_found:
        print(state_found.id)
    else:
        print("Not found")
