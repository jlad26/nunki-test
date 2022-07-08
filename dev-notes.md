Main file must be called `app.py`
Script runs as a module on the Azure server

To deploy on Azure, zip as app.zip the following - app.py , requirements.txt and imports folder - then deploy with:
`curl -X POST -H 'Content-Type: application/zip' -u '$NunkiTest' -T app.zip https://nunkitest.scm.azurewebsites.net/api/zipdeploy` and use password that is in Deployment Center > FTPS Credentials