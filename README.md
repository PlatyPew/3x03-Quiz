# Setting up the thingy

Download the plugins for owasp dependency checker and sonarqube (Manage Jenkins -> Plugins -> Available plugins).

Go to Sonarqube and generate a token (Administration -> Security -> Users -> Tokens).

Add the credentials to Jenkins (Manage Jenkins -> Credentials -> (global) -> Add Credentials).
Set the kind to "Secret text", and put the secret inside with the ID "sonar-token"

Set the SonarQube servers (Manage Jenkins -> System), set the name to "SonarQube", server url and the server authentication token to "sonar-token"

Set the SonarQube Scanner (Manage Jenkins -> Tools -> SonarQube Scanner installations). Set SonarQube Scanner name to "SonarQube", install automatically

Set the Dependency-Check installations (Manage Jenkins -> Tools -> Dependency-Check Installations). Set Name to "default", install automatically.

Click on New Item and Enter an item name. Set an item name and set to pipeline.

Click on Configure and set the pipeline to "Pipeline script from SCM". Set Repo URL (GitHub) and the script path to "jenkins/Jenkinsfile"

Yay you are done
