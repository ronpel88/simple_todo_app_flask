# Simple todo app application + CI/CD using aws, jenkins, docker, ansible

## Project description - 
1. Setup a CI flow for web application
2. Build and deploy the project as a docker container

## Prerequisites
----
### Prerequisites - web application (codewise):  
1. Project should be based on python and including tests  
2. Code should be pushed to github (public repo)  

## Prerequisites in jenkins server:  
### Server general configuration -   
1. AWS security group - expose ssh access from local pc (My ip)  
2. AWS security group - expose TCP 8080 access from local pc (My ip)  

### Jenkins - 
1. Install java, jenkins

### Github -   
1. Generate ssh key  
2. Add public key to github deploy keys  
3. Add <jenkins url>/github-webhook/ to github Integrations & services  
4. Add <jenkins url>/github-webhook/ to github Webhooks  
5. In jenkins ui - install plugins: github-plugin, git plugin  
6. AWS security group - expose TCP 8080 access from github ip  

### Docker -   
1. Install docker  

### Ansible -   
1. Install ansible (also python, docker if not exist)  
2. In jenkins ui - install ansible plugin  


## Prerequisites in the app server:
### Anisble - 
1. Install python, docker, docker-py  
2. Generate ssh key  
3. Copy public key and add to authorized_keys in jenkins server  
4. AWS security group - expose ssh access from jenkins server  

### application -   
1. AWS security group - expose access to anyone that want to access application (80, 0.0.0.0/0) 
----

# CI/CD -
Creation of ci/cd job -  
* Create a new job. job configuration:   
  - Github project - add repo url  
  - Parameters: VERSION (release), IMAGE_NAME (name of the image which will be displayed in docker hub)  
  - SCM - git, add repo url, branch
  - Build triggers section - check GitHub hook trigger for GITScm  polling  
  - Build section - execute shell script:  
    ## CI:  
      - Install the required python libraries for project  
      - Run python tests using pytest  
      - Build docker image according to Dockerfile  
      - Tag the created image with docker hub repo name, release version, build number  
      - Push the created image to docker hub  
    ## CD:  
      - Run ansible playbook witch do as followed:  
        * Playbook:  
          Pull docker image from docker hub  
          Stop existing container (if exist)  
          Start  container from the image we pull, ports 80==>5050  
        * Inventory:  
          Inventory should contain a group which called todo_app, with the aws server inner ip and the user  
 
 
 ### Ehe end :) ENJOY...