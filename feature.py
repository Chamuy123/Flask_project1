from flask import Flask

FAI=Flask(__name__)

@FAI.route('/stringresponse')
def stringresponse():
    return 'This is the first flask project'

@FAI.route('/SecondStringresponse')
def SecondStringresponse():
    return 'This is the Second flask project'

if __name__ == '__main__':
    FAI.run(debug=True)
