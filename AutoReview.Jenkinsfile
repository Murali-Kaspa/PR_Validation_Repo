pipeline {

    agent any

    stages {

        stage('Checkout PR') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                    python3 --version
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    . venv/bin/activate

                    if [ -f requirements.txt ]; then
                        pip install -r requirements.txt
                    fi
                '''
            }
        }

        stage('Validate Changes') {
            steps {
                sh '''
                    . venv/bin/activate

                    python scripts/validate_changes.py
                '''
            }
        }

    }

    post {

        success {
            echo '✅ PR validation passed successfully'
        }

        failure {
            echo '❌ PR validation failed. Please check the console logs.'
        }

        always {
            echo 'PR validation completed'
        }

    }

}
