<div id="top"> </div>

<!---- PROJECT LOGO ----> 
<div align="center">
  <a href="https://github.com/vihugoos/liber">
    <img src="https://user-images.githubusercontent.com/44311634/213873944-91230648-2fae-4e03-9c29-dcb7d68acb38.png" alt="Logo" height="90"/>
  </a>

  <h2 align="center"> 
    Liber - Advice and Solutions for Doctors
  </h2>
  
  <p align="center">
    Platform of the consulting company Liber, developed with Bootstrap and Django. <br/>
    Explore <a href="https://docs.djangoproject.com/en/3.2/">Django</a> or <a href="https://getbootstrap.com/docs/4.6/getting-started/introduction/">Bootstrap</a> docs &#187; <br/> <br/>
    <a href=""> View Demo Project </a> &nbsp;•&nbsp;
    <a href="https://github.com/vihugoos/liber/issues"> Report Bug </a> &nbsp;•&nbsp;
    <a href="https://github.com/vihugoos/liber/issues"> Request Feature </a>
  </p>
</div>


<!---- TABLE OF CONTENTS ----> 
<details>
  <summary> Table of Contents </summary>
  <ol>
    <li>
      <a href="#about-the-project"> About The Project </a>
      <ul>
        <li><a href="#built-with"> Built With </a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started"> Getting Started </a>
      <ul>
        <li><a href="#prerequisites"> Prerequisites </a></li>
        <li><a href="#installation"> Installation </a></li>
      </ul>
    </li>
    <li><a href="#usage"> Usage </a></li>
    <li><a href="#contributing"> Contributing </a></li>
    <li><a href="#license"> License </a></li>
    <li><a href="#contact"> Contact </a></li>
  </ol>
</details>


<!---- THE PROJECT ---->
## About The Project

<img src="https://user-images.githubusercontent.com/44311634/178084690-1e2c0794-d04a-444d-9e96-0ff181cb4dc8.gif" align="center" alt="Project Home Page">
A platform for customers to request different types of services and to be able to follow the progress of their requests via their profile. Request management is done in the admin panel. 


### Built With 

<div style="display: inline_block">
    <!-- Icon Python -->
    <a href="https://docs.python.org/3.8/"> 
      <img align="center" alt="Icon-Python" height="33" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"> 
    </a> 
    <!-- Icon Django -->
    <a href="https://docs.djangoproject.com/en/3.2/"> 
      <img align="center" alt="Icon-Django" height="33" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg"> 
    </a> &nbsp; 
    <!-- Icon Bootstrap -->
    <a href="https://getbootstrap.com/docs/4.6/getting-started/introduction/"> 
      <img align="center" alt="Icon-Bootstrap" height="35" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bootstrap/bootstrap-plain.svg"> 
    </a> &nbsp;  
    <!-- Icon Docker -->
    <a href="https://www.docker.com/"> 
      <img align="center" alt="Icon-Docker" height="52" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg"> 
    </a> &nbsp;
    <!-- Icon PostgreSQL -->
    <a href="https://www.postgresql.org/"> 
      <img align="center" alt="Icon-PostgreSQL" height="35" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-plain.svg"> 
    </a>
</div>

<br/>
<br/>


<!---- GETTING STARTED ----> 
## Getting Started

To get started, you need to have <strong>Python 3.8+</strong> installed on your machine, for more information, visit <a href="https://www.python.org/downloads/"> Python Downloads</a> or <a href="https://www.anaconda.com/products/distribution">Anaconda Distribuition</a>. You will also need to have <strong>Docker</strong> installed, for more information visit <a href="https://docs.docker.com/engine/install/">Docker Engine Install</a>. 

<strong>Obs:</strong> This guide will only serve to run the project locally (development environment), initially based on linux systems.


### Prerequisites

Other than Python and Docker installed, no prerequisites are needed to install the application.


### Installation

1. Clone the repo 
   ```bash
   git clone https://github.com/vihugoos/liber.git
   ```
2. Inside the project root directory, create a python virtual environment 
   ```bash
   python3 -m venv virtual-env
   ```
3. Enable virtual environment 
   ```bash
   source virtual-env/bin/activate 
   ```
5. Install all dependencies 
   ```bash
   pip install -r requirements.txt
   ```
6. Create a postgres container docker 
   ```bash
   docker run --name liber -e POSTGRES_DB=liber -e POSTGRES_PASSWORD=docker -p 5432:5432 -d postgres
   ```
7. Run the migrations
   ```bash
   python3 manage.py migrate
   ```
 

<!---- USAGE EXAMPLES ---->
## Usage

With the installation complete, we can start the project. 

* Starting the project 
   ```bash
   python3 manage.py runserver
   ```

<br/>
To enjoy the entire application, create a super user with the following command and follow the terminal instructions, remembering that in the 'plan' option it will be necessary to type <strong>'Basic'</strong>, <strong>'Premium'</strong> or <strong>'Black'</strong> to finish creating the user. <br/> <br/> 

You will be able <strong>to track</strong> and <strong>change all requests</strong> in the admin panel accessing [`localhost:8000/accounts/admin`](http://localhost:8000/accounts/admin) <br/> 

* Command to create super user 
   ```bash
   python3 manage.py createsuperuser
   ```
<br/>


<!---- CONTRIBUTING ---->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
<br/>


<!---- LICENSE ----> 
## License

Distributed under the CC0 1.0 Universal. See `LICENSE.txt` for more information.
<br/> <br/> 


<!---- CONTACT ---->
## Contact

Developer @vihugoos - victorhugoos@live.com 

<p align="right"><a href="#top"> &#129045; back to top </a></p> 
