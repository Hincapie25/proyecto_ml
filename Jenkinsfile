pipeline {
    agent any

    stages {

        stage('Ejecutar script directamente') {
            steps {
                sh '''
                python3 --version || apt-get update && apt-get install -y python3 python3-pip
                pip3 install -r requirements.txt
                python3 src/main.py
                '''
            }
        }

        stage('Guardar resultados') {
            steps {
                archiveArtifacts artifacts: 'outputs/*'
            }
        }
    }
}