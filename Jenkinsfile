pipeline {
    agent any

    stages {

        stage('Instalar Python') {
            steps {
                sh '''
                apt-get update
                apt-get install -y python3 python3-pip
                '''
            }
        }

        stage('Instalar dependencias') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Ejecutar modelo') {
            steps {
                sh 'python3 src/main.py'
            }
        }

        stage('Guardar resultados') {
            steps {
                archiveArtifacts artifacts: 'outputs/*'
            }
        }
    }
}