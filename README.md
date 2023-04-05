# Servet
### The market place for services

![services_page](https://ibb.co/yFrwGx4) 

Servet is a web application built by [Rahab](https://www.linkedin.com/in/mary-rahab/) and [Greenbel](https://www.linkedin.com/in/greenbele/) for service providers and seekers to connect. The idea behind its conception was that seekers of handy services such as hairdressing, plumbing, electrical and related services be able to quickly browse through services in the category they seek and available in their neighborhood and get the provider's contact, all in a few clicks. The end product is [Servet](https://github.io/Scaarif/ServetMVP/).

You can read more about **Servet**: the inspiration, challenges, lessons, hacks and general development process in the form of developers' reflections in the linked blogs below:
- [Frontend - Rahab](https:rahab_blog)
- [Backend - Greenbel](https:greenbel_blog)

## Story behind the Application
Just incase you don't have the time to go through the reflections, this is the short of the story behind the application.

You don’t realize how hard it can be to find a plumber, especially in estates and gated communities until 
you need one and suddenly, the seemingly just a call away plumber is calls to friends, family and 
strangers further away. Too much of a stretch? Ok, remember last time – You finally managed to leave your 
computer desk and decided to cook but all your knives were so blunt they were smashing the tomatoes 
instead of cutting them. How long did it take you to find the ‘knives’ guy, again? We’ve all been there, 
requiring a certain services - say, that of a plumber, or electrician – and that’s always when it dawns on 
us just what a nightmare we are in for - and for good reasons:
- We don’t know who to contact for the service.
- We know who to contact, but then the professional is not available for one reason or other – and the frustration begins!

The project is intended to solve this problem by connecting customers to a wider array of 
service providers, improving their odds of getting the services they need, when they need it and with ease.
While this project will connect customers to service providers, it will not [completely] solve the problem of ensuring that a required service is always available, and always delivered to the customer’s satisfaction.

**Note:** The application was developed in fulfillment of the [ALX Software Engineering](https://www.alxafrica.com/software-engineering/) programme end of foundations portfolio project requirement.


## Project installation
To be able to run and test the project yourself, clone the repository and run the following commands:
- ### Backend (Flask app)
  To run the Flask app, you'll need to have the following dependencies:
  * MySQL (prefarably version 8.0, but version 5.7 should work as well)
    On installation success:
    * create a database and user for the application
    * set the following environment variables: SERVET_USER, SERVET_PWD, SERVET_HOST, SERVET_DB for the database user, user password, host, and name respectively.
  * Python v3.8.2
  * Pip<br>
    To install:
    ```sh
    sudo apt-get install pip
    ```
  * SQLAlchemy v2.0.1
    ```sh
    pip install SQLAlchemy==2.0.1
    ```
  * Flask v2.2.2
    ```sh
    pip install Flask==2.2.2
    ```
  * Flask-SQLAlchemy v3.0.3
    ```sh
    pip install Flask-SQLAlchemy==3.0.3
    ```
  * Flask-Login v0.6.2
    ```sh
    pip install Flask-Login==0.6.2
    ```
  * Flask-Cors v3.0.10
    ```sh
    pip install Flask-Cors==3.0.10
    ```
  * Flask-WTF v1.0.1
    ```sh
    pip install Flask-WTF==1.0.1
    ```
  Once the dependencies are installed, `cd` into the directory of the cloned repository, and then `cd` into the `backend/` directory and run:
  ```sh
  python3 -m api.v1.views.application
  ```
  You can then use the service at localhost:5000

- ### Frontend (Vue app)
From inside the just cloned repository, ensure you have _node_ and _npm_ installed then:
```sh 
cd servetMVP

```
install the application's dependencies as in the dependencies file [package.json](https:github_link_to_file)
```sh 
npm install or npm i
```
then run the application
```sh 
npm run dev
```
**NOTE:** the application relies on the backend application for data. For the application to properly function, ensure the backend (_flask app_) application is already up and running by following the **steps described above**

## Usage
Once you've run the **frontend application** as described above, follow/open the application's domain link in your favorite browser. Then, the most important step - **_interact with the application_** :) Simple, right?

## Major Features
Some of the implemented features include:
### 
![features](https://ibb.co/yRhXC3Q)
- ### Browse/Filter Services
Filter services by category and location to get exactly the service you need and in your preferred location.
- ### Investigate a service
Investigate a specific service by reading through what other customers/seekers have to say about the service and go for the best possible
- ### Rate a service
Help other seekers get the best service possible by reviewing it (rating and commenting on it) once you've consumed said service.
- ### Post a service
Are you a service provider? Post the service(s) you offer and make them all the more accessible.
- ### Update a service
Make any necessary changes to a service (for service providers) to make them more accessible or attractive to clients.

## Contributing
While [Rahab](https://github.com/scaarif) worked on most of the frontend (_Vue app_) while [Greenbel](https://github.com/Coldplayz) worked on most of the backend (_Flask app_), both parties contributed to the other application's development in different capacities - whether it was debugging, brainstorming on approaches and in suggesting solutions.

## Related Projects
[~~To be added~~]

## Licensing
This project is licensed under the MIT License - see the [LICENSE](https://licence_link) file for details.

