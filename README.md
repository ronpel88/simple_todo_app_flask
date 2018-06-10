# Simple todo app application + CI/CD using aws, jenkins, docker, ansible

## Project description - 
1. Setup a CI flow for web application
2. Build and deploy the project as a Docker container

## Prerequisites
----
### Prerequisites - web application (codewise):  
1. Project should be based on Python and including tests  
2. Code should be pushed to Github (public repo)  

### Prerequisites - servers
Launch 2 ubuntu servers in AWS console - Jenkins server and app server  

## Prerequisites in Jenkins server:  
### Server general configuration -   
1. AWS security group - expose ssh access from local pc (My ip)  
2. AWS security group - expose TCP 8080 access from local pc (My ip)  

### Jenkins - 
1. Install Java, Jenkins

### Github -   
1. Generate ssh key  
2. Add public key to Github deploy keys  
3. Add <jenkins url>/github-webhook/ to Github Integrations & services  
4. Add <jenkins url>/github-webhook/ to Github Webhooks  
5. In jenkins ui - install plugins: github-plugin, git plugin  
6. AWS security group - expose TCP 8080 access from Github ip  

### Docker -   
1. Install Docker  

### Ansible -   
1. Install Ansible (also Python, Docker if not exist)  
2. In Jenkins ui - install Ansible plugin  


## Prerequisites in app server:
### Anisble - 
1. Install Python, Docker, docker-py  
2. Generate ssh key  
3. Copy public key and add to authorized_keys in Jenkins server  
4. AWS security group - expose ssh access from Jenkins server  

### application -   
1. AWS security group - expose access to anyone that want to access application (80, 0.0.0.0/0) 
----
# CI/CD -
Creation of CI/CD job -  
* Create a new job in Jenkins. job configuration:   
  - Github project - add repo url  
  - Parameters: VERSION (release), IMAGE_NAME (name of the image which will be displayed in docker hub)  
  - SCM - Git, add repo url, branch
  - Build triggers section - check GitHub hook trigger for GITScm  polling  
  - Build section - execute shell script:  
    ## CI:  
      - Install the required Python libraries for project  
      - Run Python tests using pytest  
      - Build Docker image according to Dockerfile  
      - Tag the created image with Docker hub repo name, release version, build number  
      - Push the created image to Docker hub  
    ## CD:  
      - Run Ansible playbook witch do as followed:  
        * Playbook:  
          Pull docker image from Docker hub  
          Stop existing container (if exist)  
          Start container from the image we pull, ports 80==>5050  
        * Inventory:  
          Inventory should contain a group which called todo_app, with the aws server inner ip and the user  
 
 
 ### Ehe end :) ENJOY...