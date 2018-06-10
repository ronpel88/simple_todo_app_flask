# simple todo app application + CI/CD using aws, jenkins, docker, ansible

## prerequisites
----

### prerequisites - web application (codewise):  
  * project should be based on python and including tests  
  * code should be pushed to github (public repo)  

## prerequisites in jenkins server:  
----

### server general configuration -   
1. aws security group - expose ssh access from local pc (My ip)  
2. aws security group - expose TCP 8080 access from local pc (My ip)  

### jenkins - 
1. install java, jenkins

### github -   
1. generate ssh key  
2. add public key to github deploy keys  
3. add <jenkins url>/github-webhook/ to github Integrations & services  
4. add <jenkins url>/github-webhook/ to github Webhooks  
5. in jenkins ui - install plugins: github-plugin, git plugin  
6. aws security group - expose TCP 8080 access from github ip  

### docker -   
1. install docker  

### ansible -   
1. install ansible (also python, docker if not exist)  
2. in jenkins ui - install ansible plugin  


## prerequisites in the app server:
----

### anisble - 
1. install python, docker, docker-py  
2. generate ssh key  
3. copy public key and add to authorized_keys in jenkins server  
4. aws security group - expose ssh access from jenkins server  

### application -   
1. aws security group - expose access to anyone that want to access application (80, 0.0.0.0/0) 

----

# CI/CD -
creation of ci/cd job -  
* create a new job. job configuration:   
  - github project - add repo url  
  - parameters: VERSION (release), IMAGE_NAME (name of the image which will be displayed in docker hub)  
  - SCM - git, add repo url, branch
  - Build triggers section - check GitHub hook trigger for GITScm  polling  
  - Build section - execute shell script:  
    ## ci:  
      - install the required python libraries for project  
      - run python tests using pytest  
      - build docker image according to Dockerfile  
      - tag the created image with docker hub repo name, release version, build number  
      - push the created image to docker hub  
    ## cd:  
      - run ansible playbook witch do as followed:  
        playbook:  
        pull docker image from docker hub  
        stop existing container (if exist)  
        start  container from the image we pull, ports 80==>5050  
        inventory:  
        inventory should contain a group which called todo_app, with the aws server inner ip and the user  
 
 
 ### the end :) ENJOY...