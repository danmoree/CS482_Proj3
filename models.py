from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Video Table
class Video(db.Model):
    __tablename__ = 'video'
    videoCode = db.Column(db.Integer, primary_key=True)
    videoLength = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Video {self.videoCode}>'

# Model Table
class Model(db.Model):
    __tablename__ = 'model'
    modelNo = db.Column(db.String(10), primary_key=True)
    width = db.Column(db.Numeric(6, 2))
    height = db.Column(db.Numeric(6, 2))
    weight = db.Column(db.Numeric(6, 2))
    depth = db.Column(db.Numeric(6, 2))
    screenSize = db.Column(db.Numeric(6, 2))

    # One-to-many relationship with DigitalDisplay
    digital_displays = db.relationship('DigitalDisplay', backref='model', lazy=True)

    def __repr__(self):
        return f'<Model {self.modelNo}>'

# Site Table
class Site(db.Model):
    __tablename__ = 'site'
    siteCode = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(16))
    address = db.Column(db.String(100))
    phone = db.Column(db.String(16))

    def __repr__(self):
        return f'<Site {self.siteCode}>'

# DigitalDisplay Table
class DigitalDisplay(db.Model):
    __tablename__ = 'digital_display'
    serialNo = db.Column(db.String(10), primary_key=True)
    schedulerSystem = db.Column(db.String(10))
    modelNo = db.Column(db.String(10), db.ForeignKey('model.modelNo'))

    def __repr__(self):
        return f'<DigitalDisplay {self.serialNo}>'

# Client Table
class Client(db.Model):
    __tablename__ = 'client'
    clientId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    phone = db.Column(db.String(16))
    address = db.Column(db.String(100))

    def __repr__(self):
        return f'<Client {self.clientId}>'

# TechnicalSupport Table
class TechnicalSupport(db.Model):
    __tablename__ = 'technical_support'
    empId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    gender = db.Column(db.String(1))

    def __repr__(self):
        return f'<TechnicalSupport {self.empId}>'

# Administrator Table
class Administrator(db.Model):
    __tablename__ = 'administrator'
    empId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    gender = db.Column(db.String(1))

    def __repr__(self):
        return f'<Administrator {self.empId}>'

# Salesman Table
class Salesman(db.Model):
    __tablename__ = 'salesman'
    empId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    gender = db.Column(db.String(1))

    def __repr__(self):
        return f'<Salesman {self.empId}>'

# AirtimePackage Table
class AirtimePackage(db.Model):
    __tablename__ = 'airtime_package'
    packageId = db.Column(db.Integer, primary_key=True)
    packageClass = db.Column(db.String(16))
    startDate = db.Column(db.Date)
    lastDate = db.Column(db.Date)
    frequency = db.Column(db.Integer)
    videoCode = db.Column(db.Integer, db.ForeignKey('video.videoCode'))

    def __repr__(self):
        return f'<AirtimePackage {self.packageId}>'

# AdmWorkHours Table
class AdmWorkHours(db.Model):
    __tablename__ = 'adm_work_hours'
    empId = db.Column(db.Integer, db.ForeignKey('administrator.empId'), primary_key=True)
    day = db.Column(db.Date, primary_key=True)
    hours = db.Column(db.Numeric(4, 2))

    def __repr__(self):
        return f'<AdmWorkHours empId: {self.empId}, day: {self.day}>'

# Broadcasts Table
class Broadcasts(db.Model):
    __tablename__ = 'broadcasts'
    videoCode = db.Column(db.Integer, db.ForeignKey('video.videoCode'), primary_key=True)
    siteCode = db.Column(db.Integer, db.ForeignKey('site.siteCode'), primary_key=True)

    def __repr__(self):
        return f'<Broadcasts videoCode: {self.videoCode}, siteCode: {self.siteCode}>'

# Administers Table
class Administers(db.Model):
    __tablename__ = 'administers'
    empId = db.Column(db.Integer, db.ForeignKey('administrator.empId'), primary_key=True)
    siteCode = db.Column(db.Integer, db.ForeignKey('site.siteCode'), primary_key=True)

    def __repr__(self):
        return f'<Administers empId: {self.empId}, siteCode: {self.siteCode}>'

# Specializes Table
class Specializes(db.Model):
    __tablename__ = 'specializes'
    empId = db.Column(db.Integer, db.ForeignKey('technical_support.empId'), primary_key=True)
    modelNo = db.Column(db.String(10), db.ForeignKey('model.modelNo'), primary_key=True)

    def __repr__(self):
        return f'<Specializes empId: {self.empId}, modelNo: {self.modelNo}>'

# Purchases Table
class Purchases(db.Model):
    __tablename__ = 'purchases'
    clientId = db.Column(db.Integer, db.ForeignKey('client.clientId'), primary_key=True)
    empId = db.Column(db.Integer, db.ForeignKey('salesman.empId'), primary_key=True)
    packageId = db.Column(db.Integer, db.ForeignKey('airtime_package.packageId'), primary_key=True)
    commissionRate = db.Column(db.Numeric(4, 2))

    def __repr__(self):
        return f'<Purchases clientId: {self.clientId}, empId: {self.empId}, packageId: {self.packageId}>'

# Locates Table
class Locates(db.Model):
    __tablename__ = 'locates'
    serialNo = db.Column(db.String(10), db.ForeignKey('digital_display.serialNo'), primary_key=True)
    siteCode = db.Column(db.Integer, db.ForeignKey('site.siteCode'), primary_key=True)

    def __repr__(self):
        return f'<Locates serialNo: {self.serialNo}, siteCode: {self.siteCode}>'
