initialization files for dash plotly app

1. before initialization, good to upgrade related packages first
2. create environment and git
  1. `$ cd folder`: folder name must match the appName on dash portal
  2. `$ git init`
  3. `$ virtualenv venv`
  4. `$ source venv/bin/activate` in linux, or `venv\Scripts\activate` in windows
    - should install dash, plotly, gunicorn
3. initialize utility files: `.gitignore`, `Procfile`, `requirements.txt`, `runtime.txt`
4. initialize `app.py`
5. initialize app `appName` on dash portal
6. set up remote repository connection
  1. `$ git remote add plotly https://username:password@dash.pall.com/GIT/appName`
  2. `$ git add .`
  3. `$ git commit -m "…"`
  4. `$ git push plotly master`
