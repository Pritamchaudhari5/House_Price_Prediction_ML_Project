# House_Price_Prediction_ML_Project


### Git Commands

1. [Git Documentation](https://git-scm.com/docs/gittutorial)



creating conda enviornment


---
open command from
---

---
conda create -p <env_name>
---

---
conda create -p venv python==3.7 -y
---

---
conda --version
---


---
-p create a virtual emviornment in a current project folder
---


---
conda activate venv/
---


---
OR
---

---
conda activate venv
---

---
pip install -r requirements.txt
---
      

 to add files to git
 ---
 git add<file_name>
 ---

 OR
 ---
 git add.
 ---

>Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check git status
---
To check all version maintained by git
---
git log
---

To create version/commit all changes by git

---
git commit -m "message"
---

To send version/changes to github
---
git push origin main
---

To check remote url
---
git remote -v
---

To set up CI/CD pipeline in heroku we need 3 information

1. Heroku_Email =
2. Heroku_API_KEY =
3. HEROKU_APP_NAME=
 


 Build docker image
 ---
 docker build -t <image_name>:<tagname> .
 ---

> NOte: Image name for docker must be lowercase

to list docker images
---
docker images
---

run docker image
---
docker run -p 5000:5000 -e PORT=5000 <image id>
---
To check running containers in docker
---
docker ps
---

To stop docker container
---
docker stop<container_id>
---

---
python setup.py install
---
pip intall -e .