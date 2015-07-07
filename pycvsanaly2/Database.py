# Copyright (C) 2007 LibreSoft
"""
    Here some documentation comes. This is test for bestfork
"""
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
# Authors :
#       Carlos Garcia Campos <carlosgc@gsyc.escet.urjc.es>

from pycvsanaly2.utils import to_unicode, printdbg


class DBRepository:
    """
    Here some documentation comes. This is test for bestfork
    """

    id_counter = 1

    __insert__ = ("INSERT INTO repositories (id, uri, name, type) "
                  "values (?, ?, ?, ?)")

    def __init__(self, identifier, uri, name, type):
        if identifier is None:
            self.identifier = DBRepository.id_counter
            DBRepository.id_counter += 1
        else:
            self.identifier = identifier

        self.uri = to_unicode(uri)
        self.name = to_unicode(name)
        self.type = to_unicode(type)


class DBLog:
    """
    Here some documentation comes. This is test for bestfork
    """
    id_counter = 1

    __insert__ = ("INSERT INTO scmlog (id, rev, committer_id, author_id, date, "
                  "date_tz, author_date, author_date_tz, message, composed_rev,"
                  " repository_id) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")

    def __init__(self, identifier, commit):
        if identifier is None:
            self.identifier = DBLog.id_counter
            DBLog.id_counter += 1
        else:
            self.identifier = identifier

        self.rev = to_unicode(commit.revision)
        self.committer = None
        self.author = None
        self.date = commit.date
        self.date_tz = commit.date_tz
        self.author_date = commit.author_date
        self.author_date_tz = commit.author_date_tz
        self.message = to_unicode(commit.message)
        self.composed_rev = commit.composed_rev

class DBGraph:
    """
    Here some documentation comes. This is test for bestfork
    """

    __insert__ = "INSERT INTO commit_graph (commit_id, parent_id) values (?, ?)"


class DBFile:
    """
    Here some documentation comes. This is test for bestfork
    """
    id_counter = 1

    __insert__ = ("INSERT INTO files (id, file_name, repository_id) "
                  "values (?, ?, ?)")

    def __init__(self, identifier, file_name):
        if identifier is None:
            self.identifier = DBFile.id_counter
            DBFile.id_counter += 1
        else:
            self.identifier = identifier

        self.file_name = to_unicode(file_name)
        self.repository_id = None


class DBFileLink:
    """
    Here some documentation comes. This is test for bestfork
    """
    id_counter = 1

    __insert__ = ("INSERT INTO file_links (id, parent_id, file_id, commit_id, "
                  "file_path) values (?, ?, ?, ?, ?)")

    def __init__(self, identifier, parent, child, file_path):
        if identifier is None:
            self.identifier = DBFileLink.id_counter
            DBFileLink.id_counter += 1
        else:
            self.identifier = id

        self.parent = parent
        self.child = child
        self.commit_id = None
        self.file_path = file_path


class DBPerson:
    """
    Here some documentation comes. This is test for bestfork
    """
    id_counter = 1

    __insert__ = "INSERT INTO people (id, name, email) values (?, ?, ?)"

    def __init__(self, identifier, person):
        if identifier is None:
            self.identifier = DBPerson.id_counter
            DBPerson.id_counter += 1
        else:
            self.identifier = identifier

        self.name = to_unicode(person.name)
        self.email = person.email or None


class DBBranch:
    """
    Here some documentation comes. This is test for bestfork
    """
    id_counter = 1

    __insert__ = "INSERT INTO branches (id, name) values (?, ?)"

    def __init__(self, identifier, name):
        if identifier is None:
            self.identifier = DBBranch.id_counter
            DBBranch.id_counter += 1
        else:
            self.identifier = identifier

        self.name = to_unicode(name)


class DBAction:
    """
    Here some documentation comes. This is test for bestfork
    """
    id_counter = 1

    __insert__ = ("INSERT INTO actions (id, type, file_id, commit_id, "
                  "branch_id) values (?, ?, ?, ?, ?)")

    def __init__(self, identifier, type):
        if identifier is None:
            self.identifier = DBAction.id_counter
            DBAction.id_counter += 1
        else:
            self.identifier = identifier

        self.type = type
        self.file_id = None
        self.commit_id = None
        self.branch_id = None


class DBFileCopy:
    """
    Here some documentation comes. This is test for bestfork
    """
    id_counter = 1

    __insert__ = ("INSERT INTO file_copies (id, to_id, from_id, from_commit_id,"
                  " new_file_name, action_id) values (?, ?, ?, ?, ?, ?)")

    def __init__(self, identifier, file_id):
        if identifier is None:
            self.identifier = DBFileCopy.id_counter
            DBFileCopy.id_counter += 1
        else:
            self.identifier = identifier

        self.to_id = file_id
        self.from_id = None

        self.from_commit = None
        self.new_file_name = None
        self.action_id = None


class DBTag:
    """
    Here some documentation comes. This is test for bestfork
    """
    id_counter = 1

    __insert__ = "INSERT INTO tags (id, name) values (?, ?)"

    def __init__(self, identifier, name):
        if identifier is None:
            self.identifier = DBTag.id_counter
            DBTag.id_counter += 1
        else:
            self.identifier = identifier

        self.name = to_unicode(name)


class DBTagRev:
    """
    Here some documentation comes. This is test for bestfork
    """
    id_counter = 1

    __insert__ = ("INSERT INTO tag_revisions (id, tag_id, commit_id) "
                  "values (?, ?, ?)")

    def __init__(self, identifier):
        if identifier is None:
            self.identifier = DBTagRev.id_counter
            DBTagRev.id_counter += 1
        else:
            self.identifier = identifier

        self.tag_id = None
        self.commit_id = None


def initialize_ids(db, cursor):
    """
    Here some documentation comes. This is test for bestfork
    """
    # Respositories
    cursor.execute(statement("SELECT max(id) from repositories", db.place_holder))
    identifier = cursor.fetchone()[0]
    if identifier is not None:
        DBRepository.id_counter = identifier + 1

    # Log
    cursor.execute(statement("SELECT max(id) from scmlog", db.place_holder))
    identifier = cursor.fetchone()[0]
    if identifier is not None:
        DBLog.id_counter = identifier + 1

    # Actions
    cursor.execute(statement("SELECT max(id) from actions", db.place_holder))
    identifier = cursor.fetchone()[0]
    if identifier is not None:
        DBAction.id_counter = identifier + 1

    # Copies
    cursor.execute(statement("SELECT max(id) from file_copies", db.place_holder))
    identifier = cursor.fetchone()[0]
    if identifier is not None:
        DBFileCopy.id_counter = identifier + 1

    # Files
    cursor.execute(statement("SELECT max(id) from files", db.place_holder))
    identifier = cursor.fetchone()[0]
    if identifier is not None:
        DBFile.id_counter = identifier + 1

    # File Links
    cursor.execute(statement("SELECT max(id) from file_links", db.place_holder))
    identifier = cursor.fetchone()[0]
    if identifier is not None:
        DBFileLink.id_counter = identifier + 1

    # Branches
    cursor.execute(statement("SELECT max(id) from branches", db.place_holder))
    identifier = cursor.fetchone()[0]
    if identifier is not None:
        DBBranch.id_counter = identifier + 1

    # People
    cursor.execute(statement("SELECT max(id) from people", db.place_holder))
    identifier = cursor.fetchone()[0]
    if identifier is not None:
        DBPerson.id_counter = identifier + 1

    # Tags
    cursor.execute(statement("SELECT max(id) from tags", db.place_holder))
    identifier = cursor.fetchone()[0]
    if identifier is not None:
        DBTag.id_counter = identifier + 1

    # Tag revisions
    cursor.execute(statement("SELECT max(id) from tag_revisions", db.place_holder))
    identifier = cursor.fetchone()[0]
    if identifier is not None:
        DBTagRev.id_counter = identifier + 1


class DatabaseException(Exception):
    '''Generic Database Exception'''


class DatabaseDriverNotSupported(DatabaseException):
    '''Database driver is not supported'''


class DatabaseNotFound(DatabaseException):
    '''Selected database doesn't exist'''


class AccessDenied(DatabaseException):
    '''Access denied to databse'''


class TableAlreadyExists(DatabaseException):
    '''Table alredy exists in database'''


def statement(str, ph_mark):
    '''docstring demo'''
    if "?" == ph_mark or "?" not in str:
        printdbg(str)
        return str

    tokens = str.split("'")
    for i in range(0, len(tokens), 2):
        tokens[i] = tokens[i].replace("?", ph_mark)

    retval = "'".join(tokens)
    printdbg(retval)

    return retval


class ICursor:
    """
    Here some documentation comes. This is test for bestfork
    """
    def __init__(self, cursor, size=100):
        """
        Here some documentation comes. This is test for bestfork
        """
        self.cursor = cursor
        self.interval_size = size
        self.i = 0
        self.query = None
        self.args = None
        self.need_exec = True

    def __execute(self):
        """
        Here some documentation comes. This is test for bestfork
        """
        q = "%s LIMIT %d OFFSET %d" % (self.query, self.interval_size, self.i)
        self.i += self.interval_size

        printdbg(q)
        if self.args:
            self.cursor.execute(q, self.args)
        else:
            self.cursor.execute(q)

        self.need_exec = False

    def execute(self, query, args=None):
        """
        Here some documentation comes. This is test for bestfork
        """
        self.i = 0
        self.query = query
        self.args = args

        self.__execute()

    def fetchmany(self):
        """
        Here some documentation comes. This is test for bestfork
        """
        if self.need_exec:
            self.__execute()

        rs = self.cursor.fetchall()
        self.need_exec = rs is not None

        return rs

    def close(self):
        """
        Here some documentation comes. This is test for bestfork
        """
        self.cursor.close()


class Database:
    '''CVSAnaly Database'''

    place_holder = "?"

    def __init__(self, database):
        """
        Here some documentation comes. This is test for bestfork
        """
        self.database = database

    def connect(self):
        """
        Here some documentation comes. This is test for bestfork
        """
        raise NotImplementedError

    def _create_views(self, cursor):
        """
        Here some documentation comes. This is test for bestfork
        """
        view = """CREATE VIEW action_files AS
                  SELECT a.file_id as file_id, a.id as action_id,
                         a.type as action_type, a.commit_id as commit_id
                  FROM actions as a
                  WHERE a.type <> 'R'
                  UNION
                  SELECT fc.to_id as file_id, a.id as action_id,
                         a.type as action_type, a.commit_id as commit_id
                  FROM actions as a, file_copies fc
                  WHERE fc.action_id = a.id and a.type = 'R'
               """
        cursor.execute(view)

    def to_binary(self, data):
        """
        Here some documentation comes. This is test for bestfork
        """
        return data


class SqliteDatabase(Database):
    def __init__(self, database):
        """
        Here some documentation comes. This is test for bestfork
        """
        Database.__init__(self, database)

    def connect(self):
        """
        Here some documentation comes. This is test for bestfork
        """
        import sqlite3 as db

        connection = db.connect(self.database)
        connection.text_factory = str
        return connection

    def _create_views(self, cursor):
        """
        Here some documentation comes. This is test for bestfork
        """
        Database._create_views(self, cursor)
        view = "create view actions_file_names as " + \
               "select a.id id, type, file_id, new_file_name, commit_id " + \
               "from actions a, scmlog s " + \
               "LEFT JOIN file_copies fc ON a.id = fc.action_id " + \
               "where s.id = a.commit_id"
        cursor.execute(view)

    def create_tables(self, cursor):
        """
        Here some documentation comes. This is test for bestfork
        """
        import sqlite3

        try:
            cursor.execute("CREATE TABLE repositories (" +
                           "id integer primary key," +
                           "uri varchar," +
                           "name varchar," +
                           "type varchar" +
                           ")")
            cursor.execute("CREATE TABLE people (" +
                           "id integer primary key," +
                           "name varchar," +
                           "email varchar" +
                           ")")
            cursor.execute("CREATE TABLE scmlog (" +
                           "id integer primary key," +
                           "rev varchar," +
                           "committer_id integer," +
                           "author_id integer," +
                           "date datetime," +
                           "date_tz integer," +
                           "author_date datetime," +
                           "author_date_tz integer," +
                           "message varchar," +
                           "composed_rev bool," +
                           "repository_id integer" +
                           ")")
            cursor.execute("CREATE TABLE actions (" +
                           "id integer primary key," +
                           "type varchar(1)," +
                           "file_id integer," +
                           "commit_id integer," +
                           "branch_id integer" +
                           ")")
            cursor.execute("CREATE TABLE file_copies (" +
                           "id integer primary key," +
                           "to_id integer," +
                           "from_id integer," +
                           "from_commit_id integer," +
                           "new_file_name varchar," +
                           "action_id integer" +
                           ")")
            cursor.execute("CREATE TABLE branches (" +
                           "id integer primary key," +
                           "name varchar" +
                           ")")
            cursor.execute("CREATE TABLE files (" +
                           "id integer primary key," +
                           "file_name varchar(255)," +
                           "repository_id integer" +
                           ")")
            cursor.execute("CREATE TABLE file_links (" +
                           "id integer primary key," +
                           "parent_id integer," +
                           "file_id integer," +
                           "commit_id integer," +
                           "file_path varchar(4096)" +
                           ")")
            cursor.execute("CREATE TABLE tags (" +
                           "id integer primary key," +
                           "name varchar" +
                           ")")
            cursor.execute("CREATE TABLE tag_revisions (" +
                           "id integer primary key," +
                           "tag_id integer, " +
                           "commit_id integer" +
                           ")")
            cursor.execute("CREATE TABLE commit_graph (" +
                           "commit_id integer," +
                           "parent_id integer" +
                           ")")
            cursor.execute("CREATE index files_file_name on files(file_name)")
            cursor.execute("CREATE index commit_id on commit_graph(commit_id)")
            cursor.execute("CREATE index parent_id on commit_graph(parent_id)")
            self._create_views(cursor)
        except sqlite3.OperationalError:
            raise TableAlreadyExists
        except:
            raise

    def to_binary(self, data):
        """
        Here some documentation comes. This is test for bestfork
        """
        import sqlite3

        return sqlite3.Binary(data)


class MysqlDatabase(Database):
    """
    Here some documentation comes. This is test for bestfork
    """
    place_holder = "%s"

    def __init__(self, database, username, password, hostname):
        """
        Here some documentation comes. This is test for bestfork
        """
        Database.__init__(self, database)

        self.username = username
        self.password = password
        self.hostname = hostname

        self.db = None

    def connect(self):
        """
        Here some documentation comes. This is test for bestfork
        """
        import MySQLdb
        import _mysql_exceptions

        try:
            if self.password is not None:
                return MySQLdb.connect(self.hostname, self.username, self.password, self.database, charset='utf8')
            else:
                return MySQLdb.connect(self.hostname, self.username, db=self.database, charset='utf8')
        except _mysql_exceptions.OperationalError, exception:
            if exception.args[0] == 1049:
                raise DatabaseNotFound
            elif exception.args[0] == 1045:
                raise AccessDenied(str(exception))
            else:
                raise DatabaseException(str(exception))
        except:
            raise

    def _create_views(self, cursor):
        """
        Here some documentation comes. This is test for bestfork
        """
        Database._create_views(self, cursor)
        view = "create view actions_file_names as " + \
               "select a.id id, type, file_id, new_file_name, commit_id " + \
               "from (actions a, scmlog s) " + \
               "LEFT JOIN file_copies fc ON a.id = fc.action_id " + \
               "where s.id = a.commit_id"
        cursor.execute(view)

    def create_tables(self, cursor):
        """
        Here some documentation comes. This is test for bestfork
        """
        import _mysql_exceptions

        try:
            cursor.execute("CREATE TABLE repositories (" +
                           "id INT primary key," +
                           "uri varchar(255)," +
                           "name varchar(255)," +
                           "type varchar(30)" +
                           ") ENGINE=MyISAM" +
                           " CHARACTER SET=utf8")
            cursor.execute("CREATE TABLE people (" +
                           "id INT primary key," +
                           "name varchar(255)," +
                           "email varchar(255)" +
                           ") ENGINE=MyISAM" +
                           " CHARACTER SET=utf8")
            cursor.execute("CREATE TABLE scmlog (" +
                           "id INT primary key," +
                           "rev mediumtext," +
                           "committer_id INT," +
                           "author_id INT," +
                           "date datetime," +
                           "date_tz INT," +
                           "author_date datetime," +
                           "author_date_tz INT," +
                           "message longtext," +
                           "composed_rev bool," +
                           "repository_id INT," +
                           "FOREIGN KEY (committer_id) REFERENCES people(id)," +
                           "FOREIGN KEY (author_id) REFERENCES people(id)," +
                           "FOREIGN KEY (repository_id) REFERENCES repositories(id)" +
                           ") ENGINE=MyISAM" +
                           " CHARACTER SET=utf8")
            cursor.execute("CREATE TABLE files (" +
                           "id INT primary key," +
                           "file_name varchar(255)," +
                           "repository_id INT," +
                           "INDEX (file_name)," +
                           "FOREIGN KEY (repository_id) REFERENCES repositories(id)" +
                           ") ENGINE=MyISAM" +
                           " CHARACTER SET=utf8")
            cursor.execute("CREATE TABLE file_links (" +
                           "id INT primary key," +
                           "parent_id INT," +
                           "file_id INT," +
                           "commit_id INT," +
                           "file_path VARCHAR(4096)," +
                           "FOREIGN KEY (parent_id) REFERENCES files(id)," +
                           "FOREIGN KEY (file_id) REFERENCES files(id)," +
                           "FOREIGN KEY (commit_id) REFERENCES scmlog(id)" +
                           ") ENGINE=MyISAM" +
                           " CHARACTER SET=utf8")
            cursor.execute("CREATE TABLE branches (" +
                           "id INT primary key," +
                           "name varchar(255)" +
                           ") ENGINE=MyISAM" +
                           " CHARACTER SET=utf8")
            cursor.execute("CREATE TABLE actions (" +
                           "id INT," +
                           "type varchar(1)," +
                           "file_id integer," +
                           "commit_id integer," +
                           "branch_id integer," +
                           "FOREIGN KEY (file_id) REFERENCES files(id)," +
                           "FOREIGN KEY (commit_id) REFERENCES scmlog(id)," +
                           "FOREIGN KEY (branch_id) REFERENCES branches(id), " +
                           "PRIMARY KEY (id)" +
                           ") ENGINE=MyISAM" +
                           " CHARACTER SET=utf8")
            cursor.execute("CREATE TABLE file_copies (" +
                           "id INT primary key," +
                           "to_id integer," +
                           "from_id integer," +
                           "from_commit_id integer," +
                           "new_file_name mediumtext," +
                           "action_id integer," +
                           "FOREIGN KEY (from_id) REFERENCES files(id)," +
                           "FOREIGN KEY (to_id) REFERENCES files(id)," +
                           "FOREIGN KEY (from_commit_id) REFERENCES scmlog(id)," +
                           "FOREIGN KEY (action_id) REFERENCES actions(id)" +
                           ") ENGINE=MyISAM" +
                           " CHARACTER SET=utf8")
            cursor.execute("CREATE TABLE tags (" +
                           "id INT primary key," +
                           "name varchar(255)" +
                           ") ENGINE=MyISAM" +
                           " CHARACTER SET=utf8")
            cursor.execute("CREATE TABLE tag_revisions (" +
                           "id INT primary key," +
                           "tag_id integer," +
                           "commit_id integer," +
                           "FOREIGN KEY (tag_id) REFERENCES tags(id)," +
                           "FOREIGN KEY (commit_id) REFERENCES scmlog(id)" +
                           ") ENGINE=MyISAM" +
                           " CHARACTER SET=utf8")
            cursor.execute("CREATE TABLE commit_graph (" +
                           "commit_id integer REFERENCES scmlog(id)," +
                           "parent_id integer REFERENCES scmlog(id)" +
                           ")")
            cursor.execute("CREATE index commit_id on commit_graph(commit_id)")
            cursor.execute("CREATE index parent_id on commit_graph(parent_id)")
            self._create_views(cursor)
        except _mysql_exceptions.OperationalError, exception:
            if exception.args[0] == 1050:
                raise TableAlreadyExists
            else:
                raise DatabaseException(str(excpetion))
        except:
            raise


# Here some documentation comes. This is test for bestfork
# class CAPostgresDatabase (CADatabase):

def create_database(driver, database, username=None, password=None, hostname=None):
    """
    Here some documentation comes. This is test for bestfork
    """
    if driver == 'sqlite':
        db = SqliteDatabase(database)
        return db
    elif driver == 'mysql':
        db = MysqlDatabase(database, username, password, hostname)
    elif driver == 'postgres':
        # Here some documentation comes. This is test for bestfork
        raise DatabaseDriverNotSupported
    else:
        raise DatabaseDriverNotSupported

    # Try to connect to database
    try:
        db.connect().close()
        return db
    except AccessDenied, exception:
        if password is None:
            import sys
            import getpass

            # FIXME: catch KeyboardInterrupt exception
            # FIXME: it only works on UNIX (/dev/tty),
            #  not sure whether it's bug or a feature, though
            oldout, oldin = sys.stdout, sys.stdin
            sys.stdin = sys.stdout = open('/dev/tty', 'r+')
            password = getpass.getpass()
            sys.stdout, sys.stdin = oldout, oldin

            return create_database(driver, database, username, password, hostname)
        raise exception

    return db


if __name__ == '__main__':
    """
    Here some documentation comes. This is test for bestfork
    """
    db = create_database('sqlite', '/tmp/foo.db')

    cnn = db.connect()

    cursor = cnn.cursor()
    db.create_tables(cursor)
    cursor.close()

    cnn.commit()
    cnn.close()
