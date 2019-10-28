from labaratory2.app import db


class ormPersons(db.Model):
    __tablename__ = 'orm_person'

    person_login = db.Column(db.String(50), primary_key=True)
    person_password = db.Column(db.String(32), nullable=False)
    person_name = db.Column(db.String(50), nullable=False)
    person_surname = db.Column(db.String(50), nullable=False)
    person_email = db.Column(db.String(50), nullable=True)
    person_birthday = db.Column(db.Date, nullable=False)

    Persons_Function = db.relationship("ormFunction")


class ormFunction(db.Model):
    __tablename__ = 'orm_function'

    function_name = db.Column(db.String(100), primary_key=True)
    person_text = db.Column(db.String(1000), nullable=False)
    counter_of_tests = db.Column(db.Integer, nullable=False)

    person_login_fk = db.Column(db.String(50), db.ForeignKey('orm_person.person_login'))

    Function_TescCase = db.relationship("ormTestCase")

    project = db.relationship("ormProject",
                               secondary="orm_projectfunction")


class ormTestCase(db.Model):
    __tablename__ = 'orm_testcase'

    testcase_id = db.Column(db.Integer, primary_key=True)

    function_name_fk = db.Column(db.String(100), db.ForeignKey('orm_function.function_name'))

    TestCase_Parameters = db.relationship("ormParameters")
    TestCase_Result = db.relationship("ormResult")


class ormParameters(db.Model):
    __tablename__ = 'orm_parameters'

    parameters_index = db.Column(db.Integer, primary_key=True)
    testcase_iteration = db.Column(db.Integer, nullable=False)
    parameters_value = db.Column(db.String(100), nullable=False)

    testcase_id = db.Column(db.Integer, db.ForeignKey('orm_testcase.testcase_id'), primary_key=True)


class ormResult(db.Model):
    __tablename__ = 'orm_result'

    result_value = db.Column(db.Integer, nullable=False)
    testcase_iteration = db.Column(db.Integer, primary_key=True)

    testcase_id = db.Column(db.Integer, db.ForeignKey('orm_testcase.testcase_id'), primary_key=True)


class ormProject(db.Model):
    __tablename__ = 'orm_project'

    project_name = db.Column(db.String(50), primary_key=True)
    project_cost = db.Column(db.Integer, nullable=False)
    project_lider = db.Column(db.String(100), nullable=False)
    project_department = db.Column(db.String(100), nullable=False)

    function = db.relationship("ormFunction",
                            secondary="orm_projectfunction")


class ormProjectFunction(db.Model):
    __tablename__ = 'orm_projectfunction'

    project = db.Column(db.String(50), db.ForeignKey("orm_project.project_name"), primary_key=True)
    function = db.Column(db.String(100), db.ForeignKey("orm_function.function_name"), primary_key=True)



