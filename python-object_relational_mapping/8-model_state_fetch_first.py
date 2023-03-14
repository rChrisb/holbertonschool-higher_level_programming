#!/usr/bin/python3


"""First state"""

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

    if session.query(State)[0]:
        print(f"{session.query(State)[0].id}: {session.query(State)[0].name}")
    else:
        print("Nothing")
    session.close()
