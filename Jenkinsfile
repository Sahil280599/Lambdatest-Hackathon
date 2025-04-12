pipeline {
    agent any
    
    environment {
        PYTHON_PATH = 'python3'
        VIRTUAL_ENV = 'venv'
    }
    
    stages {
        stage('Setup') {
            steps {
                sh '''
                    ${PYTHON_PATH} -m venv ${VIRTUAL_ENV}
                    . ${VIRTUAL_ENV}/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                sh '''
                    . ${VIRTUAL_ENV}/bin/activate
                    pytest -v -n auto --reruns 2 --html=report.html
                '''
            }
        }
        
        stage('Archive Reports') {
            steps {
                archiveArtifacts artifacts: 'report.html', fingerprint: true
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
        success {
            echo 'All tests passed successfully!'
        }
        failure {
            echo 'Some tests failed. Please check the test report.'
        }
    }
} 