pipeline {
    agent any

    stages {

        stage('Ejecutar con Docker') {
            steps {
                sh '''
                docker run --rm -v /var/jenkins_home/workspace/proyecto_ml:/app -w /app python:3.10 bash -c "
                pip install -r requirements.txt &&
                python src/main.py
                "
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