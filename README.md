# Project Nexus - My ALX Backend Journey

Hey there! This is where I am  documenting everything I have  learned in the ALX ProDev Backend Engineering Program. It's been quite the experience - lots of time in  debugging, and lots of "why this is not wokring ?" moments, and thankfully some real breakthroughs too.

I wanted to put this together not just as a portfolio piece, but as a way to track how much I've actually grown as a developer. Looking back at some of my early code... well, let's just say I've come a long way.

## 💼 What This Program is All About

The **ProDev Backend Engineering Program** taught us how to build real backend systems from the ground up it was next level of backend development a level where things get harder and need lots of work and late nights . At first we started with  some **Python**, and   useful tools like **generators** to make our code cleaner .

We also learned how to write **SQL queries** to work with databases, and spent a lot of time using **Django**  in building amazing projects like the airbnb apis ,it is  a powerful web framework. We didn’t just stop at the basics — we also learned about more advanced features like **Django forms** and knowing how things work behind the scenes.

Building **APIs** was a big part of the program — both **REST** and **GraphQL**.  and we used **Docker** to run our apps in containers, and set up **CI/CD pipelines** to test and deploy our code automatically. and **shell scripting** too  for automating tasks.

One of the best parts in this journey  was working with other learners hwo were nice and gave alot of help  . discussing  problems, giving and getting feedback, and building projects  and the exprets ones helped me  understand things more deeply.


## The Tech Stack I Got Comfortable With

**Core Languages & Frameworks:**
- Python became my daily driver - still amazed at how readable and powerful it is
- Django for web development - the admin panel alone sold me on this framework
- Django REST Framework for API development - once you get the serializers down, it's incredibly productive

**The Game Changers:**
- GraphQL - priviously i only used restAPI but  GraphQL completely changed how I think about API design and data fetching
- Docker - finally understood why everyone was so excited about containers witch it was very hard for me to understand 
- Redis for caching - nothing beats that performance boost when you implement it right

**DevOps & Deployment:**
- GitHub Actions and Jenkins for CI/CD - automation is addictive once you get it working
- Learning to write proper tests (yes, I was that person who skipped them initially)

## Key Concepts That Actually Stuck

**Database Work:** Spent a lot of time getting comfortable with database design patterns, learning when to normalize vs denormalize, and figuring out how to write queries that don't bring your server to its knees.

**Async Programming:** This was probably the hardest concept for me initially. Using Celery with RabbitMQ for background tasks felt like magic once I wrapped my head around it.

**Performance Optimization:** Nothing teaches you about caching strategies like having your API response times measured in seconds instead of milliseconds.

## Some Real Problems I Had to Solve

The N+1 query problem hit me hard early on. I was making database calls in loops without realizing it, and my local development setup was fast enough that I didn't notice until we deployed to staging. Learning about `select_related()` and `prefetch_related()` was a lifesaver.

API rate limiting was another headache. Users were hitting our endpoints way more than expected, and we had to implement proper throttling. The Django REST Framework throttling classes made this much easier than rolling our own solution.

Setting up reliable CI/CD pipelines took longer than I'm proud to admit. Lots of "works on my machine" moments that taught me the importance of environment consistency and proper testing practices.

## What I'd Do Differently

If I started over, I'd write tests from day one. I know everyone says this, but seriously - the amount of time I spent manually testing things that could have been automated is embarrassing.

I'd also spend more time on documentation earlier in the process. Coming back to a project after a few weeks and trying to remember why you made certain decisions is not fun.

## The Collaboration Aspect

Working with other students was honestly one of the best parts.in  this Discord channels   where we  shared  code snippets, debug issues together, and give each other feedback on our projects and milestones .


## Looking Back

Six months ago, I could barely explain what REST meant. Now I'm comfortable building full-featured APIs, setting up deployment pipelines, and even helping newer students debug their code.

The program definitely challenged me, but that's exactly what I needed. There's something satisfying about solving a problem that seemed impossible a few weeks earlier.

If you're considering a similar program or just getting into backend development, my advice is simple: embrace the struggle, ask lots of questions, and don't be afraid to share your code with others. The feedback will make you better faster than trying to figure everything out alone.

---

*"The only way to learn a new programming language is by writing programs in it." - Dennis Ritchie*

Thanks for taking the time to read through this. Feel free to reach out if you have questions about any of the projects or want to chat about backend development!


 #ABOUT MY PROJECT  :
 

# 🎬 Movie Recommendation Backend

A backend API built with Django for a movie recommendation app. It integrates with TMDb to fetch trending and recommended movies, allows users to save their favorites, and includes caching and full API documentation.

## 📌 About the Project

This project is all about building a smart, efficient, and scalable backend for a movie recommendation app. Using Django, it connects with the TMDb API to fetch real-time trending and recommended movie data. Users can sign up, log in with JWT authentication, and save their favorite movies for easy access. To make the experience fast and smooth, the backend uses Redis caching to reduce API calls and response time. The goal is to mirror a real-world production-ready backend that’s secure, fast, and easy for frontend developers to plug into—complete with Swagger API docs for a seamless integration experience.

## 🚀 Overview

This case study focuses on developing a robust backend for a movie recommendation application. The backend provides APIs for retrieving trending and recommended movies, user authentication, and saving user preferences. It emphasizes performance optimization and comprehensive API documentation.

## 🎯 Project Goals

- **API Creation:** Develop endpoints for fetching trending and recommended movies.
- **User Management:** Implement user authentication and the ability to save favorite movies.
- **Performance Optimization:** Enhance API performance with caching mechanisms.

## 🛠 Technologies Used

- **Django** – Backend framework  
- **PostgreSQL** – Relational database  
- **Redis** – Caching system  
- **Swagger** – API documentation  
- **TMDb API** – External movie data provider  

## 🌟 Key Features

- 🔍 **Trending & Recommended Movies** – Real-time data from TMDb  
- 🔐 **JWT Authentication** – Secure login & user access  
- ❤️ **Favorites** – Users can save and manage favorite movies  
- ⚡ **Caching with Redis** – Faster responses and reduced API calls  
- 📄 **Swagger Documentation** – All endpoints documented and accessible  

## 🧰 Git Commit Workflow

### Initial Setup
- `feat: set up Django project with PostgreSQL`
- `feat: integrate TMDb API for movie data`

### Feature Development
- `feat: implement movie recommendation API`
- `feat: add user authentication and favorite movie storage`

### Optimization
- `perf: add Redis caching for movie data`

### Documentation
- `feat: integrate Swagger for API documentation`
- `docs: update README with API details`



## ✅ Evaluation Criteria

- **Functionality:** Endpoints work as expected; authentication and favorites are functional.
- **Code Quality:** Modular, clean code following Django and Python best practices.
- **Performance:** Redis caching speeds up responses; optimized queries.
- **Documentation:** Clear, useful Swagger docs; complete README setup instructions.

