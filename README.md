<div id="top"> </div>
<br/>

<!-- PROJECT LOGO --> 
<div align="center">
  <a href="https://github.com/vihugoos/liber">
    <img src="https://user-images.githubusercontent.com/44311634/177224034-97d6fcb2-3dc2-4091-b016-4b901fbb681f.png" alt="Logo" height="100"/>
  </a>

  <h2 align="center"> 
    Liber - Advice and Solutions for Doctors
  </h2>
  
  <p align="center">
    Platform of the consulting company Liber, developed with Bootstrap and Django. <br/>
    Explore <a href="https://docs.djangoproject.com/en/3.2/">Django</a> or <a href="https://getbootstrap.com/docs/4.6/getting-started/introduction/">Bootstrap</a> docs &#187; <br/> <br/>
    <a href="https://liber-website.herokuapp.com/"> View Demo Project </a> &nbsp;•&nbsp;
    <a href="https://github.com/vihugoos/liber/issues"> Report Bug </a> &nbsp;•&nbsp;
    <a href="https://github.com/vihugoos/liber/issues"> Request Feature </a>
  </p>
</div>


<!-- TABLE OF CONTENTS --> 
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


<!-- THE PROJECT -->
## About The Project

<img src="https://user-images.githubusercontent.com/44311634/177225042-e1127ae0-ef95-42e7-9e80-0fc47074e9f3.jpg" align="center" alt="Project Home Page">
Specialized advice for medical professionals, offering a range of services with the aim of preserving our client's greatest asset: time. The services range from homemade, vehicles to the availability of motoboy.


### Built With 

<div style="display: inline_block">
    <!-- Icon Django -->
    <a href="https://docs.djangoproject.com/en/3.2/"> 
      <img align="center" alt="Icon-Django" height="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg"> 
    </a> &nbsp; 
    <!-- Icon Bootstrap -->
    <a href="https://getbootstrap.com/docs/4.6/getting-started/introduction/"> 
      <img align="center" alt="Icon-Django" height="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bootstrap/bootstrap-plain.svg"> 
    </a> &nbsp;  
    <!-- Icon PostgreSQL -->
    <a href="https://www.postgresql.org/"> 
      <img align="center" alt="Icon-Django" height="40" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-plain.svg"> 
    </a>
</div>

<br/>
<br/>


<!-- GETTING STARTED --> 
## Getting Started

To get started, you need to have <strong>Python 3.8+</strong> installed on your machine. For more information, visit <a href="https://www.python.org/downloads/"> Python Downloads</a> or <a href="https://www.anaconda.com/products/distribution">Anaconda Distribuition</a>. You will also need to have <strong>PostgreSQL</strong> installed, for more information visit <a href="https://www.postgresql.org/download/"> PostgreSQL Downloads</a>. 

### Prerequisites

First of all, we need to ensure that the <i>database server</i> is running, to do so, run the following commands. <strong>WARNING:</strong> Always looking at the installed version of PostgreSQL.

* Windows Terminal (as administrator)
   ```cmd
   net start postgresql-x64-14
   ```


### Installation

1. Clone the repo 
   ```bash
   git clone https://github.com/vihugoos/liber.git
   ```
2. Change the settings in `.\liber\settings.py` 
   ```python
    DEBUG = True
   
    DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': 'liber',
          'USER': 'postgres',
          'PASSWORD': '@yourPasswordRoot',
          'HOST': 'localhost',
          'PORT': '5432'
      }
    }
   ```
3. Inside the project root directory, create a python virtual environment 
   ```cmd
   python3.8 -m venv virtual-env
   ```
4. Enable virtual environment in cmd terminal
   ```cmd
   cd virtual-env/Scripts/Activate
   ```
5. Go back to the root directory and install all dependencies 
   ```cmd
   pip install -r requirements.txt
   ```
6. Run the migrations
   ```cmd
   python manage.py migrate
   ```
 

<!-- USAGE EXAMPLES -->
## Usage

With the installation complete, we can start the project. 

* Starting the project 
   ```cmd
   python manage.py runserver
   ```

<br/>
To enjoy the entire application, create a super user with the following command and follow the terminal instructions. You will be able <strong>to track</strong> and <strong>change all requests</strong> in the admin panel accessing <strong>localhost:8000/accounts/admin/</strong> 
<br/> <br/>

* Command to create super user 
   ```cmd
   python manage.py createsuperuser
   ```
<br/>


<!-- CONTRIBUTING -->
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


<!-- LICENSE --> 
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.
<br/> <br/> 


<!-- CONTACT -->
## Contact

Developer Victor Hugo - victorhugoos@live.com 

<p align="right"><a href="#top"> &#129045; back to top </a></p> 
