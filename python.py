pipeline {
agent any
stages {
stage('build') {
  steps {
echo 'building python application...'
}
}

stage('test') {
steps {
echo 'python application is test'
}
}

stage('deploy') {
steps {
echo 'python application is deploy'
}
}

stage('port') {
steps {
echo 'python application is using 5000 port'
}
}
}
}
