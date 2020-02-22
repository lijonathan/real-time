# Real Time Project

CSE 530
  - Justin Marshall
  - Jeremy Manin
  - Jonathan Li

[![N|Solid](https://fitsmallbusiness.com/wp-content/uploads/2019/01/AWS-Amplify-Reviews-150x150.jpg)](https://console.aws.amazon.com/amplify/home?region=us-east-1#/) [![N|Solid](https://cdn3.iconfinder.com/data/icons/logos-3/250/angular-128.png)](https://angular.io/)

### Tech
* [AngularJS] - HTML enhanced for web apps!

### How to Start App
Open a terminal (Gitbash, Powershell, Not cmd)
Run the first command to make sure you have angular
Second one starts the application locally

```sh
$ npm install -g @angular/cli
$ ng serve
```
### If you are getting errors make sure you have the correct versions of node and npm
  - Verify that you are running at least Node.js version 8.x or greater and npm version 5.x or greater by running
```sh
$ npm -v
$ node -v
```

####Starting the Backend
```sh
$ amplify status --will show you what you've added already and if it's locally configured or deployed
$ amplify add <category> --will allow you to add features like user login or a backend API
$ amplify push --will build all your local backend resources and provision it in the cloud
$ amplify console --to open the Amplify Console and view your project status
$ amplify publish --will build all your local backend and frontend resources (if you have hosting category added) and provision it in the cloud
```
Pro tip:
Try amplify add api to create a backend API and then amplify publish to deploy everything


