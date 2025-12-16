@echo off
echo Installing this_project_aims_to_develop_a_backend_api_for_the_designecommerceproductu_platform_using_fastapi_and_sqlalchemy,_with_authentication_via_jwt. Backend Dependencies...
echo.
cd /d "%~dp0"
pip install -r requirements.txt
echo.
echo Dependencies installed successfully!
pause