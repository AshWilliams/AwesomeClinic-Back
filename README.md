# AwesomeClinic-Back

Docker Image Name: `ashwilliams/awesome-clinic-backend:flask` 

Windows Powershell ENV Variables:    

`$env:FLASK_APP = "backend.py"`    
`$env:PYTHONIOENCODING = "UTF-8"`

Run the app:    

`flask run`
`docker run -d -p 5000:5000 ashwilliams/awesome-clinic-backend:flask`

Head to `localhost:5000/profile/` or `localhost:5000/appointments/` to check out the application    


Run tests:
`python .\backend.test.py -v`
