<img width="100%" src="https://i.imgur.com/CYx9Es5.png" />

# Full Stack Capstone Project

Throughout this course, you have built a strong foundation in full-stack software development, mastering the essential technologies and concepts that power modern web applications. From structuring web pages with HTML and styling them with CSS to adding interactivity with JavaScript, you've gained the skills to craft dynamic and engaging user experiences. On the backend, you’ve worked with Python, PostgreSQL, and the Django web framework to build robust and scalable applications, leveraging Django REST Framework to create powerful APIs that connect frontend and backend systems.

Beyond the technical skills, you've also explored software development best practices — writing clean and maintainable code, handling user authentication and security, managing databases efficiently, and deploying web applications. Now, as you approach your final project, it’s time to bring all these elements together. This capstone is your opportunity to showcase your full-stack expertise, demonstrating not only your technical proficiency but also your ability to design, develop, and deploy a complete, functional web application from scratch.

## Schedule
- Project Days: Wednesday, October 29th - Thursday, November 6th 
- Project time: 9:00am - 5:00pm
- Daily standups: 9:00am and 1:00pm
- Final presentations: 
  - Thursday, November 6th - 9:00am - 5:00pm 
  - 15 minutes max, each
  - End of Course Survey
  - End of Course Awards

## Technical Requirements

### Planning
- ERD Diagram representing all (3) models in your application.
  - **User Model Does Not Count!**
- RESTful Routing Table for **both** Client and Server.
  - should have full CRUD for at least two models
- User Stories you intend to implement.

> Project planning is due on Wednesday October 29th. 

> **Hint =>** Think about what you are creating! Figure out your tables / relationships before you create anything else. Your data and their relationships will decide how the entire appliction is designed! If you are not sure, start with a User story!

### Full Stack:
- User Authentication and Authorization with JSON Web Token
  - Routes and Models should be protected accordingly
- Have consistent and properly indented code.	
- Have functions and variables that are named sensibly.	
- No remaining dead and/or commented out code.
  - (you can leave code that is purposeful / adds to the program)
  - just do not leave unneccessary code that no longer serves a purpose
- Code is well organized and indented properly.

### Frontend: Javascript, React
- Communicates with Django backend
- Utilizes React Router
- Implement user stories
- Create intuitive UI/UX
- Handle API responses and errors
- Dockerize the application
  
### Backend: Python, DjangoRestFramework, PostgreSQL Database
- Implement a minimum three related Django models
  - should have full CRUD __between__ all models
  - **User Model Does Not Count!**
- Create RESTful API endpoints using DRF
- Include proper error handling and status codes
- Testing Suite of your choice
  - (choose from the several we cover in class.)
- Configure environment variables as needed
- Enable CORS for our React frontend
- Implements Django MVC workflow
- Dockerize the applications
  - one container for React / Frontend
  - one container for DjangoRF / Backend

## GitHub Requirements / Documentation
- Front End Repository:
    - Minimum 10 meaningful commits
    - Front End README must include:
        - Project & Repository descriptions
        - Tech stack
        - Backend Repo Link
        - Link to Deployed Site
        - Installation Instructions as Needed (docker)
        - IceBox Features
  
- Backend End Repository:
    - Minimum 10 meaningful commits
    - Backend README must include:
        - Project & Repository descriptions
        - Tech stack
        - Front End Repo Link
        - Link to Deployed Site
        - ERD diagram
        - Routing Table
        - Installation Instructions as Needed (docker)
        - IceBox Features

## Presentation Requirements
- Launch the front end app via the README.md file
- Logout / Login / Signup a User w/ JWT
- Live Demo showing CRUD and relationships
- Show important / favorite code in front and back
- Share key challenges / what you learned.
- Future / IceBox Features you would like to implement.

> **HINT =>** You can use notes to help / organize your presentation. Don't be afraid to prepare yourself and set yourself up for success! Write down words, phrases, or guide for how you would like to approach presenting.

> **HINT =>** The presentation is your opportunity to explain how you were able to use web technologies to create the application and its functionality. While explaining how these pieces fit together you should use the technical terms and concepts to support clarifying your development process and how database relationships allow for your project to operate properly. From there you can emphasize specific functionality that is likely unique to your project and the challenges related to figuring out how to implement that feature. Use what you have learned in class to express to others the knowledge obtained over the last 9 weeks.

## Grading
- Each of the above items will be graded on a scale from 0 - 3
- 0 = not having the item at all
- 1 = an attempt was made, but information is incomplete
- 2 = satisfactory / hits minimal requirements
- Maximum of 90 points
- **CHATGPT USAGE** 
  - -> YOU WILL LOSE POINTS FOR EXCESSIVE CHATGPT USAGE
  - -> YOU SHOULD NOT NEED TO USE IT TO WRITE THE CODE TO GET THROUGH THIS PROJECT
  - -> USING IT TO UNDERSTAND A CONCEPT OR EXPLAIN AN IDEA IS GOOD
  - -> USING IT TO DO YOUR WORK IS NOT.. 
  - -> WE WILL DEDUCT UP TO **5 POINTS** IF WE CAN TELL THAT YOUR ARE USING IT


>> It is your job as the developer to ensure that your project operates properly. You should be manually testing each feature as you implement it and fix any issues that may come up on the way. If a feature or expectation is not working properly, you will lose points. 

## Academic Integrity
- Complete work independently
- Properly cite resources
- Ask instructors when stuck
- No copying code
- Document external resources

>> You may refer to code in previous projects from the course, especially for the backend / django rest framework, as there is code that will be nearly identical for every person in the class because we all work with Django and React. You should NOT be using identical code from your frontend, though. Your React application is based on the project idea and the models / how they are related. This will determine what information needs to be on which pages and how many pages / components you will need. Thoroughly planning for your project will set you up for success.

## Getting Help
GitHub issues are the most useful method for answering technical questions. Issues should follow this format:

```text
I tried ___.
I expected ___ to happen.
___ happened instead.
My repo link is ___ and my question is about lines ___.
```

## Resources

- [Django docs](https://docs.djangoproject.com/en/5.1/)
- [DRF docs](https://www.django-rest-framework.org/)
- [React docs](https://react.dev/learn)
- [Docker docs](https://docs.docker.com/guides/)
- [Testing guides](https://docs.djangoproject.com/en/5.1/topics/testing/)
