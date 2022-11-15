import nox


@nox.session
def tests(session):
    """
    run unittest
    """
    session.run("python3", "-m", "unittest", "discover", "src", "--verbose")


#


@nox.session
def lint(session):
    """
    run pylint
    """
    session.install("pylint")
    session.run("pylint", "./src")


#
