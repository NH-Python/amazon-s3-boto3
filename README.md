# Amazon S3 with `boto3`

[Presentation Slides](https://docs.google.com/presentation/d/1uMYRtHMHqkteUdVO1WdvpC506LGaq9krTKdHZkxYasw/edit?usp=sharing)

## Initial Setup
(These steps work for me; they may need to be tweaked to run in your environment)
1. Create and activate a virtual environment
    ```
    $ pyenv shell 3.8.1
    $ python -m venv venv
    $ source venv/bin/activate
    (venv)$
    ```
1. Install required packages
    ```
    (venv)$ pip install -r requirements.txt
    ```
1. Create a file named `.awsconfig` file containing your AWS user's access key id and secret.  *DO NOT* check this file into git (it's ignored using `.gitignore` by default)
1. Update the path in `.env` to reflect the path to the `.awsconfig` file you created above. 

## Running Scripts
1. Activate the virtual environment
    ```
    $ source venv/bin/activate
    (venv)$
    ```
1. Set the environment variables
    ```
    (venv)$ source .env
    ```
1. Execute script
    ```
    (venv)$ ./<script_name> 
    ```

