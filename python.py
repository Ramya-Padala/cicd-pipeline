pipeline {
agent any
stages {
stage('build') {
echo 'building python application...'
}
}
stages {
stage('test') {
echo 'python application is test'
}
stages {
stage('deploy') {
echo 'python application is deploy'
}
}
stages {
stage('port') {
echo 'python application is using 5000 port'
}
}
}
