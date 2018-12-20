pipeline {
 agent any
stages {
 stage('CodeCheckout') {
 steps {
 script {
    checkout scm  
     }
    }
   }
 
 stage('Junit Test') {
            steps {
                sh 'mvn test'
            }
            post {
                always {
                    junit 'target/surefire-reports/*.xml'
                }
            }
        }
 
 stage("build & SonarQube analysis") {
            agent any
            steps {
              withSonarQubeEnv('My SonarQube Server') {
                sh 'mvn clean package sonar:sonar'
              }
            }
          }
   
 stage('build customer app code') { 
 steps {
  script {
   echo "Installing Java"
                sh 'sudo apt-get install -y default-jdk'
               
                    echo "Installing Maven"
                sh 'sudo apt-get -y install maven'
                sh 'mvn -B -DskipTests clean package'
        sh 'mvn clean install'
    }
  }
 }
 
 
 
 
 
 /*
   stage('docker images code') { 
 steps {
  script {
       sh 'docker build -t msshrinivas38/ninja-app .'
       sh "docker login --username=$env.username --password=$env.pwd"
       sh 'docker push msshrinivas38/ninja-app'
   sh 'sudo docker run -p 3000:8090 -d  msshrinivas38/ninja-app'
        
    }
  }
 }
*/
}
}

