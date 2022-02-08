pipeline {
    agent { label 'agent_1' }
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/alphacoder-io/worldofgames.git', branch: 'master'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t  worldofgames /var/jenkins_home/worker/workspace/worldofgames'
            }
        }
        stage('Run') {
            steps {
                sh 'docker rm -f worldofgames'
                sh 'docker run --rm -d -p:8777:80 --name worldofgames worldofgames'
            }
        }
        stage ('Test') {
            steps {
                sh 'docker exec worldofgames python3 tests/e2e.py'
               }
        }
        stage('Finalize') {
            steps {
                sh 'docker rm -f worldofgames'
                sh 'docker login --username alphacoderio --password 12345'
                sh 'docker push alphacoderio/worldofgames'
            }
        }
    }
}