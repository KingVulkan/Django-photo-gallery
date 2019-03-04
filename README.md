# Django-photo-gallery

A personal Django-photo-gallery application that displays my photos for others to see.

##Author

Abdulrahman Abdullahi Omar

##Setup/Installation Requirements

Python version should be 3.6 -Django version 1.11 pip install django==1.11
Additionally, you’ll need to make sure you have pip available. You can check this by running:
pip --Version
Install Pipenv pip install --user pipenv
install virtualenv and then test it
python3.6 pip install --user --upgrade pip
python3.6 -m virtualenv env
source env/bin/activate
Inorder to clone , follow the procedure below;

On GitHub, navigate to the main page of the repository.
Under the repository name, click Clone or downlonload.
click the paste button.
Open Terminal.
Change the current working directory to the location where - you want the cloned directory to be made.
Type git clone, and then paste the URL you copied in Step 2.
git clone https://github.com/naiyoma/gallery.git Press Enter.
#creating a database

Psql
CREATE DATABASE gallery
connect to the database \c gallery
check if tables have been created \dt


Run migrations

python3.6 manage.py migrate
python3.6 manage.py makemigrations gallerys
#Running the app

python3.6 manage.py runserver

##Testing

python3.6 manage.py test gallery

##SPECIFICATIONS

| Behaviour | Input | Output | | :---------------- | :---------------: | ------------------: | | Display Images| On the Landing Page| user can view different Images | Image expand | * On the Landing Page*| user can click on an image to view more details| | As An Admin Sign in| * On The Admin Dashboard*| Post images|

##Technologies Used
HTML
CSS
Python
Django
Postgres
javascript

##Known Bugs
The website does not function well on explorer and heroku

##License

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE Copyright (c) {2018} {By Abdulrahman Abdullahi}

##live link to Heruko 



