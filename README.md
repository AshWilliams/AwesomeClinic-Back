# AwesomeClinic-Back

##Azure

Create Service Principal
`az ad sp create-for-rbac --name "GHActions" --role contributor --scopes /subscriptions/<SUBSCRIPTION_ID>/resourceGroups/<RESOURCE_GROUP> --sdk-auth`

Download or fork this repository to your local machine.     

Docker Image Name: `ashwilliams/awesome-clinic-backend:flask` 

Windows Powershell ENV Variables:    

`$env:FLASK_APP = "backend.py"`    
`$env:PYTHONIOENCODING = "UTF-8"`

Run the app:    

`flask run`     
`docker run -d -p 5000:5000 ashwilliams/awesome-clinic-backend:flask`

Head to `localhost:5000/profile/` or `localhost:5000/appointments/` to check out the application    

To check the OpenApi documentation: `http://localhost/apidocs/` 

Run tests:
`python .\backend.test.py -v`

