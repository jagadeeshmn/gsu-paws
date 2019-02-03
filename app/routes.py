from flask import request, flash, jsonify
from app import app, db
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import Student, Course, Section
from flask_api import status
from datetime import datetime

def hash_password(password):
    return generate_password_hash(password)

def check_password(password,password_hash):
    return check_password_hash(password,password_hash)

@app.route('/studentslist_perdept',methods=['POST'])        
def studentslist_perdept():     
    try:
        return_data = []
        studentslist = Student.query.filter(Student.majorDept == request.json['dept']).all()
        if studentslist is not None:
            for application in studentslist:
                application_data = {}
                application_data['sid'] = application[0]
                application_data['fname'] = application[1]
                application_data['lname'] = application[2]
                return_data.append(application_data)
            return jsonify({'status':status.HTTP_200_OK,'data':return_data})
    except Exception as e:
        return jsonify({'status':status.HTTP_500_INTERNAL_SERVER_ERROR,'message':str(e)})
        # return jsonify({'status':status.HTTP_500_INTERNAL_SERVER_ERROR,'message':'Unable to get applications'})

@app.route('/login',methods=['POST'])
def login():
    try:
        student = Student.query.filter_by(email = request.json['email']).first()
        if student is None or not check_password(student.password,request.json['password']):
            return jsonify({'status': status.HTTP_401_UNAUTHORIZED,'message':'Invalid Credentials'})
        else:
            return jsonify({'status': status.HTTP_200_OK,'message':'Login successful','sid':student.sid})
    except:
        return jsonify({'status': status.HTTP_500_INTERNAL_SERVER_ERROR,'message':'Unable to login'})

@app.route('/paws_registration',methods=['POST'])        
def paws_registration():     
    try:
        for data in request.json:
            studentslist = Student.query.filter(Student.email == data['email']).first()
            if studentslist is None:
                password = hash_password(data['fname']+data['lname'])
                student = Student(
                    email=data['email'],
                    fname=data['fname'],
                    lname=data['lname'],
                    password=password,
                    address1 = data['address1'],
                    address2 = data['address2'],
                    city = data['city'],
                    state = data['state'],
                    zip = int(data['zip']),
                    sType = data['sType'],
                    majorDept = data['majorDept'],
                    gradAssistant = 'N'
                    )
                db.session.add(student)
                db.session.commit()
            else:
                return jsonify({'status': status.HTTP_404_NOT_FOUND,'message':'Already Registered'})
        return jsonify({'status': status.HTTP_200_OK,'message':'Registered Successfully'})
    except Exception as e:
        return jsonify({'status': status.HTTP_500_INTERNAL_SERVER_ERROR,'message':str(e)}) 

@app.route('/get_all_courses',methods=['POST'])
def get_all_courses():
    try:
        term = request.json['term']
        course_details = db.session.query(Course,Section).filter(Course.cno == Section.course_cpcrn).filter(Section.term == term).all()
        return_data = []
        for course in course_details:
            course_data={}
            course_data['crn'] = course.Section.crn
            course_data['cprefix'] = course.Section.cprefix
            course_data['cno'] = course.Course.cno
            course_data['ctitle'] = course.Course.ctitle
            course_data['chours'] = course.Course.chours
            course_data['days'] = course.Section.days
            course_data['starttime'] = course.Section.starttime
            course_data['endtime'] = course.Section.endtime
            course_data['room'] = course.Section.room
            course_data['cap'] = course.Section.cap
            course_data['instructor'] = course.Section.instructor
            return_data.append(course_data)
        return jsonify({'status':status.HTTP_200_OK,'data':return_data})
    except:
        return jsonify({status:status.HTTP_500_INTERNAL_SERVER_ERROR,'message':'Unable to get courses'})


           
